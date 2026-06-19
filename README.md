# 🥗 NutriFusion AI | Intelligent Health & Nutrition Prediction System

_An AI-powered healthcare platform that predicts health status, estimates calorie requirements, and provides personalized nutrition insights using Machine Learning, Google Gemini AI, and Streamlit._

---

# 📑 Table of Contents

- <a href="#overview">Overview</a>
- <a href="#problem-statement">Problem Statement</a>
- <a href="#proposed-solution">Proposed Solution</a>
- <a href="#key-features">Key Features</a>
- <a href="#tech-stack">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#dataset">Dataset</a>
- <a href="#machine-learning-workflow">Machine Learning Workflow</a>
- <a href="#system-architecture">System Architecture</a>
- <a href="#results">Results</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#future-enhancements">Future Enhancements</a>
- <a href="#author--contact">Author & Contact</a>

---

<h2><a id="overview"></a>Overview</h2>

NutriFusion AI is an AI-powered Health & Nutrition Prediction System designed to help users make healthier lifestyle decisions. The application combines Machine Learning models with Google Gemini AI to predict health conditions, estimate calorie requirements, analyze food images, and provide personalized nutrition recommendations through an interactive Streamlit web application.

---

<h2><a id="problem-statement"></a>Problem Statement</h2>

Many individuals struggle to maintain healthy eating habits due to the lack of personalized nutrition guidance and health monitoring tools. Existing applications often require manual tracking and provide generic recommendations.

This project addresses these challenges by integrating Machine Learning and Generative AI to automate health prediction, calorie estimation, and intelligent nutrition analysis.

---

<h2><a id="proposed-solution"></a>Proposed Solution</h2>

The proposed solution provides an AI-powered healthcare platform capable of:

- Predicting health status using Machine Learning.
- Estimating calorie requirements.
- Analyzing food images using Google Gemini AI.
- Providing personalized nutrition recommendations.
- Visualizing health metrics through an interactive dashboard.

---

<h2><a id="key-features"></a>Key Features</h2>

- 🤖 Machine Learning Health Prediction
- 🔥 Calorie Requirement Estimation
- 🥗 AI Food Image Analysis
- 💡 Personalized Nutrition Recommendations
- 📊 Interactive Dashboard
- 📈 Data Visualization using Plotly
- 🌐 Streamlit Web Application

---

<h2><a id="tech-stack"></a>Tools & Technologies</h2>

- Python
- Streamlit
- Scikit-learn
- Google Gemini AI
- Plotly
- Pandas
- NumPy
- Joblib
- Pillow

---

<h2><a id="project-structure"></a>Project Structure</h2>

```text
NutriFusion-AI/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── models/
│   ├── health_model.pkl
│   └── calorie_model.pkl
│
├── data/
│   ├── nutrition_data.csv
│   └── sample_dataset.csv
│
├── assets/
│   ├── logo.png
│   └── screenshots/
│
├── utils.py
├── train_health_model.py
└── train_calorie_model.py
```

---

<h2><a id="dataset"></a>Dataset</h2>

The project utilizes structured health and nutrition datasets containing features such as:

- Age
- Gender
- Height
- Weight
- BMI
- Activity Level
- Daily Calorie Intake

These datasets are preprocessed before training Machine Learning models.

---

<h2><a id="machine-learning-workflow"></a>Machine Learning Workflow</h2>

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Serialization (.pkl)
7. Streamlit Integration
8. AI Nutrition Analysis using Gemini AI

---

<h2><a id="system-architecture"></a>System Architecture</h2>

```text
User Input
      │
      ▼
Health Data + Food Image
      │
      ▼
Data Preprocessing
      │
      ▼
Machine Learning Models
      │
      ├── Health Prediction
      ├── Calorie Estimation
      └── Gemini AI Analysis
      │
      ▼
Nutrition Recommendation
      │
      ▼
Interactive Streamlit Dashboard
```

---

<h2><a id="results"></a>Results</h2>

- Accurate health prediction using Machine Learning
- Personalized calorie estimation
- AI-powered food image analysis
- Interactive visual dashboard
- Improved user experience with real-time predictions

---

<h2><a id="how-to-run-this-project"></a>How to Run This Project</h2>

### Clone Repository

```bash
git clone  https://github.com/Himanshu-gudiyan/nutrifusion-ai-health-nutrition-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

<h2><a id="future-enhancements"></a>Future Enhancements</h2>

- Wearable Device Integration
- Cloud Database Support
- User Authentication
- AI Diet Planning
- Mobile Application
- Real-time Health Monitoring

---

<h2><a id="author--contact"></a>Author & Contact</h2>

**Himanshu Gudiyan**

🎓 AI/ML & Data Science Enthusiast

📧 Email: himanshugudiyan7455@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/himanshu-gudiyan-aa10233a8

💻 GitHub: https://github.com/Himanshu-gudiyan

---

⭐ If you found this project useful, don't forget to **Star** this repository.