# 📊 CORD-19 Data Explorer

This project is a beginner-friendly data analysis and visualization of the **CORD-19 research dataset** (metadata.csv), focused on exploring COVID-19 research publications.  
It also includes a **Streamlit web app** for interactive data exploration.

---

## 📌 Project Overview
The goal of this project is to:
- Practice loading and exploring a real-world dataset.
- Perform basic data cleaning and preparation.
- Create meaningful visualizations of research trends.
- Build an interactive web app with Streamlit to share insights.

---

## 📂 Dataset Information
We use the `metadata.csv` file from the [CORD-19 dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), which contains:

- Paper titles and abstracts  
- Publication dates  
- Authors and journals  
- Source information  

Only a sample or cleaned version of the dataset is included here to make analysis lightweight.

---

## 🛠️ Tools and Libraries
- **Python 3.7+**
- **pandas** – data loading and cleaning  
- **matplotlib** & **seaborn** – visualizations  
- **wordcloud** – generate word clouds  
- **Streamlit** – build interactive web application  

Install dependencies with:
```bash
pip install -r requirements.txt
📊 Analysis & Findings
Key Insights:
Publication Trends: COVID-19 research papers increased dramatically in 2020.

Top Journals: The dataset shows which journals published the most COVID-related research.

Word Cloud: Most frequent words in paper titles include COVID-19, SARS-CoV-2, pandemic, etc.

Sample Visualizations:
Publications per year (bar chart)

Top 10 publishing journals (bar chart)

Word cloud of research titles

🌐 Streamlit Web App
The Streamlit app provides:

A year range slider to filter papers

A preview table of paper titles, journals, and dates

Interactive visualizations (bar charts + word cloud)

Run the app locally:

bash
Copy code
streamlit run app.py
📁 Project Structure
bash
Copy code
Frameworks_Assignment/
│
├── metadata.csv             # Original dataset (or sample)
├── cleaned_metadata.csv     # Cleaned and prepared dataset
├── analysis.ipynb           # Jupyter notebook with analysis
├── app.py                   # Streamlit web application
├── requirements.txt         # Project dependencies
└── README.md                # This file
🧠 Reflection
This project helped me:

Practice real-world data cleaning techniques (handling missing values, date parsing).

Build visualizations to communicate patterns effectively.

Learn how to make a simple Streamlit app for interactive exploration.

Challenges included dealing with missing data and large dataset size.
By focusing on the metadata.csv file and using a cleaned sample, I was able to work efficiently and complete the assignment.

📜 License
This project is for educational purposes as part of a data analysis assignment.

yaml
Copy code

---

Would you like me to also generate a **`requirements.txt`** file for you, so anyone cloning your repo 
