from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (count INTEGER)")
    cur.execute("SELECT count FROM visits")
    row = cur.fetchone()

    if row:
        count = row[0] + 1
        cur.execute("UPDATE visits SET count = ?", (count,))
    else:
        count = 1
        cur.execute("INSERT INTO visits (count) VALUES (?)", (count,))

    conn.commit()
    conn.close()
    return render_template("index.html", count=count)
