from watchdog.observers import Observer
from sheetflow.config import load_config
from sheetflow.watcher.excel_watcher import ExcelChangeHandler
import time
import os

if __name__ == "__main__":
    config = load_config()
    file_path = config['EXCEL']['file_path']
    folder_to_watch = os.path.dirname(file_path)

    observer = Observer()
    observer.schedule(ExcelChangeHandler(file_path), path=folder_to_watch, recursive=False)
    observer.start()

    print(f"👀 Watching: {file_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
