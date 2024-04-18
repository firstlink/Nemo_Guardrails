# Nemo_Guardrails  

Introduction to Nemo Guardrails framework  

## Description  

This repository contains examples of Nemo Guardrails.

## Installation
***
To install the required dependencies, you can use pipenv.  
1. Make sure you have `Pipenv` installed on your system.  
2. Navigate to the root directory of this project and run: `pipenv install`

## Dependencies 

* nemoguardrails = "0.4.0"
* openai = "0.27.8"

## Getting Started

### OpenAI Configuration Steps

To configure OpenAI's GPT, follow these steps:

1. Sign Up for OpenAI: If you haven't already, sign up for an account on the OpenAI platform.  
2. Get API Key: Once you have an account, navigate to the API section and generate an API key.  
3. Configure Environment Variable: In run_guardrails.py replace environment variable value "<OpenAI-API-Key>" to API-Key from OpenAI

### Run program  

1. From your terminal navigate to root project  
2. pipenv run python run_guardrails.py