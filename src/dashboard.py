import pandas as pd
import streamlit as st
import glob
import os

# Page config
st.set_page_config(
    page_title="Market Basket Analysis",
    page_icon="🛒",
    layout="wide"
)

# Title
st.title("🛒 Market Basket Analysis Dashboard")

st.markdown("""
ระบบวิเคราะห์สินค้าที่ลูกค้ามักซื้อร่วมกัน
ด้วยอัลกอริทึม FP-Growth และ PySpark
""")

# Read association rule files
files = glob.glob(
    "data/3_output/association_rules/*.csv"
)

# Remove empty files
files = [f for f in files if os.path.getsize(f) > 0]

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine data
rules = pd.concat(df_list, ignore_index=True)

# Sort by confidence
rules = rules.sort_values(
    by="confidence",
    ascending=False
)

# Sidebar
st.sidebar.header("⚙️ Filter")

min_conf = st.sidebar.slider(
    "Minimum Confidence",
    0.0,
    1.0,
    0.3
)

filtered_rules = rules[
    rules["confidence"] >= min_conf
]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Rules",
    len(filtered_rules)
)

col2.metric(
    "Highest Confidence",
    round(filtered_rules["confidence"].max(), 2)
)

col3.metric(
    "Average Lift",
    round(filtered_rules["lift"].mean(), 2)
)

st.divider()

# Data table
st.subheader("📋 Association Rules")

st.dataframe(
    filtered_rules[
        [
            "antecedent",
            "consequent",
            "confidence",
            "lift",
            "support"
        ]
    ],
    use_container_width=True
)

st.divider()

# Top combos
st.subheader("🔥 Top Product Combos")

top_rules = filtered_rules.head(10)

for index, row in top_rules.iterrows():

    st.markdown(f"""
    ### 🛍️ Combo #{index+1}

    **If customer buys:**
    - {row['antecedent']}

    **They also tend to buy:**
    - {row['consequent']}

    📈 Confidence: `{round(row['confidence']*100,2)}%`

    🚀 Lift Score: `{round(row['lift'],2)}`
    """)

    st.divider()

# Charts
st.subheader("📊 Visualization")

chart_data = filtered_rules.head(20)

st.bar_chart(
    chart_data.set_index("antecedent")["confidence"]
)

st.line_chart(
    chart_data.set_index("antecedent")["lift"]
)

# Footer
st.markdown("""
---
### 👨‍💻 Technologies Used
- PySpark
- FP-Growth
- Streamlit
- Pandas
- Kaggle Dataset
""")