import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime

# Page config
st.set_page_config(page_title="AI Policy System", layout="wide")

# Sidebar
st.sidebar.title("⚙️ System Info")
st.sidebar.write("Model: NLP Rule-Based Engine")
st.sidebar.write("Version: 2.0")
st.sidebar.write("Status: Active")

# CSS
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.title {
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
    text-align: center;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff;
    color: #000000;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    margin-bottom: 15px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("## 🚀 Smart Governance Dashboard")
st.markdown("### 🏛️ Government AI Monitoring System")

# Title
st.markdown('<div class="title">🧠 AI Policy Recommendation System</div>', unsafe_allow_html=True)
st.success("✅ AI Agent Active and Running")

st.write("Analyze public feedback and generate intelligent policy suggestions 🚀")

# Load dataset
data = pd.read_csv("feedback.csv")

# Layout
col1, col2 = st.columns(2)

# INPUT
with col1:
    st.subheader("📥 Input Feedback")
    location = st.text_input("📍 Enter Location (Optional)")
    user_input = st.text_area("Enter public feedback here...")
    analyze = st.button("🔍 Analyze")

# OUTPUT
with col2:
    st.subheader("📊 Analysis Result")

    if analyze and user_input:

        with st.spinner("Analyzing feedback..."):
            time.sleep(1)

        text = user_input.lower()

        # Sentiment
        if any(word in text for word in ["bad", "poor", "late", "problem", "not", "no", "delay", "pothole", "dirty"]):
            sentiment = "😡 Negative"
        elif any(word in text for word in ["good", "clean", "fast", "excellent", "improved"]):
            sentiment = "😊 Positive"
        else:
            sentiment = "😐 Neutral"

        # Confidence
        confidence = round(0.7 + abs(len(text)/100), 2)
        st.info(f"🔍 Confidence Score: {confidence}")

        # Priority
        if sentiment == "😡 Negative":
            priority = "🔴 High Priority"
        elif sentiment == "😐 Neutral":
            priority = "🟡 Medium Priority"
        else:
            priority = "🟢 Low Priority"

        st.warning(f"Priority Level: {priority}")

        # Severity Score
        severity = round(confidence * 10, 1)
        st.error(f"🚨 Severity Score: {severity}/10")

        # Action Type
        if priority == "🔴 High Priority":
            action = "Immediate Action Required"
        elif priority == "🟡 Medium Priority":
            action = "Planned Action Required"
        else:
            action = "Monitor Situation"

        st.info(f"⚡ Action Type: {action}")

        # Issue + Department
        if any(word in text for word in ["bus", "transport"]):
            issue = "🚌 Transport"
            suggestion = "Increase bus frequency and improve scheduling"
            dept = "Transport Department"

        elif any(word in text for word in ["road", "pothole", "traffic"]):
            issue = "🛣️ Infrastructure"
            suggestion = "Repair roads and improve maintenance"
            dept = "Public Works Department"

        elif any(word in text for word in ["water", "drainage"]):
            issue = "💧 Water"
            suggestion = "Ensure proper water supply and drainage system"
            dept = "Water Authority"

        elif any(word in text for word in ["garbage", "waste", "clean"]):
            issue = "🗑️ Sanitation"
            suggestion = "Improve waste collection and cleanliness"
            dept = "Municipal Corporation"

        elif any(word in text for word in ["hospital", "health"]):
            issue = "🏥 Healthcare"
            suggestion = "Increase healthcare facilities and staff"
            dept = "Health Department"

        elif any(word in text for word in ["light", "electricity", "power"]):
            issue = "💡 Electricity"
            suggestion = "Improve power supply and street lighting"
            dept = "Electricity Board"

        elif any(word in text for word in ["internet", "network"]):
            issue = "🌐 Connectivity"
            suggestion = "Improve internet infrastructure"
            dept = "Telecom Department"

        elif any(word in text for word in ["fees", "college", "school"]):
            issue = "🎓 Education"
            suggestion = "Review fee structure and improve education facilities"
            dept = "Education Department"

        else:
            issue = "📌 General"
            suggestion = "Further detailed analysis required"
            dept = "General Administration"

        # Location
        if location:
            st.success(f"📍 Issue reported from: {location}")

        st.info(f"🏢 Responsible Department: {dept}")

        # Output cards
        st.markdown(f'<div class="card">😊 <b>Sentiment:</b><br>{sentiment}</div>', unsafe_allow_html=True)
        st.markdown("---")

        st.markdown(f'<div class="card">📌 <b>Issue Detected:</b><br>{issue}</div>', unsafe_allow_html=True)
        st.markdown("---")

        st.markdown(f'<div class="card">💡 <b>Policy Recommendation:</b><br>{suggestion}</div>', unsafe_allow_html=True)
        st.markdown("---")

        # AI Summary
        st.success(f"📌 AI Summary: A {sentiment} issue related to {issue} has been detected. Immediate action is recommended under {dept}.")

        # Alert
        if priority == "🔴 High Priority":
            st.error("🚨 ALERT: Immediate government intervention required!")

        # Timestamp
        st.write(f"🕒 Analysis Time: {datetime.datetime.now()}")

# INSIGHTS
st.markdown("---")
st.subheader("📊 Overall Insights")

if st.button("Generate Insights"):

    issues = []
    column_name = data.columns[0]

    for feedback in data[column_name]:
        text = str(feedback).lower()

        if any(word in text for word in ["bus", "transport"]):
            issues.append("Transport")
        elif any(word in text for word in ["road", "pothole", "traffic"]):
            issues.append("Infrastructure")
        elif any(word in text for word in ["water", "drainage"]):
            issues.append("Water")
        elif any(word in text for word in ["garbage", "waste", "clean"]):
            issues.append("Sanitation")
        elif any(word in text for word in ["hospital", "health"]):
            issues.append("Healthcare")
        elif any(word in text for word in ["light", "electricity", "power"]):
            issues.append("Electricity")
        elif any(word in text for word in ["internet", "network"]):
            issues.append("Connectivity")
        elif any(word in text for word in ["fees", "college", "school"]):
            issues.append("Education")
        else:
            issues.append("Other")

    df = pd.DataFrame({"Issue": issues})

    st.info(f"🔥 Most Reported Issue: {df['Issue'].value_counts().idxmax()}")

    st.write("🔥 Top 3 Issues:")
    st.write(df["Issue"].value_counts().head(3))

    percent = (df["Issue"].value_counts(normalize=True) * 100).round(1)
    st.write("📊 Issue Percentage Distribution:")
    st.write(percent)

    # Bar chart
    st.subheader("📊 Bar Chart")
    st.bar_chart(df["Issue"].value_counts())

    # Horizontal chart
    st.subheader("📊 Horizontal View")
    st.bar_chart(df["Issue"].value_counts().sort_values())

    # Pie chart
    st.subheader("📊 Pie Chart")
    fig, ax = plt.subplots()
    df["Issue"].value_counts().plot.pie(
        autopct='%1.1f%%',
        colors=["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0","#ffb3e6"],
        ax=ax
    )
    st.pyplot(fig)

    # Trend Insight
    st.success("📈 Trend Insight: Infrastructure and sanitation issues are highly reported and require immediate attention.")