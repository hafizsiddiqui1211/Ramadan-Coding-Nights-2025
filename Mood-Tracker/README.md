---
# 😎 Mood Tracker App

A simple and interactive web application built using **Streamlit** that allows users to track, visualize, and filter their daily moods over time. Ideal for personal mood journaling or emotion-awareness practice.
---

## 🚀 Features

- Log your mood using a user-friendly dropdown
- Automatically saves mood entries with timestamps
- Visual summary of mood distribution (Bar Chart)
- Mood trends over time (Line Chart)
- Date-based filtering of mood entries
- All data is stored locally in a CSV file

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – for the web interface
- **Pandas** – for data manipulation
- **CSV** – for local storage

---

## 📦 Installation

1. Clone the repository or download the code.

```bash
git clone https://github.com/yourusername/mood-tracker.git
cd mood-tracker
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install streamlit pandas
```

---

## ▶️ Usage

Run the app using:

```bash
streamlit run main.py
```

This will open the app in your browser at `http://localhost:8501`.

---

## 📁 File Structure

```
mood-tracker/
│
├── main.py           # Main Streamlit app
├── mood_log.csv      # Stores mood logs (created after first log)
└── README.md         # Project documentation
```

---

## 📊 Sample Visuals

- **Mood Summary Bar Chart**: Shows how often each mood was selected.
- **Mood Trend Line Chart**: Displays how mood changes over days.

---

## 👤 Author

**[Hafiz Siddiqui](https://www.linkedin.com/in/hafiz-siddiqui-018587295)**
Made with ❤️ using Python & Streamlit

---

## 📃 License

This project is open-source and free to use.

---
