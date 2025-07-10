from datetime import datetime
import logging
from sheetflow.db.connection_pool import get_connection  # Ensure this import works

# ✅ Log file setup
log_filename = f"logs/sync_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ✅ Insert or Update
def insert_or_update(name, appointment_date, table):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE Name=%s", (name,))
    result = cursor.fetchone()

    if result:
        cursor.execute(
            f"UPDATE {table} SET `Appointment Date`=%s WHERE Name=%s",
            (appointment_date, name)
        )
        print(f"🔁 Updated: {name} → {appointment_date}")
        logging.info(f"🔁 Updated: {name} → {appointment_date}")
    else:
        cursor.execute(
            f"INSERT INTO {table} (Name, `Appointment Date`) VALUES (%s, %s)",
            (name, appointment_date)
        )
        print(f"✅ Inserted: {name} → {appointment_date}")
        logging.info(f"✅ Inserted: {name} → {appointment_date}")

    conn.commit()
    cursor.close()
    conn.close()

# ✅ Get All Appointments
def get_all_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointments")
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    print("\n📋 Appointment List:")
    print("{:<5} {:<25} {:<15}".format("S.No", "Name", "Appointment Date"))
    print("-" * 50)
    for i, row in enumerate(results, start=1):
        print("{:<5} {:<25} {:<15}".format(i, row[1], row[2]))
    print("-" * 50)

    return results

# ✅ Delete by Name
def delete_appointment_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Appointments WHERE Name=%s", (name,))
    affected_rows = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()

    if affected_rows > 0:
        print(f"🗑 Deleted: {name}")
        logging.info(f"🗑 Deleted: {name}")
    else:
        print(f"⚠️ No record found to delete for: {name}")
        logging.warning(f"⚠️ No record found to delete for: {name}")

# ✅ Read by Name
def get_appointment_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointments WHERE Name=%s", (name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        print(f"🔍 Found: {result}")
        logging.info(f"🔍 Found: {result}")
    else:
        print(f"⚠️ No appointment found for: {name}")
        logging.warning(f"⚠️ No appointment found for: {name}")

    return result

# ✅ Delete All
def delete_all_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Appointments")
    conn.commit()
    print("🧹 All appointments deleted.")
    logging.warning("🧹 All appointments deleted.")
    cursor.close()
    conn.close()

# ✅ Update Name
def update_name(old_name, new_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Appointments SET Name=%s WHERE Name=%s", (new_name, old_name))
    conn.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    conn.close()

    if affected_rows > 0:
        print(f"✏️ Updated Name: {old_name} → {new_name}")
        logging.info(f"✏️ Updated Name: {old_name} → {new_name}")
    else:
        print(f"⚠️ No record found for name: {old_name}")
        logging.warning(f"⚠️ No record found for name: {old_name}")
