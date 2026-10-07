# Phishing Awareness & Detection System

A web-based cybersecurity project built with **Python and Django** to help users identify potentially suspicious URLs while improving their awareness of phishing and social-engineering attacks.

The system analyzes submitted URLs using multiple security-related features, including URL structure, suspicious patterns, IP-based URLs, unusual characters, suspicious keywords, and lookalike/typosquatting domains such as `facebooks.com` being similar to `facebook.com`.

## Key Features

* 🔍 **URL Phishing Detection** — Analyze URLs for suspicious characteristics.
* 🛡️ **Risk Scoring** — Assign a risk score based on detected indicators.
* 🎯 **Typosquatting Detection** — Identify domains that closely resemble trusted domains.
* 📊 **Detailed Results** — Explain why a URL was considered potentially suspicious.
* 📚 **Phishing Awareness** — Learn about phishing, social engineering, fake links, and other common threats.
* 🧠 **Interactive Quizzes** — Test cybersecurity and phishing awareness through quizzes.
* 📝 **Scan History** — Keep track of previously analyzed URLs.
* 🗄️ **Django Admin** — Manage awareness content and quiz questions.

## Technology Stack

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **JavaScript**
* **SQLite**
* **Git & GitHub**

## Detection Approach

The initial version uses a **rule- and feature-based approach** rather than relying on machine learning. URL characteristics are extracted and analyzed before producing a risk score and explanation.

The project is intended as an educational cybersecurity system and does **not guarantee that a website is malicious or safe**. Results indicate potential risk based on the characteristics analyzed by the system.

## Project Goal

The goal of this project is to combine a practical **phishing URL analysis tool** with a **phishing awareness platform**, allowing users not only to analyze suspicious links but also to learn how phishing attacks work and how to recognize them.
