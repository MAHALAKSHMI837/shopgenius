import streamlit as st
from agents.customer_agent import CustomerAgentManager
from agents.explainability_agent import ExplainabilityAgent
from models.recommendation_engine import RecommendationEngine
from utils.data_loader import load_data

# Load customer and product data
customers_df, products_df = load_data()

# Title
st.set_page_config(page_title="🛍️ Personalized Recommender", layout="wide")
st.title("🛍️ GenAI-Powered E-commerce Recommender")

# Instantiate CustomerAgentManager
customer_manager = CustomerAgentManager(customers_df)

# Customer selection
customer_id = st.selectbox("Select Customer ID", customers_df["Customer_ID"].unique())

# Get CustomerAgent
customer_agent = customer_manager.get_customer_by_id(customer_id)

# Generate recommendations
engine = RecommendationEngine(customers_df, products_df)
recommended_items = engine.generate_recommendations(customer_id)

# Display recommendations
st.subheader("🔮 Recommended Products")
for item in recommended_items:
    st.markdown(f"- **{item}**")

# Explain recommendations
explainer = ExplainabilityAgent(customer_agent, recommended_items)
explanations = explainer.generate_explanations()

st.subheader("🧠 Why These Were Recommended")
for explanation in explanations:
    st.write(f"- {explanation}")
