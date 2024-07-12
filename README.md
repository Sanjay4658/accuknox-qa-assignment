# accuknox-qa-assignment
Problem Statement 2
Objective
Choose any two objectives from the list and solve using Bash or Python. We will solve the "System Health Monitoring Script" and "Automated Backup Solution" using Python.

Steps to Solve
1. System Health Monitoring Script
Create Monitoring Script
Create a file named health_monitor.py and add the following code:
python
Copy code
import psutil
import os

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    processes = len(psutil.pids())

    if cpu_usage > 80:
        print("CPU usage is above 80%")
    if memory_info.percent > 80:
        print("Memory usage is above 80%")
    if disk_info.percent > 80:
        print("Disk space usage is above 80%")

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_info.percent}%")
    print(f"Disk Space Usage: {disk_info.percent}%")
    print(f"Running Processes: {processes}")

if __name__ == "__main__":
    check_system_health()
2. Automated Backup Solution
Create Backup Script
Create a file named backup.py and add the following code:
python
Copy code
import os
import shutil
from datetime import datetime

def backup_directory(source, destination):
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        backup_folder = os.path.join(destination, f"backup_{timestamp}")
        shutil.copytree(source, backup_folder)
        print(f"Backup successful: {backup_folder}")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    source_dir = input("Enter the source directory to backup: ")
    dest_dir = input("Enter the backup destination directory: ")
    backup_directory(source_dir, dest_dir)
