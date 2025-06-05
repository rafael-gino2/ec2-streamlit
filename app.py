import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Análise Financeira - Microsoft Financial Sample")

@st.cache_data
@st.cache_data
def load_data():
    df = pd.read_csv("MS_Financial Sample.csv", sep=";")
    
    df.columns = df.columns.str.strip()
    num_cols = ["Units Sold", "Manufacturing Price", "Sale Price", "Gross Sales",
                "Discounts", "Sales", "COGS", "Profit"]
    
    for col in num_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .str.replace("$", "", regex=False)
            .str.strip()
            .replace("-", None)  
            .pipe(pd.to_numeric, errors='coerce') 
        )
    
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    return df


df = load_data()

# Filtros
st.sidebar.header("Filtros")
years = st.sidebar.multiselect("Ano", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
countries = st.sidebar.multiselect("País", sorted(df["Country"].unique()), default=sorted(df["Country"].unique()))

filtered_df = df[(df["Year"].isin(years)) & (df["Country"].isin(countries))]

# Grafico de "Vendas por País"
st.subheader("Vendas Totais por País")
sales_by_country = (
    filtered_df.groupby("Country")["Sales"].sum().sort_values(ascending=False)
)

fig1, ax1 = plt.subplots()
sns.barplot(x=sales_by_country.values, y=sales_by_country.index, ax=ax1)
ax1.set_xlabel("Vendas")
st.pyplot(fig1)
