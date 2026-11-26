import os
import sqlite3
from contextlib import closing
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
path = Path(os.getenv('NOTES_DB', '/data/notes.sqlite3'))
path.parent.mkdir(parents=True, exist_ok=True)


def connect():
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db


with closing(connect()) as db, db:
    db.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, body TEXT NOT NULL)')


@app.get('/')
def index():
    with closing(connect()) as db:
        notes = db.execute('SELECT id, body FROM notes ORDER BY id DESC').fetchall()
    return render_template('index.html', notes=notes)


@app.post('/notes')
def add_note():
    text = request.form.get('body', '').strip()
    if not 1 <= len(text) <= 240:
        return 'Введите заметку от 1 до 240 символов.', 400
    with closing(connect()) as db, db:
        db.execute('INSERT INTO notes (body) VALUES (?)', (text,))
    return redirect(url_for('index'), code=303)


@app.post('/notes/<int:note_id>/delete')
def delete_note(note_id):
    with closing(connect()) as db, db:
        db.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    return redirect(url_for('index'), code=303)
