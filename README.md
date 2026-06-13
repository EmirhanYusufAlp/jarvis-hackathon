# JARVIS v0.1 (Beta) - Hackathon MVP Assistant

This project is a lightweight, neural-network-based terminal assistant and chatbot prototype (MVP) developed completely from scratch in just **6 hours** during a high school Hackathon using Python 3.10.

---

## 🧠 Core Features

* **Neural Network Backed:** Powered by `scikit-learn`'s `MLPClassifier` (Multi-Layer Perceptron) to classify, analyze, and predict user intents locally without relying on external APIs.
* **Dynamic Run-time Learning & Persistent Memory:** Integrated with an `SQLite` database. It processes live user feedback (Correct/Incorrect verification) to dynamically retrain itself and learn new responses on the fly during runtime.
* **Directory-Based Dynamic Architecture:** Built using dynamic pathing (`os.path`), making the entire project independent of absolute disk paths. It is fully portable and runs directly from its root folder.

---

## 🚀 Quick Start

1. Install the required dependencies:
   ```bash
   pip install scikit-learn numpy rich pyfiglet keyboard

2. Run the assistant

The Backstory

Before transferring to my current school, the most important thing on my mind was my first love, whom I had been infatuated with since the 8th grade. We were on good terms, but I had never confessed my feelings (my biggest mistake, and by the time I finally did, it was already too late).Around that time, there was a school hackathon, followed by a presentation to an Erasmus group that she was also a part of. Driven by that motivation, I locked in on the final day of the hackathon and wrote Jarvis from scratch during a non-stop, 6-hour coding session.Weeks later, I finally opened up to her, only to face rejection. As primitive as this project may seem technically, it holds an incredibly special place in my heart. It is the monument of my hopes from that time.

My recommendation to anyone reading this: If you love someone, say it to them **NOW**. Don't wait for the perfect code or the perfect moment. Time doesn't wait.
