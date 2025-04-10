from utils.data_loader import load_customer_data, load_product_data
from models.recommendation_engine import RecommendationEngine
from agents.customer_agent import CustomerAgent
from agents.explainability_agent import ExplainabilityAgent

def main():
    # Load data from CSVs
    customer_df = load_customer_data("data/customer_data_collection.csv")
    product_df = load_product_data("data/product_recommendation_Data.csv")

    # Initialize recommendation engine
    recommender = RecommendationEngine(customer_df, product_df)

    # Loop through each customer
    for _, row in customer_df.iterrows():
        customer_id = row["Customer_ID"]
        print(f"\n🛍️ Recommendations for customer {customer_id}:")

        # Create a customer agent instance
        customer_profile = row.to_dict()
        customer_agent = CustomerAgent(customer_id, customer_profile)

        # Generate top N product recommendations
        recommendations = recommender.generate_recommendations(customer_id, top_n=5)

        # Format product names for explainability agent
        recommended_items = [f"{r['Category']} > {r['Subcategory']}" for r in recommendations]

        # Generate explanations
        explainer = ExplainabilityAgent(customer_agent, recommended_items)
        explanations = explainer.generate_explanations()

        # Print recommendations with explanations
        for rec, reason in zip(recommended_items, explanations):
            print(f"- {rec} → {reason}")

if __name__ == "__main__":
    main()
