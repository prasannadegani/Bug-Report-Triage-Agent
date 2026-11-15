import streamlit as st
import pandas as pd
from difflib import SequenceMatcher
import plotly.express as px

st.set_page_config(
    page_title="Bug Report Triage Agent",
    page_icon="🐞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(135deg, #F8FBFF 0%, #EAF4FF 100%) !important;
    color: #243447 !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #F8FBFF !important;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HEADINGS */

h1 {
    color: #163A63 !important;
    font-weight: 750 !important;
}

h2, h3 {
    color: #1F4E79 !important;
    font-weight: 650 !important;
}

p, label {
    color: #334155 !important;
}

/* FILE UPLOADER - WHITE BACKGROUND */

[data-testid="stFileUploader"] {
    background: #FFFFFF !important;
    border: 1px solid #D5E4F5 !important;
    border-radius: 15px !important;
    padding: 20px !important;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}

[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"] {
    background: #F5F9FF !important;
    border: 2px dashed #8BB8E8 !important;
    border-radius: 12px !important;
}

/* UPLOADER TEXT */

[data-testid="stFileUploader"] * {
    color: #334155 !important;
}

/* BROWSE FILES BUTTON */

[data-testid="stFileUploader"] button {
    background: #7B2CBF !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
}

[data-testid="stFileUploader"] button * {
    color: #FFFFFF !important;
}

/* UPLOADED CSV FILE DISPLAY */

[data-testid="stFileUploaderFile"],
[data-testid="stFileUploaderFile"] > div,
[data-testid="stFileUploaderFileName"],
[data-testid="stFileUploader"] [data-testid="stMarkdownContainer"] {
    background: #FFFFFF !important;
    color: #243447 !important;
}

[data-testid="stFileUploaderFile"] *,
[data-testid="stFileUploaderFileName"] * {
    color: #243447 !important;
}

/* BUTTONS */

.stButton > button {
    background: #7B2CBF !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    padding: 10px 25px !important;
    font-weight: 600 !important;
}

.stButton > button p,
.stButton > button span,
.stButton > button div {
    color: white !important;
}

.stButton > button:hover {
    background: #5A189A !important;
    color: white !important;
}

/* DOWNLOAD BUTTON */

.stDownloadButton > button {
    background: #7B2CBF !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
}

.stDownloadButton > button * {
    color: white !important;
}

.stDownloadButton > button:hover {
    background: #5A189A !important;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    background: white !important;
    border-radius: 12px;
    border: 1px solid #DCE8F5;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

[data-testid="stElementToolbar"] {
    opacity: 1 !important;
}

[data-testid="stAlert"] {
    border-radius: 10px;
}

/* SUMMARY CARDS */

.summary-card {
    padding: 14px 10px;
    border-radius: 13px;
    color: white !important;
    min-height: 105px;
    box-shadow: 0 5px 12px rgba(0,0,0,0.12);
    margin-bottom: 10px;
}

.summary-card .card-title {
    color: white !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    margin: 0 0 10px 0 !important;
    white-space: nowrap;
}

.summary-card .card-value {
    color: white !important;
    font-size: 30px !important;
    font-weight: 800 !important;
    margin: 0 !important;
}

.total-card {
    background: linear-gradient(135deg, #2196F3, #00BCD4) !important;
}

.critical-card {
    background: linear-gradient(135deg, #E53935, #FF5252) !important;
}

.high-card {
    background: linear-gradient(135deg, #FB8C00, #FFCA28) !important;
}

.medium-card {
    background: linear-gradient(135deg, #1565C0, #42A5F5) !important;
}

.low-card {
    background: linear-gradient(135deg, #2E7D32, #66BB6A) !important;
}

.duplicate-card {
    background: linear-gradient(135deg, #7B1FA2, #AB47BC) !important;
}

</style>
""", unsafe_allow_html=True)


st.title("🐞 Bug Report Triage Agent")

st.write(
    "Upload bug reports and automatically analyze severity, "
    "affected area, duplicate reports, and clarification requirements."
)

st.divider()


# SEVERITY CLASSIFICATION

def classify_severity(description):

    text = str(description).lower()

    critical_keywords = [
        "crash", "crashes", "system down",
        "data loss", "not starting", "freeze", "freezes"
    ]

    high_keywords = [
        "error", "failed", "fails",
        "cannot", "unable", "broken", "not working"
    ]

    medium_keywords = [
        "slow", "slowly", "delay", "performance", "lag"
    ]

    if any(word in text for word in critical_keywords):
        return "Critical"

    elif any(word in text for word in high_keywords):
        return "High"

    elif any(word in text for word in medium_keywords):
        return "Medium"

    else:
        return "Low"


# AREA CLASSIFICATION

def classify_area(description):

    text = str(description).lower()

    if any(word in text for word in [
        "login", "password", "authentication", "signin", "session"
    ]):
        return "Authentication"

    elif any(word in text for word in [
        "button", "screen", "page", "layout", "ui", "display"
    ]):
        return "User Interface"

    elif any(word in text for word in [
        "slow", "delay", "performance", "loading", "lag"
    ]):
        return "Performance"

    elif any(word in text for word in [
        "database", "data", "server", "record"
    ]):
        return "Backend"

    elif any(word in text for word in [
        "upload", "file"
    ]):
        return "File Management"

    else:
        return "General"


# CLARIFICATION SUGGESTION

def clarification(description):

    text = str(description)

    word_count = len(text.split())

    if word_count < 5:
        return (
            "More information required. "
            "Add steps to reproduce and expected behavior."
        )

    elif word_count < 8:
        return (
            "Consider adding environment details "
            "and steps to reproduce."
        )

    else:
        return (
            "Bug report contains sufficient "
            "basic information."
        )


# SIMILARITY CHECK

def similarity(text1, text2):

    return SequenceMatcher(
        None,
        str(text1).lower().strip(),
        str(text2).lower().strip()
    ).ratio()


# DUPLICATE DETECTION

def detect_duplicates(descriptions):

    results = []

    for i in range(len(descriptions)):

        duplicate = "No Duplicate"

        for j in range(i):

            score = similarity(
                descriptions[i],
                descriptions[j]
            )

            if score >= 0.70:
                duplicate = f"Possible Duplicate of Bug {j + 1}"
                break

        results.append(duplicate)

    return results


# ROW COLORING

def color_severity_row(row):

    if "Possible Duplicate" in str(row["Duplicate Status"]):

        color = (
            "background-color: #E8D5F2; "
            "color: #6A1B9A; font-weight: 600;"
        )

    elif row["Severity"] == "Critical":

        color = (
            "background-color: #FFD6D6; "
            "color: #B71C1C; font-weight: 600;"
        )

    elif row["Severity"] == "High":

        color = (
            "background-color: #FFE8B3; "
            "color: #9A5700; font-weight: 600;"
        )

    elif row["Severity"] == "Medium":

        color = (
            "background-color: #D6ECFF; "
            "color: #0D47A1; font-weight: 600;"
        )

    elif row["Severity"] == "Low":

        color = (
            "background-color: #D9F5DF; "
            "color: #1B5E20; font-weight: 600;"
        )

    else:
        color = ""

    return [color] * len(row)


# FILE UPLOAD

uploaded_file = st.file_uploader(
    "📂 Upload Bug Reports CSV",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        # FIND DESCRIPTION COLUMN

        description_column = None

        for column in df.columns:

            if column.lower().strip() in [
                "description",
                "bug_description",
                "bug description",
                "bugdescription"
            ]:

                description_column = column
                break

        if description_column is None:

            st.error(
                "❌ CSV file must contain a 'Description' column."
            )

        elif df.empty:

            st.warning("Uploaded CSV file is empty.")

        else:

            df["bug_id"] = range(1, len(df) + 1)

            uploaded_table = df[
                ["bug_id", description_column]
            ].copy()

            uploaded_table.columns = [
                "Bug ID",
                "Description"
            ]

            st.subheader("📄 Uploaded Bug Reports")

            st.dataframe(
                uploaded_table,
                hide_index=True,
                use_container_width=True,
                height=500
            )

            if st.button(
                "🔍 Analyze Bug Reports",
                use_container_width=False
            ):

                # ANALYZE BUG REPORTS

                df["Severity"] = df[description_column].apply(
                    classify_severity
                )

                df["Affected Area"] = df[description_column].apply(
                    classify_area
                )

                df["Duplicate Status"] = detect_duplicates(
                    df[description_column].fillna("").tolist()
                )

                df["Clarification Suggestion"] = (
                    df[description_column].apply(clarification)
                )

                st.success(
                    "✅ Bug reports analyzed successfully!"
                )

                # SUMMARY

                total_bugs = len(df)

                critical_bugs = df["Severity"].eq("Critical").sum()
                high_bugs = df["Severity"].eq("High").sum()
                medium_bugs = df["Severity"].eq("Medium").sum()
                low_bugs = df["Severity"].eq("Low").sum()

                duplicates = df["Duplicate Status"].str.contains(
                    "Possible Duplicate",
                    na=False
                ).sum()

                st.subheader("📌 Analysis Summary")

                col1, col2, col3, col4, col5, col6 = st.columns(6)

                cards = [
                    (col1, "🐞 Total", total_bugs, "total-card"),
                    (col2, "🚨 Critical", critical_bugs, "critical-card"),
                    (col3, "⚠️ High", high_bugs, "high-card"),
                    (col4, "🔵 Medium", medium_bugs, "medium-card"),
                    (col5, "🟢 Low", low_bugs, "low-card"),
                    (col6, "📑 Duplicates", duplicates, "duplicate-card")
                ]

                for col, title, value, css_class in cards:

                    with col:

                        st.markdown(
                            f"""
                            <div class="summary-card {css_class}">
                                <p class="card-title">{title}</p>
                                <p class="card-value">{value}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                # RESULTS TABLE

                st.subheader("📋 Bug Analysis Results")

                display_columns = [
                    "bug_id",
                    description_column,
                    "Severity",
                    "Affected Area",
                    "Duplicate Status",
                    "Clarification Suggestion"
                ]

                styled_table = (
                    df[display_columns]
                    .style
                    .apply(color_severity_row, axis=1)
                )

                st.dataframe(
                    styled_table,
                    use_container_width=True,
                    hide_index=True,
                    height=(len(df) + 1) * 36
                )

                # SEVERITY PIE CHART

                severity_count = (
                    df["Severity"]
                    .value_counts()
                    .reindex(
                        ["Critical", "High", "Medium", "Low"],
                        fill_value=0
                    )
                    .rename_axis("Severity")
                    .reset_index(name="Count")
                )

                severity_count = severity_count[
                    severity_count["Count"] > 0
                ]

                st.subheader("📊 Bug Severity Distribution")

                fig = px.pie(
                    severity_count,
                    names="Severity",
                    values="Count",
                    hole=0.50,
                    color="Severity",
                    color_discrete_map={
                        "Critical": "#EF4444",
                        "High": "#F59E0B",
                        "Medium": "#3B82F6",
                        "Low": "#22C55E"
                    }
                )

                fig.update_traces(
                    textposition="inside",
                    texttemplate="<b>%{label}</b><br>%{value} Bugs<br>%{percent}",
                    hovertemplate=(
                        "<b>%{label}</b><br>"
                        "Bugs: %{value}<br>"
                        "Percentage: %{percent}<extra></extra>"
                    ),
                    marker=dict(
                        line=dict(color="white", width=3)
                    ),
                    pull=[0.03] * len(severity_count)
                )

                fig.update_layout(
                    title={
                        "text": "<b>Bug Reports by Severity</b>",
                        "x": 0.5,
                        "xanchor": "center",
                        "font": {
                            "size": 22,
                            "color": "#1F4E79"
                        }
                    },
                    height=520,
                    margin=dict(l=20, r=20, t=80, b=20),
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#1F2937", size=13),
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=-0.08,
                        xanchor="center",
                        x=0.5,
                        title=None,
                        font=dict(size=13)
                    ),
                    annotations=[
                        dict(
                            text=f"<b>{len(df)}</b><br>Total Bugs",
                            x=0.5,
                            y=0.5,
                            font=dict(
                                size=18,
                                color="#1F4E79"
                            ),
                            showarrow=False
                        )
                    ]
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                    config={
                        "displayModeBar": True,
                        "displaylogo": False
                    }
                )

                # AFFECTED AREA CHART

                area_count = (
                    df["Affected Area"]
                    .value_counts()
                    .reset_index()
                )

                area_count.columns = [
                    "Affected Area",
                    "Count"
                ]

                st.subheader("📈 Bugs by Affected Area")

                area_fig = px.bar(
                    area_count,
                    x="Affected Area",
                    y="Count",
                    title="Affected Area Distribution",
                    text="Count",
                    color="Affected Area"
                )

                area_fig.update_traces(
                    textposition="outside"
                )

                area_fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#1F2937"),
                    showlegend=False
                )

                st.plotly_chart(
                    area_fig,
                    use_container_width=True
                )

                # DOWNLOAD RESULTS

                st.subheader("📥 Download Analysis")

                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇️ Download Analysis Results",
                    data=csv,
                    file_name="bug_triage_results.csv",
                    mime="text/csv"
                )

    except Exception as e:

        st.error(
            f"Unable to process CSV file: {e}"
        )

else:

    st.info(
        "👆 Upload a CSV file to start bug analysis."
    )
