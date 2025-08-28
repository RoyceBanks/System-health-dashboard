🖥️ System Health Dashboard

[Python 3.11] [Flask 2.3.2] [SQLite]

The System Health Dashboard is a real-time system monitoring application built with Python, Flask, SQLite, and Plotly.
It provides actionable insights into system performance by tracking CPU, RAM, Disk, and Network usage, complete with AI-style recommendations.

⸻

Project Overview
	•	Visualize real-time CPU, RAM, Disk, and Network metrics
	•	Receive AI-style actionable recommendations with severity indicators (OK / Warning / Critical)
	•	Monitor systems continuously with an auto-refreshing interface
	•	Store historical performance data in SQLite database
	•	Access test data visualization immediately, even before live data is logged

⸻

Key Features
	•	Interactive charts for CPU, RAM, Disk usage
	•	Network Upload/Download monitoring
	•	AI-style actionable recommendations with visual alerts
	•	Auto-refresh every 5 seconds
	•	Lightweight database storing historical metrics
	•	Test data ensures instant visualization

⸻

Project Structure

system-health-dashboard/
├── app.py                  # Flask web application
├── system_collector.py     # Logs system stats into SQLite DB
├── system_monitor.db       # SQLite database (auto-created)
├── templates/
│     └── dashboard.html    # HTML template for the dashboard
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

⸻

Dependencies
	•	Flask >=2.3.2
	•	Plotly >=5.16.0
	•	psutil >=5.9.5

Install dependencies using the requirements.txt file in your virtual environment.

⸻

One-Click Setup & Run
	1.	Clone the repository and navigate into the project folder.
	2.	Create and activate a Python virtual environment.
	3.	Install required dependencies using the requirements.txt file.
	4.	Start the system collector to log real-time system statistics (keep this running).
	5.	Launch the Flask dashboard in a separate terminal.
	6.	Open your web browser and navigate to http://localhost:5000/dashboard.

The dashboard auto-refreshes every 5 seconds and displays CPU, RAM, Disk, and Network usage along with AI-style recommendations. Test data will be shown automatically if the database is empty.

⸻

Usage Highlights
	•	Monitor real-time system metrics in interactive charts
	•	Review AI-style alerts for warnings or critical issues
	•	Track historical data for performance analysis
	•	Works immediately with test data if the database is empty

⸻

Visual Presentation

(Add screenshots or a GIF of the dashboard here for portfolio display)
	•	Top: CPU, RAM, and Disk line charts
	•	Middle: Network Upload/Download bar chart
	•	Bottom: AI-style recommendations with color-coded severity indicators

⸻

Future Enhancements
	•	Secure dashboard with user authentication
	•	Automated alerts via Email or Slack
	•	Generate weekly or monthly performance reports
	•	Docker containerization for easy deployment
	•	UI improvements: dark mode, responsive design, customizable charts

⸻

Technologies Used
	•	Python 3.7+
	•	Flask
	•	Plotly
	•	SQLite
	•	psutil
