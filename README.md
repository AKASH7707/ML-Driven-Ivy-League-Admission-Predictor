# ML-Driven Ivy League Admission Predictor

## Introduction

### 1.1 Problem Statement

Jamboree has helped thousands of students achieve success in top colleges abroad through their unique problem-solving methods for GMAT, GRE, and SAT exams. Recently, they launched a new feature on their website that allows students to check their probability of getting into Ivy League colleges. This feature estimates the chances of graduate admission, providing a valuable tool for students aiming for top-tier education.

### 1.2 Goals and Objectives

The primary goal of this project is to develop a machine learning model that estimates the probability of admission to Ivy League colleges, using data. The project aims to integrate the created model into a web-based tool, allowing students to input their credentials and assess their admission chances.

### 1.3 Importance of the Project

This project is a prototype designed to demonstrate how a predictive model can estimate Ivy League admission probabilities based on various input criteria. If Jamboree approves the model, it may be integrated into their website, providing prospective students with a tool to assess their admission chances. This feature would enhance Jamboree's offerings, helping students make informed decisions and better prepare for their applications.

---
## 2. Project Structure

my_project/ ├── app.py # Main Flask application file ├── Dockerfile # Docker configuration for building and running the app ├── requirements.txt # Python dependencies needed to run the app ├── templates/ # HTML templates for the web pages │ └── index.html # Main HTML template for user input and displaying results ├── static/ # Static files (e.g., CSS, JavaScript) │ └── styles.css # Styling for the web interface ├── models/ # Contains saved models and preprocessing objects │ ├── final_model_with_lor_mean.pkl # Trained model file │ ├── scaler.pkl # Scaler for numerical feature standardization │ └── encoder.pkl # Encoder for categorical data ├── README.md # Documentation file describing the project 

---
## 3. Features
- **Input fields:** Allows users to enter details such as GRE score, TOEFL score, GPA, etc.
- **Prediction:** Provides an estimated probability of admission based on input criteria.
- **User-Friendly Interface:** Interactive and visually appealing UI with input sliders and dynamic feedback.

---

## 4. Installation

### 4.1 Prerequisites

- **Python 3.11.5 or later**
- **pip** (Python package manager)
- **Docker** (optional, for containerization)

### 4.2 **Clone the repository:**

    git clone <repository-url>
    cd ML-Driven-Ivy-League-Admission-Predictor

### 4.3 **Install dependencies:**

    pip install -r requirements.txt

### 4.3 Run the Flask App:

    flask run

---

## 5. Usage

   - After running the Flask app, open a web browser and go to http://localhost:5000.
   - Enter the relevant input values (GRE score, TOEFL score, CGPA and LOR).
   - Click on the "Predict" button to view your estimated probability of admission.

---

## 6. Model Information

This project uses a Linear Regression machine learning model trained to estimate admission probabilities. The model was developed using scikit-learn and saved as final_model_with_lor_mean.pkl. Preprocessing objects, including scaler.pkl and encoder.pkl, are used to standardize and encode input data before making predictions.

--- 

## 7. Future Work

> In the later stages, Docker integration will be fully completed to make deployment smoother. For now, the app can be run using the flask run command. Additional steps to complete Docker integration will be documented here.

---

## 8. License

This project is licensed under the **MIT License**. See LICENSE for more information.

---