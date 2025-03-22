# ⏲ Time Zone Application

This is a simple web application built using **Streamlit** that allows users to view and convert time between different time zones.

## Features
- Display current time for multiple selected time zones.
- Convert time between different time zones.
- User-friendly interface with an interactive time selection.

## Installation

1. **Clone the repository** (or copy the script):
   ```sh
   git clone https://github.com/your-username/time-zone-app.git
   cd time-zone-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Requirements
Ensure you have the following Python packages installed:
   ```sh
   pip install streamlit zoneinfo
   ```

## Usage

Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

## Time Zones Supported
The app provides time conversions for the following time zones:
- UTC
- Asia/Karachi
- America/New_York
- Europe/London
- Asia/Tokyo
- Australia/Sydney
- America/Los_Angeles
- Europe/Berlin
- Asia/Dubai
- Asia/Kolkata

## How to Use
1. **View Time in Different Time Zones**  
   - Select one or multiple time zones from the dropdown.
   - The application will display the current time in the selected zones.

2. **Convert Time Between Time Zones**  
   - Choose a time using the input field.
   - Select the source and target time zones.
   - Click the **Convert Time** button to get the converted time.

## Author
Developed by **Hafiz Siddiqui**.

## License
This project is open-source and free to use.
