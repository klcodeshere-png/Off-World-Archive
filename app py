import os
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    # app.root_path automatically finds the folder where this file lives
    db_path = os.path.join(app.root_path, 'space_museum.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    artifacts = conn.execute("SELECT * FROM artifacts ORDER BY id").fetchall()
    conn.close()
    return render_template("index.html", artifacts=artifacts)
