# content-summarizer

This project utilizes the BERT model to perform extractive text summarization on article transcripts. The contents of 
this project include a RESTful API to serve these summaries.

Reference Paper: https://arxiv.org/abs/1906.04165

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/title.png" width=100%>

## Architecture

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/project_architecture.png" width=100%>

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/bert_architecture.png" width=100%>

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/bert_input.png" width=100%>

## Process
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/process_flow.png" width=100%>

## Steps

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/steps_article.png" width=100%>

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/steps_create_summary.png" width=100%>

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/steps_get_summary.png" width=100%>

## ROUGH Score

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/rough_score_mean.png" width=100%>

<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/rough_score_density.png" width=100%>

## Running the service locally
First, docker is required to run the service locally. To start the service, run the command:
```bash
make run
```

## Launch the UI Interface

Start the front end service and launch tha application using
```bash
make client-run
```

## Tensorboard results for fine tuned BERT model for learning rate and xent

### Learning Rate
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/learningrate.png" width=100%>

### Xent
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/xent.png" width=100%>

## TFX artifacts

### Evaluator
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/evaluator.PNG" width=100%>

### Example
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/example.PNG" width=100%>

### Model Resolver
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/model_resolver.PNG" width=100%>

### Print Output
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/print.PNG" width=100%>

### Pusher
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/pusher.PNG" width=100%>

### Pusher Run
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/pusher_run.PNG" width=100%>

### Schema
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/schema.PNG" width=20%>

### Schema Output
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/schema_out.PNG" width=100%>

### Statistics
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/stats_.PNG" width=100%>

### Trainer
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/trainer.PNG" width=100%>

### Transfrom
<img src="https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/transform.PNG" width=100%>

## References
Miller, D., “Leveraging BERT for Extractive Text Summarization on Lectures”, <i>arXiv e-prints</i>, 2019.
arxiv.org/abs/1906.04165
