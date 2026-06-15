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
- Plotly


## Installation

pip install -r requirements.txt

Run Application

streamlit run app.py



## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Data Processing

* Pandas

### Data Source

* CSV Files

### Visualization

* Plotly Express

### AI Components

* Rule-Based Bug Classification
* Severity Prioritization
* Duplicate Bug Detection



## Features

1. Upload bug reports in CSV format
2. Classify bug severity (Critical, High, Medium, Low)
3. Identify affected area (Authentication, UI, Performance, General)
4. Detect possible duplicate bug reports
5. Generate clarification suggestions
6. Download analysis results as CSV






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




## Future Enhancements

* Integrate advanced AI models for more accurate bug classification and prioritization.
* Implement automatic bug assignment to the appropriate development teams.
* Enhance duplicate bug detection using semantic similarity and NLP techniques.
* Support integration with Jira, GitHub Issues, and other bug tracking platforms.
* Provide real-time bug report analysis through API-based processing.




## Assumptions

- Keyword-based classification is used.
- Input CSV must contain a "description" column.
- Bug descriptions are written in English.
- Uploaded data is assumed to be valid and properly formatted.





## Limitations

- Classification is rule-based and depends on predefined keywords.
- Accuracy may decrease for ambiguous bug descriptions.
- Large datasets are not optimized for performance.
- Does not integrate with external bug tracking tools such as Jira.



## Demo Video Link

https://www.loom.com/share/98e26de0d7a5469aadb14c44ff12c313










