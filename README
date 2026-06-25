# 🎓 Wejheti — AI-Powered University Orientation Assistant

<div align="center">

# 🎓 Wejheti — وجهتي

### Helping Tunisian students choose the right university path

AI-powered recommendation system built with Machine Learning, FastAPI, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📖 Overview

Choosing a university program after obtaining the Tunisian Baccalaureate can be challenging.

**Wejheti** is an AI-powered university orientation assistant that helps students discover suitable university programs based on their Bac type and score.

The application leverages historical admission data, data processing techniques, and a recommendation engine to provide personalized academic guidance.

### Key Objectives

* Help students make informed academic decisions
* Simplify access to university admission information
* Provide personalized recommendations
* Showcase practical Machine Learning and Data Engineering skills

---

## 🚀 Features

### 🎯 Personalized Orientation

* Select Bac type
* Enter Bac score
* Receive tailored recommendations

### 📊 Recommendation Categories

#### 🚀 Ambitious Programs

Programs requiring a score slightly above the student's score.

#### ✅ Realistic Programs

Programs matching the student's academic profile.

#### 🛡️ Safe Programs

Programs with admission thresholds below the student's score.

### 🌐 REST API

The application exposes a FastAPI backend with:

* GET /bac_types
* GET /universities
* POST /orientation
* GET /

### 📚 Interactive Documentation

Swagger UI available at:

```text
http://localhost:8000/docs
```

---

## 🏗️ System Architecture

```text
Historical Admission Data
            │
            ▼
     Data Cleaning
            │
            ▼
   Feature Engineering
            │
            ▼
 Recommendation Engine
            │
            ▼
      FastAPI API
            │
            ▼
   Streamlit Frontend
            │
            ▼
 Student Recommendations
```

---

## 📂 Project Structure

```text
Wejheti/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── api/
│   │   ├── main.py
│   │   └── schemas.py
│   │
│   ├── data/
│   │   └── cleaner.py
│   │
│   ├── features/
│   │   └── engineer.py
│   │
│   └── models/
│       └── train.py
│
├── data/
│   ├── clean_scores.csv
│   └── full_clean_scores.csv
│
├── tests/
│
├── outputs/
│
├── screenshots/
│   ├── home.png
│   └── swagger.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔄 Machine Learning Workflow

### 1. Data Collection

Historical university admission scores are collected and stored in structured datasets.

### 2. Data Cleaning

Implemented in:

```python
src/data/cleaner.py
```

Tasks include:

* Missing value handling
* Data validation
* Duplicate removal
* Data standardization

### 3. Feature Engineering

Implemented in:

```python
src/features/engineer.py
```

Tasks include:

* Data transformation
* Feature preparation
* Recommendation logic

### 4. Recommendation Engine

Implemented in:

```python
src/models/train.py
```

The engine analyzes:

* Bac section
* Bac score
* Historical admission thresholds

and generates personalized recommendations.

### 5. API Layer

Built using FastAPI.

Responsibilities:

* Request validation
* Data serving
* Recommendation generation
* API documentation

### 6. Frontend Layer

Built using Streamlit.

Responsibilities:

* User interaction
* Input collection
* Result visualization

---

## 🖥️ Screenshots

### Main Application

![Home](screenshots/home.png)

### API Documentation

![Swagger](screenshots/swagger.png)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Nour-Faker/Wejheti.git

cd Wejheti
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
uvicorn src.api.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## ▶️ Run Frontend

```bash
streamlit run app/streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 📈 Example Usage

1. Select your Bac type.
2. Enter your Bac score.
3. Click **Trouver mon orientation**.
4. Explore Ambitious, Realistic, and Safe programs.
5. Make informed university choices.

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit

### Machine Learning

* Scikit-Learn

### Development Tools

* Git
* GitHub
* VS Code

---

## 🎯 Skills Demonstrated

* Data Cleaning
* Feature Engineering
* API Development
* Machine Learning Fundamentals
* Data Pipelines
* REST API Design
* Python Development
* Software Architecture
* Version Control with Git

---

## 🔮 Future Improvements

### Version 2

* Recommendation ranking score
* Advanced filtering
* Improved user interface
* Export recommendations

### Version 3

* Predictive Machine Learning models
* Historical admission trend analysis
* University comparison dashboard
* Cloud deployment

### Version 4

* AI-powered academic advisor
* Chatbot integration
* Personalized student profiles

---

## 👨‍💻 Author

### Nour Faker

Computer Engineering Student — ENICarthage

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Backend Development
* Software Engineering

GitHub:

https://github.com/Nour-Faker

---

## ⭐ Support

If you find this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🚀 Share it with others

---

Built with ❤️ using Python, FastAPI, Streamlit, and Machine Learning.
