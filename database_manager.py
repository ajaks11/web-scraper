import sqlite3
import os

DB_NAME = "scraped_data.db"

def create_database():
    """
    Connects to the database (creates it if it doesn't exist)
    and creates the necessary table for storing scraped highlights.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Creating a table that can store generic "highlights"
        # For quotes, 'content' is the quote, 'source' is the author.
        # For news, 'content' could be the headline, 'source' the detailed link or date.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS highlights (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                source TEXT,
                tags TEXT
            )
        ''')
        
        conn.commit()
        print(f"✅ Database '{DB_NAME}' ready.")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return None

def save_highlight(conn, content, source, tags=""):
    """
    Inserts a single scraped item into the database.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO highlights (content, source, tags)
            VALUES (?, ?, ?)
        ''', (content, source, tags))
        conn.commit()
    except sqlite3.Error as e:
        print(f"❌ Error inserting data: {e}")

def close_connection(conn):
    if conn:
        conn.close()
