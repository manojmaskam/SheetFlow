from sheetflow.excel.reader import read_excel
from sheetflow.db.crud import insert_or_update
from sheetflow.config import get_config
import logging

logging.basicConfig(
    filename='logs/sync.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def sync_excel_to_mysql():
    print("🟢 Sync engine started...")
    config = get_config()
    table = config.get("DATABASE", "table")
    df = read_excel()

    for _, row in df.iterrows():
        name = row["Name"]
        appointment_date = row["Appointment Date"]
        insert_or_update(name, appointment_date, table)

    print("✅ Sync completed.")

# Only runs if executed directly
if __name__ == "__main__":
    sync_excel_to_mysql()
