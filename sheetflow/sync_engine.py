from sheetflow.excel.reader import read_excel
from sheetflow.db.crud import insert_or_update, delete_appointment_by_name
from sheetflow.config import get_config
from sheetflow.db.connection_pool import get_connection
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
    
    # 1. Read Excel data
    df = read_excel()
    excel_names = set(df["Name"])

    # 2. Sync insert/update
    for _, row in df.iterrows():
        name = row["Name"]
        appointment_date = row["Appointment Date"]
        insert_or_update(name, appointment_date, table)

    # 3. Fetch names from SQL
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT Name FROM {table}")
    db_names = set(row[0] for row in cursor.fetchall())
    cursor.close()
    conn.close()

    # 4. Delete names not found in Excel
    to_delete = db_names - excel_names
    for name in to_delete:
        delete_appointment_by_name(name)

    print("✅ Sync completed.")

# Only runs if executed directly
if __name__ == "__main__":
    sync_excel_to_mysql()
