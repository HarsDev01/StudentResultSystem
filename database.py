import sqlite3

conn = sqlite3.connect('result.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
''')
conn.commit()
conn.close()

print("✅ Database initialized.")
