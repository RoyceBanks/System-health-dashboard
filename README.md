🖥️ System Health Dashboard

Real-time system monitoring with Python, Flask, SQLite, and Plotly

The System Health Dashboard allows users to monitor CPU, RAM, Disk, and Network usage in real time, with AI-style recommendations and interactive visualizations.

⸻

🚀 Project Overview

<p>This dashboard is ideal for system administrators, IT monitoring, or personal projects. It provides:
<p>	•	Live system metrics: CPU, RAM, Disk, Network usage
<p>	•	Actionable recommendations with severity levels (OK / Warning / Critical)
<p>	•	Auto-refreshing dashboard to monitor system health continuously
<p>	•	Historical data storage using SQLite
<p>	•	Test data support for immediate visualization

⸻

✨ Key Features
<p>	•	Interactive charts for CPU, RAM, and Disk usage
<p>	•	Network Upload/Download tracking
<p>	•	AI-style actionable recommendations with color-coded severity
<p>	•	Auto-refresh every 5 seconds
<p>	•	Lightweight SQLite database storing historical metrics
<p>	•	Test data display if no metrics are yet recorded


Project Structure

system-health-dashboard/
<p>├── app.py                  # Flask web application
<p>├── system_collector.py     # Logs system stats into SQLite DB
<p>├── system_monitor.db       # SQLite database (auto-created)
<p>├── templates/
<p>│     └── dashboard.html    # HTML template for the dashboard
<p>├── requirements.txt        # Python dependencies
<p>└── README.md               # Project documentation

⚙️ Dependencies <p>
	•	Python 3.7+<p>
	•	Flask >=2.3.2<p>
	•	Plotly >=5.16.0<p>
	•	psutil >=5.9.5<p>

Dependencies can be installed via pip install -r requirements.txt.<p>

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
<p>	•	Monitor real-time system metrics with interactive charts
<p>	•	Review AI-style alerts for warnings or critical issues
<p>	•	Track historical system performance over time
<p>	•	Works immediately with test data if database is empty

⸻

🎨 Visual Presentation

(Add screenshots or GIFs of the dashboard here for portfolio showcase)
<p>	•	Top: CPU, RAM, and Disk line charts
<p>	•	Middle: Network Upload/Download charts
<p>	•	Bottom: AI-style recommendations with severity color codes

⸻

🔮 Future Enhancements
<p>	•	Secure dashboard with user authentication
<p>	•	Automated alerts via Email or Slack for critical thresholds
<p>	•	Generate weekly or monthly performance reports
<p>	•	Docker containerization for simplified deployment
<p>	•	UI improvements: dark mode, responsive design, customizable charts

⸻

🛠 Technologies Used
<p>	•	Python 3.7+
<p>	•	Flask
<p>	•	Plotly
<p>	•	SQLite
<p>	•	psutil
