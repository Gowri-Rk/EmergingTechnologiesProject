from gensim.summarization.summarizer import summarize



def gensim_summarize(text, ratio = 0.2,word_count=None):

    return summarize(text, ratio, word_count)


def pytextrank_rank(text):

    tr = pytextrank.TextRank()
    nlp = spacy.load("en")
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
    doc = nlp(text)
    return doc



def pytextrank_get_rank(doc):

    rank = {}
    for p in doc._.phrases:
        rank[p] = [p.rank,p.count]
    return rank



def pytextrank_get_summary(doc, n=2):

    summary = ""
    for p in doc._.phrases[0:2]:
        for s in doc.sents:
            if p.text in s.text:
                summary += ''.join(s.text)
    return summary
