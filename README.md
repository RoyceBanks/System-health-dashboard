🖥️ System Health Dashboard

Real-time system monitoring with Python, Flask, SQLite, and Plotly

The System Health Dashboard allows users to monitor CPU, RAM, Disk, and Network usage in real time, with AI-style recommendations and interactive visualizations.

⸻

🚀 Project Overview

This dashboard is ideal for system administrators, IT monitoring, or personal projects. It provides:
	•	Live system metrics: CPU, RAM, Disk, Network usage
	•	Actionable recommendations with severity levels (OK / Warning / Critical)
	•	Auto-refreshing dashboard to monitor system health continuously
	•	Historical data storage using SQLite
	•	Test data support for immediate visualization

⸻

✨ Key Features
	•	Interactive charts for CPU, RAM, and Disk usage
	•	Network Upload/Download tracking
	•	AI-style actionable recommendations with color-coded severity
	•	Auto-refresh every 5 seconds
	•	Lightweight SQLite database storing historical metrics
	•	Test data display if no metrics are yet recorded


Project Structure

system-health-dashboard/
├── app.py                  # Flask web application
├── system_collector.py     # Logs system stats into SQLite DB
├── system_monitor.db       # SQLite database (auto-created)
├── templates/
│     └── dashboard.html    # HTML template for the dashboard
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

⚙️ Dependencies
	•	Python 3.7+
	•	Flask >=2.3.2
	•	Plotly >=5.16.0
	•	psutil >=5.9.5

Dependencies can be installed via pip install -r requirements.txt.

⸻

⚡ One-Click Setup & Run
<p>1.	Clone the repository and navigate into the folder.
<p>2.	Create and activate a Python virtual environment.
<p>3.	Install dependencies using requirements.txt.
<p>4.	Start the system collector to log real-time stats (keep this terminal open).
<p>5.	Launch the Flask dashboard in a separate terminal.
<p>6.	Open your browser and go to http://localhost:5000/dashboard.

The dashboard auto-refreshes every 5 seconds. Test data will display if the database is empty.

⸻

📊 Usage Highlights
	•	Monitor real-time system metrics with interactive charts
	•	Review AI-style alerts for warnings or critical issues
	•	Track historical system performance over time
	•	Works immediately with test data if database is empty

⸻

🎨 Visual Presentation

(Add screenshots or GIFs of the dashboard here for portfolio showcase)
	•	Top: CPU, RAM, and Disk line charts
	•	Middle: Network Upload/Download charts
	•	Bottom: AI-style recommendations with severity color codes

⸻

🔮 Future Enhancements
	•	Secure dashboard with user authentication
	•	Automated alerts via Email or Slack for critical thresholds
	•	Generate weekly or monthly performance reports
	•	Docker containerization for simplified deployment
	•	UI improvements: dark mode, responsive design, customizable charts

⸻

🛠 Technologies Used
	•	Python 3.7+
	•	Flask
	•	Plotly
	•	SQLite
	•	psutil
