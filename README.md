ChocoCrunch Analytics
Introduction
ChocoCrunch Analytics analyzes the global chocolate market nutrition data using the OpenFoodFacts API. The project pipeline includes data extraction, cleaning, feature engineering, SQL database management, exploratory data analysis, and visualization dashboard development.

Features
Extract up to 12,000 chocolate product records via API

Clean and impute missing data

Derived nutrition metrics (e.g., sugar-to-carb ratio, calorie categories)

Store data in SQL tables (product info, nutrient info, derived metrics)

Perform EDA with Python visualization libraries (matplotlib, seaborn)

Develop interactive Power BI and Streamlit dashboards

Generate SQL queries for insights across brands and nutrition categories

Getting Started
Prerequisites
Python 3.x

SQL Database (MySQL, PostgreSQL, or SQLite)

Power BI Desktop (optional, for dashboard)

Streamlit (optional, for interactive web app)

Installation
bash
git clone https://github.com/yourusername/ChocoCrunch-Analytics.git
cd ChocoCrunch-Analytics
pip install -r requirements.txt
Usage
Run the extract_data.py script to fetch raw data from OpenFoodFacts API.

Use clean_data.py for data cleaning and imputation.

Execute feature_engineering.py to create derived features.

Load cleaned data into your SQL database using load_to_sql.py.

Run SQL queries via provided scripts or connect with Power BI/Streamlit for visualization.

Launch the Streamlit app with:

bash
streamlit run dashboards/Streamlit/app.py
Project Structure
Brief on the folders and key scripts for navigation.

Key Insights
Summarize notable findings from the exploratory analysis and SQL queries.

Authors and Acknowledgments
Created by: MUTHU SELVAM

Verified and guided by: GUVI HCL mentors

License
Specify the license under which the project is shared.










