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
