import streamlit as st
import datetime
import time
import pandas as pd
import base64


current_utc_time = datetime.datetime.utcnow()
st.markdown(f"### Current Time (UTC): {current_utc_time.strftime('%H:%M')}")


# Define the event schedule
event_schedule = [
   
    {"start": "07:00", "end": "08:00", "event": "Exercise"},
    {"start": "08:00", "end": "09:00", "event": "Breakfast"},
    {"start": "09:00", "end": "10:00", "event": "Work"},
    {"start": "10:00", "end": "11:00", "event": "Work"},
    {"start": "11:00", "end": "12:00", "event": "Work"},
    {"start": "12:00", "end": "13:00", "event": "Work"},
    {"start": "13:00", "end": "14:00", "event": "Lunch"},
    {"start": "14:00", "end": "15:00", "event": "Work"},
    {"start": "15:00", "end": "16:00", "event": "Work"},
    {"start": "16:00", "end": "17:00", "event": "Work"},
    {"start": "17:00", "end": "18:00", "event": "Rest"},
    {"start": "18:00", "end": "19:00", "event": "Work"},
    {"start": "19:00", "end": "20:00", "event": "Work"},
    {"start": "20:00", "end": "21:00", "event": "Dinner"},
    {"start": "21:00", "end": "22:00", "event": "Work"},
    {"start": "22:00", "end": "23:00", "event": "Work"},
    {"start": "23:00", "end": "00:00", "event": "Work on Website"},
    {"start": "00:00", "end": "01:00", "event": "Youtube/book"},
    {"start": "01:00", "end": "02:00", "event": "Twitch"},
    {"start": "02:00", "end": "06:00", "event": "Sleep"},
]
def get_current_event(schedule, current_time):
    # Function to find the current event
    for event in schedule:
        start_time = datetime.datetime.strptime(event["start"], "%H:%M").time()
        end_time = datetime.datetime.strptime(event["end"], "%H:%M").time()

        # Handle the case where the end time is "00:00"
        if (start_time <= current_time < end_time) or (start_time <= current_time and end_time == datetime.time(0, 0)):
            return event
    return None

def get_ist_time():
    # Get the current UTC time
    current_utc_time = datetime.datetime.utcnow()

    # Calculate IST time (UTC+5:30)
    ist_time = current_utc_time + datetime.timedelta(hours=5, minutes=30)

    return ist_time.time()

def main():
    st.title("Live Timetable")

    current_time = get_ist_time()  # Get current IST time
    st.markdown(f"### Current Time (IST): {current_time.strftime('%H:%M')}")

    st.markdown("### Event Schedule")

    df = pd.DataFrame(event_schedule)
    st.dataframe(df)

    current_event = get_current_event(event_schedule, current_time)
    if current_event:
        st.markdown(f"🔵 **Current Event:** {current_event['event']} ({current_event['start']} - {current_event['end']})")

    # Add a button to download the event list as a CSV
    if st.button("Download Event List (CSV)"):
        csv_data = df.to_csv(index=False)
        b64 = base64.b64encode(csv_data.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="event_schedule.csv">Download Event List (CSV)</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
