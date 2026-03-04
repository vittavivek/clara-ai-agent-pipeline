\# Clara AI Agent Automation Pipeline



\## Overview

This project builds an automated pipeline that converts demo call transcripts into a preliminary AI voice agent configuration and updates the agent after onboarding data is received.



\## Architecture



Pipeline A: Demo Call → Agent v1

1\. Read demo transcript

2\. Extract structured account memo

3\. Generate Retell agent specification

4\. Store outputs



Pipeline B: Onboarding → Agent v2

1\. Read onboarding update

2\. Update existing memo

3\. Regenerate agent configuration

4\. Save versioned outputs and changelog



\## Tools Used

\- Python

\- Local JSON storage

\- Rule-based extraction



\## Folder Structure

scripts – pipeline scripts  

dataset – demo and onboarding data  

outputs – generated agent configurations  

changelog – version updates  



\## How to Run



Generate memo:



python scripts/extract\_data.py dataset/demo\_calls/demo1.txt



Generate agent:



python scripts/generate\_agent.py outputs/accounts/account\_001/v1/memo.json



Update memo with onboarding:



python scripts/update\_agent.py outputs/accounts/account\_001/v1/memo.json dataset/onboarding\_calls/onboarding1.json



Regenerate updated agent:



python scripts/generate\_agent.py outputs/accounts/account\_001/v2/memo.json



\## Output

Each account contains:



v1 → demo generated agent  

v2 → onboarding updated agent

