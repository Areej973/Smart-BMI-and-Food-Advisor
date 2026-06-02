# Smart BMI and Food Advisor

<img width="1428" height="741" alt="image" src="https://github.com/user-attachments/assets/2d27067a-cb41-4e80-8090-e9b55594f54c" />

Smart BMI and Food Advisor is a web application built with Streamlit that helps users track their health status, estimate body fat percentage, and receive tailored nutritional advice based on clinical guidelines. The application features a modern, customized health-themed background with adjustable transparency for optimal readability.

## Features

- **Health Analysis:** Calculates Body Mass Index (BMI) and estimates Body Fat Percentage using the scientific Deurenberg formula based on age, gender, weight, and height.
- **RAG-Simulated Food Advice:** Retrieves customized nutritional recommendations from a mock internal clinical knowledge base tailored to the user's weight category.
- **Progress Tracking:** Generates a 1-year interactive line chart showing projected weight progress toward an ideal weight goal.
- **Calorie Calculator:** Displays daily calorie needs tailored to different activity levels (Sedentary, Moderate, and High Activity).
- **Social Sharing:** Integrated custom sharing buttons to quickly post health progress and targets to X (formerly Twitter) and WhatsApp.

## Requirements

The project relies on Python 3.x and the following libraries:
- streamlit
- pandas

Since you have not created a `requirements.txt` file yet, you can set it up by following the installation steps below.

## Installation and Setup

1. **Clone or Download the Project:**
   Ensure your main script file is named `app2.py` and placed in your project directory.

2. **Install Dependencies:**
   Open your terminal inside the project directory and run the following command to install the required packages directly:
   ```bash
   pip install streamlit pandas

#### Optional: If you want to create a requirements.txt file for deployment (e.g., on GitHub or Streamlit Community Cloud), create a new text file named requirements.txt in your project folder and paste the following text into it:
streamlit
pandas

## How to Run the Application

Do not use the standard Python "Play" button in your IDE. Instead, run the app using the Streamlit CLI.

## Open your terminal and execute:
streamlit run app2.py

The application will automatically open in your default web browser at http://localhost:8501.
