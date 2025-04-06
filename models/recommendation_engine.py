from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent

class RecommendationEngine:
    def __init__(self, customer_df, product_df):
        self.customers = {
            row["Customer_ID"]: CustomerAgent(row["Customer_ID"], row)
            for _, row in customer_df.iterrows()
        }

        self.products = [
            ProductAgent(row["Product_ID"], row)
            for _, row in product_df.iterrows()
        ]

    def generate_recommendations(self, customer_id, top_n=5):
        if customer_id not in self.customers:
            return []

        customer_agent = self.customers[customer_id]
        interests = customer_agent.get_interests()
        context = customer_agent.get_seasonal_context()
        location = customer_agent.get_location()

        scored_products = []

        for product in self.products:
            score = product.calculate_relevance(interests, context, location)
            if score > 0:
                scored_products.append((product, score))

        scored_products.sort(key=lambda x: x[1], reverse=True)
        top_products = scored_products[:top_n]

        return [product.to_dict() for product, _ in top_products]
