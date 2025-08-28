#!/usr/bin/env python3
import psutil
import sqlite3
import time
from datetime import datetime

#---------------------------------
# Setup SQLite database
#---------------------------------

def _inti_db():
    conn = sqlite3.connect("system_monitor.db")
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
    return conn

#------------------------------------
# Insert system stats
#------------------------------------
def log_stats(conn):
    c = conn.cursor()

    # Collects stats
    timestamp =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent / (1024 * 1024) #MB
    net_recv = net_io.bytes_recv / (1024 * 1024) #MB

    # Insert into DB
    c.execute("""
        INSERT INTO system_stats (timestamp, cpu_percent, ram_percent, disk_percent, net_sent, net_recv)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (timestamp, cpu_percent, ram_percent, disk_percent, net_sent, net_recv))
    
    conn.commit()

    print(f"[{timestamp}] CPU: {cpu_percent}% | RAM: {ram_percent}% | Disk: {disk_percent}% | Sent: {net_sent:.2f}MB | Recv: {net_recv:.2f}MB")

#---------------------------------------
# Main Loop
#---------------------------------------

if __name__ == "__main__":
    conn = _inti_db()
    print("Starting system monitor... (press CTRL+C to stop)")
    try:
        while True:
            log_stats(conn)
            time.sleep(5)  # collects every 5 seconds
    except KeyboardInterrupt:
        print("\nStopped Monitoring.")
        conn.close()
