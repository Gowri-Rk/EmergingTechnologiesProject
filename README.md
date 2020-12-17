# content-summarizer

This project utilizes the BERT model to perform extractive text summarization on article transcripts. The contents of 
this project include a RESTful API to serve these summaries.

Paper: https://arxiv.org/abs/1906.04165

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

![alt text](https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/learningrate.png)
![alt text](https://github.com/Gowri-Rk/EmergingTechnologiesProject/blob/main/Images/xent.png)


## References
Miller, D., “Leveraging BERT for Extractive Text Summarization on Lectures”, <i>arXiv e-prints</i>, 2019.
arxiv.org/abs/1906.04165
