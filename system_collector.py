#!/usr/bin/env python3
import sqlite3
import psutil
import time
from datetime import datetime
import os

DB_FILE = "system_monitor.db"

# ------------------------------
# Ensure DB and table exist
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
    print(f"Database initialized at {os.path.abspath(DB_FILE)}")

# ------------------------------
# Log system stats
# ------------------------------
def log_stats():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent / (1024 * 1024)   # Convert to MB
    recv = net_io.bytes_recv / (1024 * 1024)   # Convert to MB

    c.execute("""
    INSERT INTO system_stats (timestamp, cpu_percent, ram_percent, disk_percent, net_sent, net_recv)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (timestamp, cpu, ram, disk, sent, recv))

    conn.commit()
    conn.close()
    print(f"[{timestamp}] Logged: CPU {cpu}%, RAM {ram}%, Disk {disk}%, Sent {sent:.2f}MB, Recv {recv:.2f}MB")

# ------------------------------
# Main loop
# ------------------------------
if __name__ == "__main__":
    init_db()
    print("Starting system stats logging... Press Ctrl+C to stop.")
    try:
        while True:
            log_stats()
            time.sleep(5)   # log every 5 seconds
    except KeyboardInterrupt:
        print("Logging stopped by user.")
