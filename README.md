# ACEest_Fitness and Gym - Desktop GUI App

## Overview

This is a simple fitness tracker GUI application built using `tkinter` for ACEest_Fitness and Gym.

Users can:
- Add workouts with duration
- View logged workouts

---

## 🛠️ How to Run the App Locally

```bash
git clone https://github.com/2024tm93260/DevOps-Assignement1.git
cd C:\Repos\2024tm93260
pip install -r requirements.txt
python ACEest_Fitness.py

---

## ⚙️ GitHub Actions Pipeline
This project uses GitHub Actions for Continuous Integration (CI).

On every push / PR:
Checkout code → Gets your repo.
Set up Python → Uses Python 3.10.
Install dependencies → Installs from requirements.txt.
Run tests → Executes all unit tests (Unit_TestCase.py).
