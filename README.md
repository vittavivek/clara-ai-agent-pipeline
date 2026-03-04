\# Clara AI Automation Pipeline



\## Overview



This project implements an automated pipeline that converts client call information into a deployable AI voice agent configuration.



The system simulates the workflow used by Clara Answers where information from a demo call is transformed into an initial AI agent configuration and later updated using onboarding information.



The goal of the project is to demonstrate system design, automation, structured data extraction, versioning, and reproducibility without using any paid APIs.



The solution runs completely locally using Python scripts and structured JSON outputs.



---



\# Architecture



The system is divided into two main pipelines.



Pipeline A converts demo call data into a preliminary agent configuration.



Pipeline B updates that configuration after onboarding information is received.



---



\# Pipeline A — Demo Call to Agent v1



Input

Demo call transcript.



Processing Steps



1\. Read demo transcript file

2\. Extract structured operational data

3\. Generate Account Memo JSON

4\. Generate Retell Agent Draft Specification

5\. Store versioned output



Output



outputs/accounts/<account\_id>/v1/



memo.json

agent.json



The memo contains extracted business information and routing rules.



The agent specification contains the system prompt and agent configuration.



---



\# Pipeline B — Onboarding Update to Agent v2



Input

Onboarding call data or onboarding form updates.



Processing Steps



1\. Load existing account memo (v1)

2\. Apply onboarding updates

3\. Generate updated memo

4\. Regenerate AI agent configuration

5\. Store updated version

6\. Record changes in changelog



Output



outputs/accounts/<account\_id>/v2/



memo.json

agent.json



Changelog



changelog/account\_id.md



---



\# Project Structure



clara-ai-agent-pipeline



scripts

 extract\_data.py

 generate\_agent.py

 update\_agent.py

 batch\_pipeline.py



dataset

 demo\_calls

 onboarding\_calls



outputs

 accounts

  account\_001

   v1

    memo.json

    agent.json

   v2

    memo.json

    agent.json



changelog

 account\_001.md



workflows



README.md



---



\# Scripts



\## extract\_data.py



Extracts structured business information from demo call transcripts.



The script generates a structured JSON memo containing operational data.



Example



python scripts/extract\_data.py dataset/demo\_calls/demo1.txt



Output



memo.json



---



\## generate\_agent.py



Generates an AI agent configuration using the structured memo.



The agent specification includes system prompt design and routing logic.



Example



python scripts/generate\_agent.py outputs/accounts/account\_001/v1/memo.json



Output



agent.json



---



\## update\_agent.py



Applies onboarding updates to an existing account memo and generates version 2.



Example



python scripts/update\_agent.py outputs/accounts/account\_001/v1/memo.json dataset/onboarding\_calls/onboarding1.json



Output



Updated memo.json in v2 folder.



---



\## batch\_pipeline.py



Runs the demo pipeline automatically for all transcripts inside the dataset.



Example



python scripts/batch\_pipeline.py



This automatically generates agent configurations for every demo call transcript.



---



\# Versioning



Each account maintains versioned outputs.



Version 1

Generated from demo call assumptions.



Version 2

Generated after onboarding updates.



Changes between versions are recorded inside the changelog directory.



Example



changelog/account\_001.md



---



\# Prompt Design



The generated AI agent prompt follows strict conversation flows.



Business Hours Flow



1\. Greeting

2\. Identify purpose of call

3\. Collect caller name and phone number

4\. Route or transfer the call

5\. Handle transfer failure

6\. Confirm next steps

7\. Ask if caller needs additional help

8\. Close the call



After Hours Flow



1\. Greeting

2\. Ask reason for call

3\. Confirm if the issue is an emergency

4\. If emergency collect caller name, phone number, and address

5\. Attempt call transfer

6\. If transfer fails assure follow-up

7\. Ask if additional assistance is needed

8\. Close the call



---



\# Automation Goals



The system demonstrates



Structured extraction from conversation data



Automated AI agent configuration generation



Version controlled updates between demo and onboarding stages



Batch processing for multiple customer accounts



Reproducible automation workflow



---



\# How to Run the Project



Step 1 — Generate Memo



python scripts/extract\_data.py dataset/demo\_calls/demo1.txt



---



Step 2 — Generate Agent Version 1



python scripts/generate\_agent.py outputs/accounts/account\_001/v1/memo.json



---



Step 3 — Apply Onboarding Update



python scripts/update\_agent.py outputs/accounts/account\_001/v1/memo.json dataset/onboarding\_calls/onboarding1.json



---



Step 4 — Generate Agent Version 2



python scripts/generate\_agent.py outputs/accounts/account\_001/v2/memo.json



---



Step 5 — Run Batch Processing



python scripts/batch\_pipeline.py



This processes all demo transcripts automatically and generates agent configurations for multiple accounts.



---



\# Future Improvements



With production access the system could be extended with



Automatic speech-to-text transcription



Direct Retell API integration



Automatic agent deployment



Dashboard for managing accounts



Visualization of configuration changes between versions



Integration with service management systems



---



\# Summary



This project demonstrates a structured automation pipeline that converts real world client call information into versioned AI voice agent configurations.



The solution emphasizes system design, safe automation, version control, and reproducibility while avoiding hallucinated data and preserving operational logic between demo and onboarding stages.



