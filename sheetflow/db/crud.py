from sheetflow.db.connection_pool import get_connection
import logging

def insert_or_update(name, appointment_date, table):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table} WHERE Name = %s", (name,))
    result = cursor.fetchone()

    if result:
        cursor.execute(f"UPDATE {table} SET `Appointment Date` = %s WHERE Name = %s", (appointment_date, name))
        print(f"🔁 Updated: {name} → {appointment_date}")
        logging.info(f"Updated: {name} → {appointment_date}")
    else:
        cursor.execute(f"INSERT INTO {table} (Name, `Appointment Date`) VALUES (%s, %s)", (name, appointment_date))
        print(f"✅ Inserted: {name} → {appointment_date}")
        logging.info(f"Inserted: {name} → {appointment_date}")

    conn.commit()
    cursor.close()
    conn.close()
