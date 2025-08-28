from flask import Flask, jsonify, render_template
import sqlite3
import plotly.graph_objs as go
import plotly
import json
<<<<<<< HEAD
=======
import os
from datetime import datetime
import random  # only for test data if DB is empty
>>>>>>> 50eadb6 (Initial commit fix)

app = Flask(__name__)
DB_FILE = "system_monitor.db"

# ------------------------------
<<<<<<< HEAD
# DB Helpers
# ------------------------------
def fetch_recent_stats(limit=60):
    """Return last `limit` rows from DB as list of dicts (oldest -> newest)."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "SELECT timestamp, cpu_percent, ram_percent, disk_percent, net_sent, net_recv "
        "FROM system_stats ORDER BY id DESC LIMIT ?",
        (limit,)
    )
=======
# Initialize DB if not exists
# ------------------------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS system_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        cpu_percent REAL,
        ram_percent REAL,
        disk_percent REAL,
        net_sent REAL,
        net_recv REAL
    )
    """)
    conn.commit()
    conn.close()

# ------------------------------
# Fetch recent stats
# ------------------------------
def fetch_recent_stats(limit=20):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        SELECT timestamp, cpu_percent, ram_percent, disk_percent, net_sent, net_recv
        FROM system_stats ORDER BY id DESC LIMIT ?
    """, (limit,))
>>>>>>> 50eadb6 (Initial commit fix)
    rows = c.fetchall()
    conn.close()

    stats = []
    for row in rows:
        stats.append({
            "timestamp": row[0],
            "cpu_percent": row[1],
            "ram_percent": row[2],
            "disk_percent": row[3],
<<<<<<< HEAD
            "net_sent_mb": row[4],   # cumulative MB since boot
            "net_recv_mb": row[5],   # cumulative MB since boot
        })
    return stats[::-1]  # oldest -> newest


def net_deltas(data):
    """
    Convert cumulative sent/recv MB into per-sample deltas (MB since prior sample).
    First sample delta = 0.
    """
    up = [0.0]
    down = [0.0]
    for i in range(1, len(data)):
        d_up = max(0.0, data[i]["net_sent_mb"] - data[i-1]["net_sent_mb"])
        d_dn = max(0.0, data[i]["net_recv_mb"] - data[i-1]["net_recv_mb"])
        up.append(d_up)
        down.append(d_dn)
    return up, down


# ------------------------------
# AI-style Recommendations
# ------------------------------
def generate_recommendations(data):
    """
    Return list of dicts: {message, level} where level in {"ok","warn","crit"}.
    """
    recs = []
    if not data:
        return [{"message": "No data yet. Keep the logger running.", "level": "warn"}]

    # Averages over the window
    avg_cpu = sum(d['cpu_percent'] for d in data) / len(data)
    avg_ram = sum(d['ram_percent'] for d in data) / len(data)
    latest_disk = data[-1]['disk_percent']

    # Network (average per-sample MB up/down)
    up, down = net_deltas(data)
    avg_up = sum(up) / len(up) if up else 0.0
    avg_dn = sum(down) / len(down) if down else 0.0

    # CPU thresholds
    if avg_cpu > 90:
        recs.append({"message": f"🚨 CPU average very high ({avg_cpu:.1f}%). Check runaway processes.", "level": "crit"})
    elif avg_cpu > 80:
        recs.append({"message": f"⚠️ CPU average high ({avg_cpu:.1f}%). Consider closing heavy apps.", "level": "warn"})

    # RAM thresholds
    if avg_ram > 95:
        recs.append({"message": f"🚨 RAM critically high ({avg_ram:.1f}%). Memory pressure likely.", "level": "crit"})
    elif avg_ram > 85:
        recs.append({"message": f"⚠️ RAM usage high ({avg_ram:.1f}%). Free memory or consider upgrade.", "level": "warn"})

    # Disk thresholds (this is % used, so > 85 means getting full)
    if latest_disk > 95:
        recs.append({"message": f"🚨 Disk almost full ({latest_disk:.1f}% used). Clean large files ASAP.", "level": "crit"})
    elif latest_disk > 85:
        recs.append({"message": f"⚠️ Disk getting full ({latest_disk:.1f}% used). Consider cleanup.", "level": "warn"})

    # Network thresholds (average MB per sample window)
    if avg_up > 100 or avg_dn > 100:
        recs.append({"message": f"⚠️ High network throughput (avg ↑ {avg_up:.1f} MB, ↓ {avg_dn:.1f} MB). Check transfers.", "level": "warn"})
=======
            "net_sent": row[4],
            "net_recv": row[5]
        })
    return stats[::-1]  # oldest → newest

# ------------------------------
# Generate test data if DB is empty
# ------------------------------
def generate_test_data(num=10):
    stats = []
    now = datetime.now()
    for i in range(num):
        ts = (now).strftime("%Y-%m-%d %H:%M:%S")
        stats.append({
            "timestamp": ts,
            "cpu_percent": random.randint(10, 90),
            "ram_percent": random.randint(20, 95),
            "disk_percent": random.randint(30, 90),
            "net_sent": random.uniform(0, 50),
            "net_recv": random.uniform(0, 50)
        })
    return stats

# ------------------------------
# Generate recommendations
# ------------------------------
def generate_recommendations(data):
    recs = []
    if not data:
        return [{"message": "No data yet. Use system collector to log stats.", "level": "warn"}]

    avg_cpu = sum(d['cpu_percent'] for d in data) / len(data)
    avg_ram = sum(d['ram_percent'] for d in data) / len(data)
    latest_disk = data[-1]['disk_percent']
    avg_net_sent = sum(d['net_sent'] for d in data) / len(data)
    avg_net_recv = sum(d['net_recv'] for d in data) / len(data)

    if avg_cpu > 90:
        recs.append({"message": f"🚨 CPU critically high ({avg_cpu:.1f}%)", "level": "crit"})
    elif avg_cpu > 80:
        recs.append({"message": f"⚠️ CPU high ({avg_cpu:.1f}%)", "level": "warn"})

    if avg_ram > 95:
        recs.append({"message": f"🚨 RAM critically high ({avg_ram:.1f}%)", "level": "crit"})
    elif avg_ram > 85:
        recs.append({"message": f"⚠️ RAM high ({avg_ram:.1f}%)", "level": "warn"})

    if latest_disk > 95:
        recs.append({"message": f"🚨 Disk full ({latest_disk:.1f}%)", "level": "crit"})
    elif latest_disk > 85:
        recs.append({"message": f"⚠️ Disk high ({latest_disk:.1f}%)", "level": "warn"})

    if avg_net_sent > 50 or avg_net_recv > 50:
        recs.append({"message": f"⚠️ High network activity (Sent {avg_net_sent:.1f} MB, Recv {avg_net_recv:.1f} MB)", "level": "warn"})
>>>>>>> 50eadb6 (Initial commit fix)

    if not recs:
        recs.append({"message": "✅ System running normally.", "level": "ok"})

    return recs

<<<<<<< HEAD

# ------------------------------
# Routes
# ------------------------------
@app.route("/")
def home():
    return (
        "<h1>System Monitor API</h1>"
        "<p>JSON: <a href='/stats/recent'>/stats/recent</a></p>"
        "<p>Dashboard: <a href='/dashboard'>/dashboard</a></p>"
    )


@app.route("/stats/recent")
def recent_stats():
    data = fetch_recent_stats(limit=60)
    return jsonify(data)


@app.route("/dashboard")
def dashboard():
    data = fetch_recent_stats(limit=60)
    if not data:
        # Render a minimal page if DB hasn't got data yet
        return render_template(
            "dashboard.html",
            usageJSON="[]",
            netJSON="[]",
            recommendations=[{"message": "No data yet. Keep the logger running.", "level": "warn"}],
            timestamps=[]
        )

    timestamps = [d["timestamp"] for d in data]

    # Usage traces
    cpu_trace = go.Scatter(x=timestamps, y=[d["cpu_percent"] for d in data],
                           mode="lines+markers", name="CPU %")
    ram_trace = go.Scatter(x=timestamps, y=[d["ram_percent"] for d in data],
                           mode="lines+markers", name="RAM %")
    disk_trace = go.Scatter(x=timestamps, y=[d["disk_percent"] for d in data],
                            mode="lines+markers", name="Disk %")
    usage_traces = [cpu_trace, ram_trace, disk_trace]
    usageJSON = json.dumps(usage_traces, cls=plotly.utils.PlotlyJSONEncoder)

    # Network traces (per-sample deltas)
    up, down = net_deltas(data)
    up_trace = go.Bar(x=timestamps, y=up, name="Upload (MB / sample)")
    dn_trace = go.Bar(x=timestamps, y=down, name="Download (MB / sample)")
=======
# ------------------------------
# Flask Routes
# ------------------------------
@app.route("/")
def home():
    return "<h1>System Monitor</h1><p>Go to <a href='/dashboard'>/dashboard</a></p>"

@app.route("/dashboard")
def dashboard():
    init_db()
    data = fetch_recent_stats(limit=20)
    if not data:
        data = generate_test_data(10)

    timestamps = [d["timestamp"] for d in data]

    # CPU/RAM/Disk chart
    cpu_trace = go.Scatter(x=timestamps, y=[d["cpu_percent"] for d in data], mode='lines+markers', name='CPU %')
    ram_trace = go.Scatter(x=timestamps, y=[d["ram_percent"] for d in data], mode='lines+markers', name='RAM %')
    disk_trace = go.Scatter(x=timestamps, y=[d["disk_percent"] for d in data], mode='lines+markers', name='Disk %')
    usage_traces = [cpu_trace, ram_trace, disk_trace]
    usageJSON = json.dumps(usage_traces, cls=plotly.utils.PlotlyJSONEncoder)

    # Network chart (MB)
    up_trace = go.Bar(x=timestamps, y=[d["net_sent"] for d in data], name="Upload MB")
    dn_trace = go.Bar(x=timestamps, y=[d["net_recv"] for d in data], name="Download MB")
>>>>>>> 50eadb6 (Initial commit fix)
    net_traces = [up_trace, dn_trace]
    netJSON = json.dumps(net_traces, cls=plotly.utils.PlotlyJSONEncoder)

    # Recommendations
    recommendations = generate_recommendations(data)

<<<<<<< HEAD
    return render_template(
        "dashboard.html",
        usageJSON=usageJSON,
        netJSON=netJSON,
        recommendations=recommendations,
        timestamps=timestamps
    )

=======
    return render_template("dashboard.html",
                           usageJSON=usageJSON,
                           netJSON=netJSON,
                           recommendations=recommendations)
>>>>>>> 50eadb6 (Initial commit fix)

# ------------------------------
# Run app
# ------------------------------
if __name__ == "__main__":
<<<<<<< HEAD
    # Visit http://localhost:5000/dashboard
=======
>>>>>>> 50eadb6 (Initial commit fix)
    app.run(debug=True, host="0.0.0.0", port=5000)
