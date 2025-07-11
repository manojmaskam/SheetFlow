# 📊 SheetFlow – Excel & MySQL Real-time Sync Tool

SheetFlow is a lightweight desktop utility built with Python that keeps an Excel sheet and a MySQL database in sync in **real-time**. It supports basic **CRUD operations**, **automatic file watching**, and **Excel export** – ideal for appointment scheduling or simple database management.

---

## ✅ Features

- 🔁 **Real-time Sync** – Watches an Excel file for live updates and syncs to MySQL instantly.
- 🧾 **Excel to SQL Sync** – All insertions and updates from Excel are captured and pushed to DB.
- 📤 **SQL to Excel Export** – Export current MySQL data back into the Excel file in the same format.
- 🔍 **CRUD Operations** – Support for:
  - Insert or Update (automatically handled)
  - Read All / By Name
  - Delete by Name / Delete All
- 📝 **Auto Logging** – Sync actions are logged daily for auditing and debugging.

---

## 📁 Folder Structure

SheetFlow/
│
├── sheetflow/
│   ├── db/
│   │   ├── connection\_pool.py
│   │   └── crud.py
│   ├── excel/
│   │   └── reader.py
│   ├── sql/
│   │   └── export\_to\_excel.py
│   ├── watcher/
│   │   └── excel\_watcher.py
│   └── sync\_engine.py
│
├── Appointments.xlsx            # Excel file (live source)
├── config.ini                   # App configuration
├── requirements.txt             # Dependencies
├── README.md
└── logs/

---

## ⚙️ Requirements

Install required libraries using:

```bash
pip install -r requirements.txt
````

Your `requirements.txt` should include:

```text
pandas==2.2.2
openpyxl==3.1.2
mysql-connector-python==8.3.0
watchdog==4.0.0
python-dotenv==1.0.1
```

---

## 🛠️ Configuration (`config.ini`)

```ini
[EXCEL]
file_path = C:/Users/dell/Desktop/Appointments.xlsx

[DATABASE]
host = localhost
port = 3306
user = root
password = your_password
database = Sheetflow_db
table = Appointments
```

---

## 🚀 How to Run

### 1. 🔄 One-Time Sync from Excel → MySQL

```bash
python -m sheetflow.sync_engine
```

---

### 2. 👀 Start Real-Time Watching (Auto-Sync on Edit)

```bash
python -m sheetflow.watcher.excel_watcher
```

---

### 3. 📤 Export SQL → Excel (in same format)

```bash
python -m sheetflow.sql.export_to_excel
```

✅ Make sure Excel is closed when exporting.

---

### 4. 🔧 Run CRUD Operations (in code or Python REPL)

* `get_all_appointments()`
* `get_appointment_by_name("Manoj")`
* `delete_appointment_by_name("Sai")`
* `delete_all_appointments()`
* `update_name("Sai", "Sai Kumar")`

All available in: `sheetflow/db/crud.py`

---

## ⚠️ Notes

* **Ensure Excel file is closed** during export to avoid permission errors.
* **Primary key (`s_no`)** should be `AUTO_INCREMENT` in your MySQL table.
* Logs are created daily inside `/logs/` directory.

---

## 🧪 MySQL Table Structure

```sql
CREATE TABLE Appointments (
    s_no INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    `Appointment Date` DATE
);
```

---

## 👤 Author

**Maskam Manoj Kumar**
Made with ❤️ for real-time data syncing between Excel and SQL.

--