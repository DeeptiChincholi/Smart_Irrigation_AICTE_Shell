# Smart_Irrigation_AICTE_Shell
A Machine Learning-based irrigation control system that predicts the ON/OFF status of 3 sprinklers using real-time sensor input from agricultural land parcels.

🔍 Problem Statement
Efficient water management in agriculture requires automated, intelligent irrigation based on real-time environmental data. This system predicts which sprinklers should be ON/OFF using sensor values.

✅ Solution
Predicts sprinkler status using 20 sensor inputs (scaled 0–1).

Uses a Random Forest model wrapped in MultiOutputClassifier.

Deployed with Streamlit for an interactive web interface.

🛠️ Tech Stack
Language: Python 3.12.8

IDE: Visual Studio Code

Libraries: pandas, numpy, scikit-learn, joblib, streamlit

Algorithm: Random Forest Classifier (multi-output)

🚀 Features
Takes 20 scaled sensor inputs via sliders

Predicts ON/OFF status of 3 sprinklers instantly

User-friendly web interface with real-time feedback

📦 How to Run
Clone the repo

Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py

🧠 Project By
Deepti Chincholi

