import os
import zipfile
from datetime import datetime


DIRECTORIES_TO_BACKUP = ["./"] # or list the back directory (folder names) i.e. ['1.problem-logfile-error-analyzer', '2.problem-log-file-analyze']
BACKUP_LOCATION = "../my-backup"

def create_backup():
    """
    Compress directories into a timestamped zip file.
    """
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_name = f"backup_{timestamp}.zip"
    backup_file_path = os.path.join(BACKUP_LOCATION, backup_file_name)

    
    with zipfile.ZipFile(backup_file_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for directory in DIRECTORIES_TO_BACKUP:
            for root, _, files in os.walk(directory):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, directory)
                    backup_zip.write(full_path, os.path.join(os.path.basename(directory), arcname))

    print(f"Backup created successfully: {backup_file_path}")

if __name__ == "__main__":
    os.makedirs(BACKUP_LOCATION, exist_ok=True)
    
    create_backup()
