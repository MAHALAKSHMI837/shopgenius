from utils.data_loader import load_customer_data, load_product_data
from models.recommendation_engine import RecommendationEngine

def main():
    # Load data from CSVs
    customer_df = load_customer_data("data/customer_data_collection.csv")
    product_df = load_product_data("data/product_recommendation_Data.csv")

    # Initialize recommendation engine
    recommender = RecommendationEngine(customer_df, product_df)

    # Loop through each customer
    for customer_id in customer_df["Customer_ID"]:
        print(f"\nRecommendations for customer {customer_id}:")
        recommendations = recommender.generate_recommendations(customer_id, top_n=5)

        for rec in recommendations:
            print(f"- {rec['Category']} > {rec['Subcategory']}")

if __name__ == "__main__":
    main()
