import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bug Report Triage Agent")

st.title("AI Bug Report Triage Agent")

uploaded_file = st.file_uploader(
    "Upload Bug Report CSV",
    type=["csv"]
)

def classify_severity(text):
    text = text.lower()

    if "crash" in text:
        return "Critical"

    elif "error" in text:
        return "High"

    elif "slow" in text:
        return "Medium"

    else:
        return "Low"

def classify_area(text):
    text = text.lower()

    if "login" in text or "password" in text:
        return "Authentication"

    elif "button" in text:
        return "UI"

    elif "search" in text:
        return "Performance"

    else:
        return "General"

def check_duplicate(text, descriptions):
    text = text.lower()

    for d in descriptions:
        if d.lower() != text:
            common = set(text.split()) & set(d.lower().split())

            if len(common) >= 2:
                return "Possible Duplicate"

    return "No Duplicate"

def clarification(text):
    if len(text.split()) < 4:
        return ("Please provide steps to reproduce, "
                "expected result and actual result.")
    return "No clarification required"

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    results = []

    for desc in df["description"]:

        severity = classify_severity(desc)
        area = classify_area(desc)
        duplicate = check_duplicate(desc, df["description"])
        clarify = clarification(desc)

        results.append([
            severity,
            area,
            duplicate,
            clarify
        ])

    result_df = pd.DataFrame(
        results,
        columns=[
            "Severity",
            "Area",
            "Duplicate Check",
            "Clarification"
        ]
    )

    final_df = pd.concat(
        [df, result_df],
        axis=1
    )

    st.subheader("Analysis Result")
    st.dataframe(final_df)

    csv = final_df.to_csv(index=False)

    st.download_button(
        "Download Result",
        csv,
        "triage_report.csv",
        "text/csv"
  )
