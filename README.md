# End-to-End Text Summarizer with Huggingface Model
![](text_summarizer.png)

## Table of Contents
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [What it does ?](#what_it_does?)
  * [Getting Started](#Getting_started)
  * [Installation](##installation)
  * [Setup](##setup)
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
