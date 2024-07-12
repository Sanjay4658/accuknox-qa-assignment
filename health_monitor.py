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
