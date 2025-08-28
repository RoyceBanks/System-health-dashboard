🖥️ System Health Dashboard

Real-time system monitoring with Python, Flask, SQLite, and Plotly

The System Health Dashboard allows users to monitor CPU, RAM, Disk, and Network usage in real time, with AI-style recommendations and interactive visualizations.

⸻

🚀 Project Overview

<br>This dashboard is ideal for system administrators, IT monitoring, or personal projects. It provides:
<br>	•	Live system metrics: CPU, RAM, Disk, Network usage
<br>	•	Actionable recommendations with severity levels (OK / Warning / Critical)
<br>	•	Auto-refreshing dashboard to monitor system health continuously
<br>	•	Historical data storage using SQLite
<br>	•	Test data support for immediate visualization

⸻

✨ Key Features
<br>	•	Interactive charts for CPU, RAM, and Disk usage
<br>	•	Network Upload/Download tracking
<br>	•	AI-style actionable recommendations with color-coded severity
<br>	•	Auto-refresh every 5 seconds
<br>	•	Lightweight SQLite database storing historical metrics
<br>	•	Test data display if no metrics are yet recorded


Project Structure

system-health-dashboard/
<br>├── app.py                  # Flask web application
<br>├── system_collector.py     # Logs system stats into SQLite DB
<br>├── system_monitor.db       # SQLite database (auto-created)
<br>├── templates/
<br>│     └── dashboard.html    # HTML template for the dashboard
<br>├── requirements.txt        # Python dependencies
<br>└── README.md               # Project documentation

⚙️ Dependencies <br>
	•	Python 3.7+<br>
	•	Flask >=2.3.2<br>
	•	Plotly >=5.16.0<br>
	•	psutil >=5.9.5<br>

Dependencies can be installed via pip install -r requirements.txt.<br>

⸻

⚡ One-Click Setup & Run
<br>1.	Clone the repository and navigate into the folder.
<br>2.	Create and activate a Python virtual environment.
<br>3.	Install dependencies using requirements.txt.
<br>4.	Start the system collector to log real-time stats (keep this terminal open).
<br>5.	Launch the Flask dashboard in a separate terminal.
<br>6.	Open your browser and go to http://localhost:5000/dashboard.

The dashboard auto-refreshes every 5 seconds. Test data will display if the database is empty.

⸻

📊 Usage Highlights
<br>	•	Monitor real-time system metrics with interactive charts
<br>	•	Review AI-style alerts for warnings or critical issues
<br>	•	Track historical system performance over time
<br>	•	Works immediately with test data if database is empty

⸻

🎨 Visual Presentation

<br>	•	Top: CPU, RAM, and Disk line charts
<br>	•	Middle: Network Upload/Download charts
<br>	•	Bottom: AI-style recommendations with severity color codes

⸻

🔮 Future Enhancements
<br>	•	Secure dashboard with user authentication
<br>	•	Automated alerts via Email or Slack for critical thresholds
<br>	•	Generate weekly or monthly performance reports
<br>	•	Docker containerization for simplified deployment
<br>	•	UI improvements: dark mode, responsive design, customizable charts

⸻

🛠 Technologies Used
<br>	•	Python 3.7+
<br>	•	Flask
<br>	•	Plotly
<br>	•	SQLite
<br>	•	psutil
