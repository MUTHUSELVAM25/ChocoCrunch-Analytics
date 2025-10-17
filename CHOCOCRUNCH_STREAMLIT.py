import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import squarify


# --- Database connection ---
def get_connection():
    return mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        port=4000,
        user='EnD345nfx9wxmnG.root',
        password='Q4KKSkNgKxF3JIPn',
        database='choco_crunch'
    )

# Run SQL query and return dataframe
def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    cols = cursor.column_names
    rows = cursor.fetchall()
    cursor.close()
    return pd.DataFrame(rows, columns=cols)

# Queries dictionary
QUERIES = {
    "Count products per brand": "SELECT brand, COUNT(*) AS count FROM product_info GROUP BY brand ORDER BY count DESC;",
    "Unique products per brand": "SELECT brand, COUNT(DISTINCT product_code) FROM product_info GROUP BY brand ORDER BY 1;",
    "Top 5 brands by product count": "SELECT brand, COUNT(*) AS count FROM product_info GROUP BY brand ORDER BY count DESC LIMIT 5;",
    "Products with missing product name": "SELECT * FROM product_info WHERE product_name IS NULL OR product_name = '';",
    "Unique brands": "SELECT COUNT(DISTINCT brand) FROM product_info;",
    "Products with code starting with '3'": "SELECT * FROM product_info WHERE product_code LIKE '3%';",

    "Top 10 highest calorie products": "SELECT product_code, energy_kcal_value FROM nutrient_info ORDER BY energy_kcal_value DESC LIMIT 10;",
    "Average sugars per nova-group": "SELECT nova_group, AVG(sugars_value) FROM nutrient_info GROUP BY nova_group;",
    "Count with fat_value > 20g": "SELECT COUNT(*) FROM nutrient_info WHERE fat_value > 20;",
    "Average carbohydrates_value": "SELECT AVG(carbohydrates_value) FROM nutrient_info;",
    "Products with sodium_value > 1g": "SELECT product_code FROM nutrient_info WHERE sodium_value > 1;",
    "Count products with fruits/vegetables/nuts": "SELECT COUNT(*) FROM nutrient_info WHERE fruits_vegetables_nuts_estimate_from_ingredients_100g > 0;",
    "Products with energy-kcal_value > 500": "SELECT product_code FROM nutrient_info WHERE energy_kcal_value > 500;",

    "Count per calorie_category": "SELECT calorie_category, COUNT(*) FROM derived_metrics GROUP BY calorie_category;",
    "Count of High Sugar products": "SELECT COUNT(*) FROM derived_metrics WHERE sugar_category = 'High Sugar';",
    "Average sugar_to_carb_ratio for High Calorie": "SELECT AVG(sugar_to_carb_ratio) FROM derived_metrics WHERE calorie_category = 'High';",
    "Products both High Calorie and High Sugar": "SELECT * FROM derived_metrics WHERE calorie_category = 'High' AND sugar_category = 'High Sugar';",
    "Count of ultra-processed products": "SELECT COUNT(*) FROM derived_metrics WHERE is_ultra_processed = 'Yes';",

    "Top 5 brands with most High Calorie products": """
        SELECT p.brand, COUNT(*) FROM product_info p
        JOIN derived_metrics d ON p.product_code = d.product_code
        WHERE d.calorie_category = 'High'
        GROUP BY p.brand ORDER BY COUNT(*) DESC LIMIT 5;""",

    "Average energy_kcal_value per calorie_category": """
        SELECT d.calorie_category, AVG(n.energy_kcal_value)
        FROM derived_metrics d
        JOIN nutrient_info n ON d.product_code = n.product_code
        GROUP BY d.calorie_category;""",

    "Count ultra-processed per brand": """
        SELECT p.brand, COUNT(*)
        FROM product_info p
        JOIN derived_metrics d ON p.product_code = d.product_code
        WHERE d.is_ultra_processed = 'Yes'
        GROUP BY p.brand;""",

    "Products with High Sugar and High Calorie": """
        SELECT p.brand, p.product_code
        FROM product_info p
        JOIN derived_metrics d ON p.product_code = d.product_code
        WHERE d.calorie_category = 'High' AND d.sugar_category = 'High Sugar';""",

    "Average sugars per brand for ultra-processed": """
        SELECT p.brand, AVG(n.sugars_value)
        FROM product_info p
        JOIN derived_metrics d ON p.product_code = d.product_code
        JOIN nutrient_info n ON p.product_code = n.product_code
        WHERE d.is_ultra_processed = 'Yes'
        GROUP BY p.brand;""",

    "Number with fruits/veggies/nuts per calorie_category": """
        SELECT d.calorie_category, COUNT(*)
        FROM derived_metrics d
        JOIN nutrient_info n ON d.product_code = n.product_code
        WHERE n.fruits_vegetables_nuts_estimate_from_ingredients_100g > 0
        GROUP BY d.calorie_category;""",

    "Top 5 products by sugar_to_carb_ratio": """
        SELECT p.product_code, d.sugar_to_carb_ratio, d.calorie_category, d.sugar_category
        FROM product_info p
        JOIN derived_metrics d ON p.product_code = d.product_code
        ORDER BY d.sugar_to_carb_ratio DESC LIMIT 5;"""
}

# Streamlit app start
st.set_page_config(page_title="ChocoCrunch Analytics Dashboard", layout="wide")
st.title("ChocoCrunch Chocolate Nutrition Dashboard 🍫")

conn = get_connection()

# Sidebar Filters
st.sidebar.header("Filters")
calorie_opts = ['Low', 'Moderate', 'High']
selected_calories = st.sidebar.multiselect("Select Calorie Category", calorie_opts, default=calorie_opts)
sugar_opts = ['Low Sugar', 'Moderate Sugar', 'High Sugar']
selected_sugars = st.sidebar.multiselect("Select Sugar Category", sugar_opts, default=sugar_opts)
selected_ultra = st.sidebar.multiselect("Ultra-Processed?", ['Yes', 'No'], default=['Yes', 'No'])

# Main data query
query_main = """
SELECT p.product_code, p.product_name, p.brand,
       n.energy_kcal_value, n.sugars_value, n.carbohydrates_value, 
       d.sugar_to_carb_ratio, d.calorie_category, d.sugar_category, d.is_ultra_processed,
       n.nova_group, n.fruits_vegetables_nuts_estimate_from_ingredients_100g
FROM product_info p
JOIN nutrient_info n ON p.product_code = n.product_code
JOIN derived_metrics d ON p.product_code = d.product_code;
"""
df = run_query(conn, query_main)

# Apply filters
df_filtered = df[
    (df['calorie_category'].isin(selected_calories)) &
    (df['sugar_category'].isin(selected_sugars)) &
    (df['is_ultra_processed'].isin(selected_ultra))
]

st.markdown(f"### Showing {len(df_filtered)} products after filters")
st.dataframe(df_filtered)

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Average Calories", f"{df_filtered['energy_kcal_value'].mean():.1f}")
col2.metric("Average Sugars", f"{df_filtered['sugars_value'].mean():.1f}")
col3.metric("Ultra-Processed Count", int(df_filtered['is_ultra_processed'].value_counts().get('Yes', 0)))

# Visualizations
# 1. Bar chart: Number of products in each calorie_category
fig, ax = plt.subplots()
sns.countplot(data=df_filtered, x='calorie_category', order=calorie_opts, palette='ch:s=.25,rot=-.25', ax=ax)
ax.set_title("Number of Products by Calorie Category")
st.pyplot(fig)

# 2. Pie chart: Distribution of products by nova-group
nova_counts = df_filtered['nova_group'].value_counts().sort_index()
fig2, ax2 = plt.subplots()
ax2.pie(nova_counts, labels=nova_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
ax2.set_title("Product Distribution by NOVA Group")
st.pyplot(fig2)

# 3. Bar chart: Top 10 brands by average energy-kcal_value
top_brands = df_filtered['brand'].value_counts().nlargest(10).index
df_top_brands = df_filtered[df_filtered['brand'].isin(top_brands)]
fig3, ax3 = plt.subplots(figsize=(10,5))
sns.barplot(data=df_top_brands, x='brand', y='energy_kcal_value', estimator='mean', palette='deep', ax=ax3)
ax3.set_title("Top 10 Brands by Average Calories")
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)

# 4. Scatter plot: Calories vs Sugar content colored by ultra_processed
fig4, ax4 = plt.subplots(figsize=(10,6))
palette = {'Yes':'red','No':'green'}
sns.scatterplot(data=df_filtered, x='energy_kcal_value', y='sugars_value', hue='is_ultra_processed', palette=palette, alpha=0.6, ax=ax4)
ax4.set_title("Calories vs Sugars by Ultra-Processed Flag")
ax4.set_xlabel("Calories per 100g")
ax4.set_ylabel("Sugars per 100g")
st.pyplot(fig4)

# 5. Boxplot: sugar_to_carb_ratio distribution across brands (top 10 brands)
fig5, ax5 = plt.subplots(figsize=(12,6))
sns.boxplot(data=df_top_brands, x='brand', y='sugar_to_carb_ratio', ax=ax5)
ax5.tick_params(axis='x', rotation=45)
ax5.set_title("Sugar to Carb Ratio Distribution Across Top Brands")
st.pyplot(fig5)

# 6. Treemap: Product count by brand and calorie_category 
brand_cat_counts = df_filtered.groupby(['brand','calorie_category']).size().reset_index(name='count')
brand_cat_counts_top = brand_cat_counts[brand_cat_counts['brand'].isin(top_brands)]
labels = brand_cat_counts_top.apply(lambda x: f"{x['brand']}\n({x['calorie_category']})\nCount: {x['count']}", axis=1)
sizes = brand_cat_counts_top['count']

fig6, ax6 = plt.subplots(figsize=(12,7))
squarify.plot(sizes=sizes, label=labels, alpha=0.7, ax=ax6)
ax6.axis('off')
ax6.set_title("Treemap: Product Count by Brand and Calorie Category")
st.pyplot(fig6)

# 7. Heatmap: Correlation between calories, sugars, and carbohydrates
fig7, ax7 = plt.subplots()
corr = df_filtered[['energy_kcal_value','sugars_value','carbohydrates_value']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax7)
ax7.set_title("Correlation Heatmap: Calories, Sugars, Carbohydrates")
st.pyplot(fig7)

# 8. Bar chart: Number of High Sugar products per brand
high_sugar_counts = df_filtered[df_filtered['sugar_category'] == 'High Sugar']['brand'].value_counts().nlargest(10)
fig8, ax8 = plt.subplots(figsize=(10,5))
sns.barplot(x=high_sugar_counts.index, y=high_sugar_counts.values, palette='dark:#5A9_r', ax=ax8)
ax8.set_title("Number of High Sugar Products Per Brand")
ax8.tick_params(axis='x', rotation=45)
ax8.set_ylabel("Product Count")
st.pyplot(fig8)

# 9. Stacked bar: Count of ultra-processed vs minimally processed products per brand
up_counts = df_filtered.groupby(['brand','is_ultra_processed']).size().unstack(fill_value=0).loc[top_brands]
fig9, ax9 = plt.subplots(figsize=(12,6))
up_counts.plot(kind='bar', stacked=True, color=['#8B4513','#D2691E'], ax=ax9)
ax9.set_title("Ultra-Processed vs Minimally Processed Products by Brand")
ax9.set_ylabel("Product Count")
ax9.legend(title='Ultra Processed')
ax9.tick_params(axis='x', rotation=45)
st.pyplot(fig9)

# 10. Show all SQL query results
st.header("All SQL Query Results")
for desc, sql in QUERIES.items():
    st.subheader(desc)
    df_query = run_query(conn, sql)
    st.dataframe(df_query)

conn.close()

