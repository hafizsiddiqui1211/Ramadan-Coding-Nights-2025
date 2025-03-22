import streamlit as st
from datetime import datetime as dt
from zoneinfo import ZoneInfo as zi

st.set_page_config(
    page_icon="⏲", page_title="Time Zone Application", layout="centered")
st.title("⌛ Time Zone Application by Hafiz Siddiqui")

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"
]

selected_timezone = st.multiselect(
    "Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Selected Time Zones")
for tz in selected_timezone:
    current_time = dt.now(zi(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert time between TimeZones")
current_time = st.time_input("Current time", value=dt.now().time())
from_tz = st.selectbox("From Time Zone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Time Zone", TIME_ZONES, index=1)

if st.button("Covert Time"):
    datetime = dt.combine(dt.today(), current_time, tzinfo=zi(from_tz))
    converted_time = datetime.astimezone(
        zi(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in : {to_tz}: {converted_time}")
