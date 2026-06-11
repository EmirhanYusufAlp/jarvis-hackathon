# color_ascii_save.py
import cv2
import json
from time import sleep
from rich.console import Console
import os

console = Console()
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# -------------------- Fonksiyonlar -------------------- #
def resize_frame(frame, new_width=120):
    height, width, _ = frame.shape
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return cv2.resize(frame, (new_width, new_height))

def frame_to_ascii_color(frame):
    ascii_frame = ""
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            b, g, r = frame[i, j]
            brightness = int((r + g + b) / 3)
            char = ASCII_CHARS[brightness // 25]
            ascii_frame += f"[rgb({r},{g},{b})]{char}[/rgb({r},{g},{b})]"
        ascii_frame += "\n"
    return ascii_frame

def video_to_ascii_save(video_path, output_file="ascii_frames.json", new_width=120):
    if os.path.exists(output_file):
        # Dosya varsa tekrar dönüştürmeye gerek yok
        console.print(f"[yellow]{output_file} zaten var, yükleniyor...[/yellow]")
        with open(output_file, "r", encoding="utf-8") as f:
            frames = json.load(f)
        return frames

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        console.print("[red]Video açılamadı! Yol doğru mu?[/red]")
        return []

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = resize_frame(frame, new_width)
        ascii_frame = frame_to_ascii_color(frame_resized)
        frames.append(ascii_frame)

    with open(output_file, "/home/Emoabi32", encoding="utf-8") as f:
        json.dump(frames, f)
    cap.release()
    console.print(f"[green]{len(frames)} kare kaydedildi ve {output_file} oluşturuldu.[/green]")
    return frames

def play_ascii_frames(frames, fps=30):
    delay = 1 / fps
    for frame in frames:
        console.clear()
        console.print(frame)
        sleep(delay)
    console.clear()
    console.print("[green]🎵 Animasyon bitti! 🎵[/green]")

# -------------------- Ana -------------------- #
if __name__ == "__main__":
    video_path = "/home/Emoabi32/Masaüstü/Jarvis/animationmp4/1.mp4"  # Video dosyanın yolu
    frames = video_to_ascii_save(video_path, output_file="ascii_frames.json", new_width=120)
    if frames:
        play_ascii_frames(frames, fps=30)
