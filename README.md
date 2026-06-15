## BUG-REPORT-TRIAGE-AGENT

Bug Report Triage Agent built using Python and Streamlit that automatically analyzes bug reports, classifies severity, identifies affected areas, detects possible duplicates, and provides clarification suggestions for faster bug triage.


## Overview

This application analyzes bug reports and automatically performs:

- Severity Classification
- Area Classification
- Duplicate Detection
- Clarification Suggestions


## Technologies Used

- Python
- Streamlit
- Pandas


## Installation

pip install -r requirements.txt

Run Application

streamlit run app.py


## Features

1. Upload bug reports in CSV format
2. Classify bug severity (Critical, High, Medium, Low)
3. Identify affected area (Authentication, UI, Performance, General)
4. Detect possible duplicate bug reports
5. Generate clarification suggestions
6. Download analysis results as CSV


## Assumptions

- Keyword-based classification is used.
- Input CSV must contain a "description" column.


## Limitations

- Classification is rule-based and depends on keywords.
- Large datasets are not optimized for performance.




  ## How It Works

```text
Upload CSV
    ↓
Analyze Bug Reports
    ↓
Classify Severity
    ↓
Identify Affected Area
    ↓
Detect Duplicates
    ↓
Generate Suggestions
    ↓
Display Results
    ↓
Download CSV
```




## Project Workflow

1. Upload bug report CSV file
2. Analyze bug descriptions
3. Classify severity level
4. Identify affected area
5. Detect duplicate reports
6. Generate clarification suggestions
7. Download results as CSV


## Project Architecture






```text
User Input
    ↓
Bug Report Dataset (CSV)
    ↓
Data Processing
    ↓
AI Classification Logic
    ↓
Priority Assignment
    ↓
Visualization Dashboard
    ↓
Output to User
```




## Project Structure

- app.py                 → Main Streamlit application
- bug_reports.csv        → Sample bug report dataset
- screenshots/           → Input and output screenshots
- sample_data/           → Sample input and output files
- Resume/                → Team member resumes
- requirements.txt       → Required Python libraries


## COLLEGE NAME

-ASHOKA WOMENS ENGINEERING COLLEGE

-KURNOOL

-ANDHRA PRADESH


## PROBLEM TITLE

BUG REPORT TRIAGE AGENT (QA-04)

## TEAM NAME

Team - 12



## TEAM MEMBERS

1. Degani Lakshmi Prasanna

2. Gobbirigalla Shivalakshmi

3. Dudekula Juveriya

4. Sounu Vani
   


## RESUMES

All team member resumes are available in the Resume folder.


## DEMO VIDEO LINK

https://www.loom.com/share/98e26de0d7a5469aadb14c44ff12c313



