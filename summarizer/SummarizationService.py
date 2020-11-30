from summarizer.tables import Summarization, Engine
from typing import List, Dict
from summarizer.article_summarizer import SingleModelProcessor
from nltk import tokenize
from summarizer.ArticleService import ArticleService


class SummarizationService(object):

    bert_model = SingleModelProcessor()

    def __init__(self, use_memory: bool=False):
        self.use_memory: bool = use_memory
        self.article_service: ArticleService = ArticleService(use_memory)

    def __process_content_sentences(self, body: str) -> List[str]:
        sentences = tokenize.sent_tokenize(body)
        return [c for c in sentences if len(c) > 75 and not c.lower().startswith('but') and
                not c.lower().startswith('and')
                and not c.lower().__contains__('quiz') and
                not c.lower().startswith('or')]

    def create_summary(self, lecture_id: int, request_body: Dict) -> Dict:
        lecture: Dict[str, str] = self.article_service.get_article(lecture_id)
        if not lecture:
            return {}

        summary_name: str = request_body['name']
        ratio: float = float(request_body['ratio'])
        lecture_content: str = lecture['content']

        initial_sentences: List[str] = self.__process_content_sentences(lecture_content)
        if len(initial_sentences) == 0:
            raise RuntimeError("No viable sentences found. Consider adding larger lectures.")
        sentences = self.bert_model.run_clusters(initial_sentences, ratio)
        result: str = ' '.join(sentences).strip()
        summary = Summarization(name=summary_name, lecture=lecture_id, ratio=ratio, content=result)

        session = Engine.get_instance(self.use_memory).Session()
        session.add(summary)
        session.flush()
        session.commit()

        return {
            'id': summary.id,
            'name': summary.name,
            'ratio': summary.ratio,
            'content': summary.content,
            'lecture': summary.lecture
        }

    def get_summary(self, lecture_id: int, summary_id: int) -> Dict:
        session = Engine.get_instance(self.use_memory).Session()
        query = session.query(Summarization)\
            .filter(Summarization.lecture == lecture_id)\
            .filter(Summarization.id == summary_id)
        summary: Summarization = query.first()
        if summary:
            return {
                'id': summary.id,
                'name': summary.name,
                'ratio': summary.ratio,
                'content': summary.content,
                'lecture': summary.lecture
            }
        return {}

    def list_summaries(self, name: str, lecture: int, limit: int) -> List[Dict]:
        session = Engine.get_instance(self.use_memory).Session()
        query = session.query(Summarization)
        if name:
            query = query.filter(Summarization.name == name)
        if lecture:
            query = query.filter(Summarization.lecture == lecture)

        limit = limit if limit else 10
        query = query.limit(limit)
        result = query.all()
        return [{
            'id': summary.id,
            'name': summary.name,
            'lecture': summary.lecture,
            'content': summary.content,
            'ratio': summary.ratio
        } for summary in result]

    def delete_summary(self, summary_id: int) -> Dict[str, int]:
        session = Engine.get_instance(self.use_memory).Session()
        summary = session.query(Summarization).filter(Summarization.id == summary_id).first()
        if summary:
            session.delete(summary)
            session.commit()
            return {'id': summary_id}
        return {}

