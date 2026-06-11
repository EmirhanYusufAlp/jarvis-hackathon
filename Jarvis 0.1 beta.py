import time
from rich.console import Console
from pyfiglet import Figlet
from time import sleep
from rich.console import Console
import json
import keyboard
import os
import threading
import sys, select
import sqlite3
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from datetime import datetime
from pyfiglet import Figlet

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "ai_db.sqlite")
#Great Love

console = Console()
fig = Figlet(font='slant')
conn = sqlite3.connect("ai_db.sqlite")
c = conn.cursor()

initial_data = [
    ("Merhaba", "Merhaba! Nasılsın?"),
    ("Nasılsın?", "İyiyim, teşekkürler!"),
    ("Bugün hava nasıl?", "Bilmiyorum, dışarı bakmalısın ")
]

c.executemany("INSERT OR IGNORE INTO qa (soru, cevap) VALUES (?, ?)", initial_data)
conn.commit()
conn.close()


conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS qa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                soru TEXT UNIQUE,
                cevap TEXT
            )''')
conn.commit()

initial_data = [
    ("merhaba", "Merhaba! Nasılsın?"),
    ("nasılsın", "İyiyim, teşekkürler!"),
    ("bugün hava nasıl", "Bilmiyorum, dışarı bakmalısın ")
]
c.executemany("INSERT OR IGNORE INTO qa (soru, cevap) VALUES (?, ?)", initial_data)
conn.commit()
conn.close()

def get_answer_db(soru):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT cevap FROM qa WHERE soru=?", (soru,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def learn_answer_db(soru, cevap):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO qa (soru, cevap) VALUES (?, ?)", (soru, cevap))
    conn.commit()
    conn.close()

def load_all_data():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT soru, cevap FROM qa")
    data = c.fetchall()
    conn.close()
    if data:
        questions, answers = zip(*data)
        return list(questions), list(answers)
    else:
        return [], []
    
def train_brain(questions, answers):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(questions)
    model = MLPClassifier(hidden_layer_sizes=(12,), max_iter=10000, random_state=42)
    model.fit(X, answers)
    return model, vectorizer

def think(model, vectorizer, question):
    X = vectorizer.transform([question])
    return model.predict(X)[0]

def typewriter(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def typewriter(text, delay=0.03):
    """Harf harf yazı efekti"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def startup_animation():
    for i in range(1):
        console.clear()
        console.print(fig.renderText('JARVIS 0.1'), style="bold cyan")
        console.print(f"[yellow]Jarvis Is Starting... {'.' * i}[/yellow]")
        time.sleep(0.5)
        console.print("[green]Jarvis is Ready![/green]\n") 
        typewriter(" Merhaba efendim,ben Jarvis. Sizi için her zaman yardıma hazırım. ", 0.03)


def ai():
    startup_animation()
    while True:
        user_input = input("\n[Sen]: ").strip().lower()

        # Boş girdi kontrolü
        if not user_input:
            continue

        if user_input in ["çık", "exit", "quit"]:
            typewriter("Bana zaman ayırdığınız için teşekkür ederim efendim.")
            break

        # Veritabanı kontrolü
        answer = get_answer_db(user_input)
        if answer:
            print(f"AI  (hafızadan): {answer}")
            continue

        # Yapay sinir ağı tahmini
        questions, answers = load_all_data()
        if len(questions) >= 3:
            model, vectorizer = train_brain(questions, answers)
            predicted = think(model, vectorizer, user_input)
            print(f"AI (tahmin): {predicted}")
            # Kullanıcıya sor: doğru mu?
            feedback = input("Bu doğru mu? (e/h): ").strip().lower()
            if feedback == "h":
                new_answer = input("Doğrusunu öğret: ").strip()
                learn_answer_db(user_input, new_answer)
                print(" Öğrendim ve kaydettim.")
        else:
            print("AI: Bu soruyu bilmiyorum. Cevabını öğretir misin?")
            new_answer = input("→ Cevap: ").strip()
            learn_answer_db(user_input, new_answer)
            print(" Öğrendim ve kaydettim.")

def main():
    ai()
    

if __name__ == "__main__":
    main()

    