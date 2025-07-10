import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sheetflow.sync_engine import sync_excel_to_mysql
from sheetflow.config import get_config

# Load config
config = get_config()
excel_path = config["EXCEL"]["file_path"]

# Watchdog event handler
class ExcelChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Ensure it's the actual Excel file being modified
        if event.src_path.replace("\\", "/") == excel_path.replace("\\", "/"):
            print("🔄 Excel file modified. Syncing...")
            sync_excel_to_mysql()

if __name__ == "__main__":
    print("🟢 Sync engine started...")
    print(f"👀 Watching Excel file for changes: {excel_path}")

    event_handler = ExcelChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(excel_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
