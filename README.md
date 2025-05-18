# 💬 Customer Support Using Intelligent Chatbot

An intelligent, NLP-powered chatbot built using Streamlit that revolutionizes customer support by automating query responses, visualizing insights, and improving customer satisfaction.

---

## 📌 Project Overview

This project aims to **automate customer support** using a rule-based chatbot integrated into a **Streamlit web application**. It responds to customer queries based on a predefined dataset and visualizes insights like category frequency and sentiment distribution.

### 🔍 Problem Statement

To provide automated assistance to customers through an intelligent chatbot that accurately understands and responds to queries, reducing response times and improving satisfaction.

**Why it Matters**:
- 24/7 availability with instant responses  
- Reduced human workload and operational cost  
- Boosted customer loyalty and business efficiency  

---

## 🎯 Objectives

- Build a query-response chatbot using real support data  
- Identify intent and sentiment of queries  
- Visualize trends using interactive charts  
- Simulate user-chatbot interaction for testing and demonstration  

---

## 📁 Dataset Description

- **Format**: CSV (Structured data)  
- **Fields**:
  - `customer_query`: The question asked by the user  
  - `response`: Chatbot's reply  
  - `category`: The topic type (e.g., Loan, ATM, Account Info)  
  - `sentiment`: Labeled emotion (Positive, Neutral, Negative)  
- **Total Records**: 100+  
- **Type**: Static dataset used for rule-based query matching  

---

## 🛠️ Tools & Technologies

| Component           | Technology Used                     |
|---------------------|--------------------------------------|
| Programming Language | Python                              |
| Interface Framework | Streamlit                            |
| NLP Library         | NLTK (Natural Language Toolkit)      |
| Visualization       | Matplotlib, Seaborn                  |
| Fuzzy Matching      | difflib (for closest query matching) |

---

## 📊 Features

- ✅ **Query Matching**: Uses fuzzy logic to find closest matching query in dataset  
- 📚 **Dataset Viewer**: Displays the first 20 rows of the dataset  
- 📈 **Visualization Tab**:
  - Bar chart of query **categories**  
  - Pie chart of **sentiment distribution**  

---

## 🧪 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nithish-kumar20/customer-support-using-intelligent-chatbot.git
   cd customer-support-using-intelligent-chatbot
