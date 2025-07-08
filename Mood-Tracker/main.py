import streamlit as st
import pandas as pd
import datetime as dt
import csv
import os

MOOD_FILE = "mood_log.csv"


# ✅ Function to load mood data safely
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.path.getsize(MOOD_FILE) == 0:
        return pd.DataFrame(columns=["Date", "Mood"])

    try:
        data = pd.read_csv(MOOD_FILE)
        if "Date" in data.columns and "Mood" in data.columns:
            return data
        else:
            return pd.DataFrame(columns=["Date", "Mood"])
    except Exception:
        return pd.DataFrame(columns=["Date", "Mood"])


# ✅ Function to save mood data safely
def save_mood_data(date, mood):
    file_exists = os.path.isfile(MOOD_FILE)
    write_header = not file_exists or os.path.getsize(MOOD_FILE) == 0

    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Date", "Mood"])
        writer.writerow([date, mood])


# ✅ Streamlit Page Setup
st.set_page_config(page_icon="😶", page_title="Mood Tracker App", layout="centered")
st.title(
    "😎 Mood Tracker App by [Hafiz Siddiqui](https://www.linkedin.com/in/hafiz-siddiqui-018587295)"
)

# ✅ Logging the Mood
now = dt.datetime.now()
today_str = now.strftime("%Y-%m-%d %H:%M:%S")
st.subheader("📅 How are you feeling right now?")
mood = st.selectbox("Select Your Mood:", ["Happy😊", "Sad😢", "Angry😠", "Neutral😐"])

if st.button("Log Mood"):
    save_mood_data(today_str, mood)
    st.success("🎊 Mood Logged Successfully")

# ✅ Load mood data
data = load_mood_data()

if not data.empty:
    data["Date"] = pd.to_datetime(data["Date"])

    # ✅ Mood Distribution (Bar Chart)
    st.subheader("📊 Mood Summary")
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)

    # ✅ Mood Trend Over Time (Line Chart)
    st.subheader("📈 Mood Trend Over Time")
    daily_moods = data.copy()
    daily_moods["Day"] = daily_moods["Date"].dt.date
    mood_trend = daily_moods.groupby(["Day", "Mood"]).size().unstack(fill_value=0)
    st.line_chart(mood_trend)

    # ✅ Optional Filter by Date
    st.subheader("🔍 Filter Mood Entries by Date")
    start_date = st.date_input("From Date", value=data["Date"].min().date())
    end_date = st.date_input("To Date", value=data["Date"].max().date())

    if start_date > end_date:
        st.error("🚫 Start date cannot be after end date.")
    else:
        filtered_data = data[
            (data["Date"].dt.date >= start_date) & (data["Date"].dt.date <= end_date)
        ]
        st.write("📝 Filtered Mood Entries:")
        st.dataframe(filtered_data)
