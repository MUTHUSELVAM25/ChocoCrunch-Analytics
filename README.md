# 🍫✨ ChocoCrunch Analytics: Sweet Stats & Sour Truths  

### 🧠 Domain: Nutrition Analytics / Food Tech / Public Health  
**Author:** Muthu Selvam  

---

## 📋 Skills & Tools Gained

- 🐍 Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
- 🔗 API Data Extraction (OpenFoodFacts API)
- 🧹 Data Cleaning & Imputation
- ⚙️ Feature Engineering & Derived Metrics
- 🧮 SQL (MySQL / SQLite / PostgreSQL)
- 📊 Exploratory Data Analysis (EDA)
- 📈 Power BI / Streamlit Dashboards
- 💡 Insight Generation & Presentation

---

## 🎯 Problem Statement

As a Data Analyst at a nutrition research firm, your mission is to analyze the **global chocolate market**.  
The goal is to:
1. Extract chocolate product data from the OpenFoodFacts API  
2. Clean, transform, and engineer features  
3. Store the data in an SQL database  
4. Perform EDA and derive insights  
5. Build interactive dashboards (Power BI / Streamlit)

---

## 💼 Business Use Cases

- Identify **calorie and sugar-heavy** chocolate products  
- Track **ultra-processed chocolate** trends via NOVA classification  
- Compare **brand-wise healthiness** based on sugar & calories  
- Categorize chocolates into **health-based classes**  
- Provide **interactive reports** for stakeholders  

---

## 🧩 Project Workflow

### 📥 Step 1: Dataset Collection
- Extracted 12,000+ chocolate product records using the [OpenFoodFacts API](https://world.openfoodfacts.org/api/v2/search?categories=chocolates)
- Key columns:  
  `product_code`, `product_name`, `brand`, `nutriments`

---

### 🧹 Step 2: Data Cleaning & Exploration
- Identified and handled missing values  
- Dropped columns with excessive nulls  
- Imputed missing data appropriately  

---

### ⚙️ Step 3: Feature Engineering
Created new derived metrics:

| Feature | Description |
|----------|--------------|
| `sugar_to_carb_ratio` | Ratio of sugar to total carbohydrates |
| `calorie_category` | Classified as *Low*, *Moderate*, *High* calorie |
| `sugar_category` | Classified as *Low*, *Moderate*, *High* sugar |
| `is_ultra_processed` | Flag for NOVA group = 4 |

---

### 🧮 Step 4: Exploratory Data Analysis (EDA)
Explored nutritional characteristics using Python:

- Distribution of energy (kcal), sugar, and carbohydrate levels  
- Correlation between sugar and calorie content  
- Brand-wise comparison of average calories  
- Relationship between **NOVA group** and **energy values**  

#### 📊 Visualization Highlights:
- Bar charts: Calorie & sugar category distributions  
- Pie charts: NOVA group proportions  
- Heatmaps: Nutrient correlations  
- Boxplots: Brand-wise sugar & calorie spread  
- Scatter plots: Calories vs Sugars  

---

### 🗃️ Step 5: SQL Database Design

**Tables:**
1. `product_info` → product details  
2. `nutrient_info` → nutritional data  
3. `derived_metrics` → engineered features  

**Integration:**
- Connected Python → SQL using `sqlite3` / `mysql.connector`  
- Populated tables with cleaned data  

---

### 🧠 Step 6: SQL Analysis

#### 🔢 Sample Queries:
- Top 10 brands by average calorie value  
- Count of ultra-processed vs minimally processed products  
- High sugar + high calorie product combinations  
- Average sugar-to-carb ratio per calorie category  
- Top 5 products by sugar_to_carb_ratio  

---

### 📈 Step 7: Visualization Dashboard

**Option 1: Power BI Dashboard**
- 20+ visualizations combining SQL & custom insights  
- Slicers and filters for interactive exploration  

**Option 2: Streamlit App**
- Displayed all 27 SQL query outputs  
- Integrated Python-based EDA visuals  

---

## 💡 Insights & Recommendations

- Ultra-processed chocolates (NOVA 4) have **40–60% higher average calories**  
- Certain brands consistently fall in **High Calorie + High Sugar** categories  
- **Sugar-to-Carb ratio** serves as a strong indicator of over-processed chocolates  
- Consumers can use these insights for **health-conscious product choices**  

---

## 🧰 Technical Stack

| Category | Tools Used |
|-----------|-------------|
| Language | Python |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Plotly |
| Database | MySQL / SQLite |
| Visualization | Power BI / Streamlit |
| APIs | OpenFoodFacts API |

---

## 🧾 Expected Deliverables

- 3 structured SQL tables  
- 27 SQL queries (analytical & join-based)  
- 7–12 Python EDA visualizations  
- 10–20 Power BI dashboard visuals or Streamlit app  
- Final insight summary  

---

## 📎 References
- [OpenFoodFacts API Documentation](https://world.openfoodfacts.org/data)  
- [Streamlit Docs](https://docs.streamlit.io/develop/api-reference)  
- [Power BI Tutorials](https://learn.microsoft.com/en-us/power-bi/)  

---

## 🚀 Project Outcome

A **data-driven chocolate nutrition analytics platform** that blends  
API integration, SQL, Python, and dashboard visualization — empowering  
researchers and consumers to uncover the **sweet truth behind every bite 🍫**  

---

### 🏷️ Tags
`Python` `SQL` `API` `EDA` `Feature Engineering` `Power BI` `Streamlit` `Public Health` `Food Analytics` `Data Science`











