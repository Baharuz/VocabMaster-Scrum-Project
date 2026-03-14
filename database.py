import sqlite3
from datetime import datetime

def initialize_database():
    conn = sqlite3.connect('vocab_master.db')
    cursor = conn.cursor()

    # 1. Users Tablosu (Story 1)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            UserName TEXT NOT NULL UNIQUE,
            Password TEXT NOT NULL
        )
    ''')

    # 2. Words Tablosu (Story 2 & 3)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Words (
            WordID INTEGER PRIMARY KEY AUTOINCREMENT,
            EngWordName TEXT NOT NULL,
            TurWordName TEXT NOT NULL,
            PicturePath TEXT,          -- Resim yolu (String)
            CurrentLevel INTEGER DEFAULT 0, -- 0'dan 6'ya aşamalar
            NextReviewDate DATETIME,   -- Algoritmanın belirlediği tarih
            IsLearned BOOLEAN DEFAULT 0 -- 6. aşama bitti mi?
        )
    ''')

    # 3. WordSamples Tablosu (Story 2 - Kelime Cümleleri)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WordSamples (
            SampleID INTEGER PRIMARY KEY AUTOINCREMENT,
            WordID INTEGER,
            SampleSentence TEXT,
            FOREIGN KEY (WordID) REFERENCES Words(WordID)
        )
    ''')

    conn.commit()
    conn.close()
    print("SCRUM-1: Tüm veritabanı tabloları başarıyla oluşturuldu.")

if __name__ == "__main__":
    initialize_database()