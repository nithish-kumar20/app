import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from difflib import get_close_matches

# Title
st.title("💬 Banking Customer Support Chatbot")
st.write("This chatbot uses a dataset to answer customer queries and provides insight into query data.")

# Load CSV
@st.cache_data
def load_data():
    return pd.read_csv("banking_customer_support_chatbot_dataset.csv")

df = load_data()

# Sidebar - Navigation
st.sidebar.header("📊 Data Explorer")
page = st.sidebar.radio("Go to", ["Chatbot", "Dataset Overview", "Visualizations"])

# --- CHATBOT PAGE ---
if page == "Chatbot":
    st.header("🤖 Chatbot Assistant")

    user_query = st.text_input("Ask your question:", "")

    def get_response(query):
        all_queries = df['customer_query'].unique().tolist()
        match = get_close_matches(query, all_queries, n=1, cutoff=0.6)
        if match:
            matched_row = df[df['customer_query'] == match[0]].iloc[0]
            return {
                "response": matched_row['response'],
                "category": matched_row['category'],
                "sentiment": matched_row['sentiment']
            }
        else:
            return {"response": "I'm sorry, I couldn't understand that. Please rephrase your question.",
                    "category": "Unknown", "sentiment": "Neutral"}

    if user_query:
        result = get_response(user_query)
        st.markdown(f"**Response:** {result['response']}")
        st.markdown(f"**Category:** {result['category']}")
        st.markdown(f"**Sentiment:** {result['sentiment']}")

# --- DATASET PAGE ---
elif page == "Dataset Overview":
    st.header("📄 Dataset Preview")
    st.dataframe(df.head(20))
    st.markdown(f"**Total records:** {df.shape[0]}")
    st.markdown(f"**Unique Categories:** {df['category'].nunique()}")

# --- VISUALIZATION PAGE ---
elif page == "Visualizations":
    st.header("📊 Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Category Distribution")
        category_counts = df['category'].value_counts()
        fig, ax = plt.subplots()
        sns.barplot(y=category_counts.index, x=category_counts.values, ax=ax)
        ax.set_xlabel("Number of Queries")
        ax.set_ylabel("Category")
        st.pyplot(fig)

    with col2:
        st.subheader("Sentiment Distribution")
        sentiment_counts = df['sentiment'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=140)
        ax2.axis("equal")
        st.pyplot(fig2)
