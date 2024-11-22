# End-to-End Text Summarizer with Huggingface Model
![](text_summarizer.png)

## Table of Contents
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [What It Does](#what-it-does)
  * [Getting Started](#Getting-started)
  * [Usage](#usage)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Techstack Used](#techstack-used)
  * [License](#license)
  * [Credits](#credits)

## Demo
[Link:](Project_Demo_Showcase.mp4)

https://github.com/user-attachments/assets/21faa3b6-c36d-4248-ba2f-cfeecd943c70


## Overview
This is an end-to-end text summarization web application based on fastAPI. It uses a **finetuned version** of the [pegasus model](https://huggingface.co/google/pegasus-cnn_dailymail) to summarize the text from any source. This project involved building an **end-to-end pipeline** encompassing **data ingestion**, **data transformation**, **model training**, **evaluation**, and **prediction**, along with **API integration** and **web hosting** for seamless user interaction. Additional features include the implementation of **GitHub Actions** for continuous integration, robust **Python logging** for efficient debugging, and workflow optimization.

## Motivation
Imagine a scenario where you want a specific context from a news paper article. Wouldn't it be a tedious task to read the entire article? Instead if you know the context information for specific section of text, you can decide whether to go through that specific section or not. So you can take help of this summarizer to find out which part of the newspaper or any other source, you are interested in. This approach is quicker and reliable as it uses a **trained** and **finetuned sequence-to sequence model** which retrieves the accurate context from the query.

## What It Does
Before going to the functioning of the project I will brief upon the initial setup
* **Create requirements.txt file to install all the dependencies.**
* **Create a series of directories and files to organize the project effectively. Configure logging to log all actions like directory and file creation or skipping existing files. Here we are allowing for modular logging.**
* Create a **pipeline** which **downloads** the data from hugging face and **extracts** it, **preprocess** and **transform** the data, **train** the model on the **prepared data** and **evaluate** the model's performance.
* The **stages** are **executed** in a **sequential manner**, ensuring that each step is completed before moving to the next.
* **Each stage logs its initiation and completion for traceability.** Errors are logged using logger.exception(), which captures both the error message and stack trace.
* **Each stage is wrapped in a try-except block to handle any exceptions gracefully.** If an exception occurs in any stage, it is logged, and the error is raised to stop further execution. This ensures that any issue is properly captured, and the pipeline does not continue in a failed state.
* Now, we have the model and tokenizer. We load these to run predictions on the unseen text. So, A prediction is created which uses this Huggingface summarizer pipeline, model, tokenizer to generate summary on a completely new text.
* **For all the above actions, we continuously integrate  with github by commiting and pushing it to the github repository.**

Now comes the part of **setting up a FastAPI web application** that exposes a simple endpoint for text summarization by integrating with the prediction pipeline. 
The **FastAPI application serves a REST API** with two routes:
* **Root Route (/):** Redirects users to the API documentation (/docs).
* **Prediction Route (/predict):** Accepts a POST request with text, processes it through the PredictionPipeline, and returns the summarized text.
* The server runs on http://0.0.0.0:8080 when executed.

## Getting Started
  We will get started with installation and set up process. Clone the repository and open the folder using Vs Code.
  ### Clone this repository into a local folder:
  ```
  git clone https://github.com/dhanushpittala11/SummarizerText_Hf_End2End_1.git
  ```
  ### Setup Environment using:
  ```bash
  conda create -p venv python==3.10 -y
  ```
  If conda is not installed, run this command in the terminal of the project environment.
  ```bash
  pip install conda
  ```
  ### Activate the environment:
  ```bash
  conda activate venv/
  ```
  ### Install all the required libraries and packages using the command:
  ```bash
  pip install -r requirements.txt
  ```
## Usage
  ### Now run the script using:
  ```bash
  python main.py
  python app.py
  ```
## Directory Tree
   ```
./.github
    ./.github/workflows     -> store workflow configuration files for github actions
        ./.gitkeep     
./artifacts
    ./artifacts/data_ingestion    -> stores the data files extracted from hugging face
        ./huggingface_dialogsum_dataset
        ./data.zip
    ./artifacts/data_transformation  -> stores the transformed  data - train,test and validation datasets
        ./test
        ./train
        ./validation
    ./artifacts/model_trainer       -> saves and stores the finetuned model and tokenizer
        ./pegasus-dialogsum-model
        ./tokenizer
    ./artifacts/model_evaluation     -> saves the metrics after model evaluation
        ./metrics.csv
./config
    ./config/config.yaml         -> defines the configuration for the end-to-end text summarization pipeline, specifying paths, URLs, model/tokenizer details 
./logs
    ./logs/continuos_logs.log    -> store runtime information, errors, and activity logs
./research                       
    ./research/ModelTrainer1.ipynb  ->  ipynb file for the pipeline which trains the model using the transformed data
    ./research/dialogsum.ipynb      -> ipynb file specific for fine tuning the model
    ./research/model_evaluation.ipynb -> ipynb file for the pipeline which evaluates the model
    ./research/DataTransformation.ipynb  -> ipynb file for the pipeline which splits the ingested data into train, test, validation sets
    ./research/DataIngestion1.ipynb   -> ipynb file for setting up the data ingestion pipeline
    ./research/research.ipynb
./src
    ./src/textSummarizer
        ./__pycache__
        ./components             
            ./__init__.py
            ./data_ingestion.py    -> download a file from a specified URL and extract its contents into a designated directory
            ./data_transformation.py  -> preprocesses the data by tokenizing dialogues,their summaries for model training, saves data to disk
            ./model_trainer.py   -> trains a text summarization model using the Pegasus architecture, saves the trained model and tokenizer
            ./model_evaluation.py  -> evaluates a trained text summarization model by computing ROUGE metrics on a test dataset
        ./config
            ./__init__.py
            ./configuration.py -> reads configuration and parameter files, creates necessary directories, and generates configuration objects
        ./constants
            ./__init__.py  -> contains the path for YAML files
        ./entity
            ./__init__.py  -> defines data classes to structure and manage configuration settings for different components of the pipeline
        ./logging
            ./__init__.py  -> sets logging system that outputs log messages to file and console for tracking  the text summarization process
        ./pipeline
            ./__init__.py
            ./prediction_pipeline.py -> Prediction pipeline
            ./stage1_dataIngestion_pipeline.py  -> Data Ingestion pipeline
            ./stage2_DataTransformation_pipeline.py -> Data Transformation  pipeline
            ./stage3_modeltrainer_pipeline.py  -> Model trainer pipeline
            ./stage4_modelevaluation_pipeline.py -> Model evaluation pipeline
        ./utils
            ./__init__.py  
            ./common.py -> read YAML files into ConfigBox and create directories while logging the process
        ./__init__.py
./venv  -> virtual environment for the project 
./.gitignore -> specifies files not to be tracked in version control
./app.py  -> 
./huggingface_dialogsum_dataset.zip -> dataset used in the project
./LICENSE
./main.py -> orchestrates and logs the execution of all the stages in the pipeline and handling exceptions for each stage.
./params.yaml  -> training parameters
./README.md   
./requirements.txt -> check all the dependencies, libraries, packages in this
./template.py  
```
   
  







