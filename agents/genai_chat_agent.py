# agents/genai_chat_agent.py

class ChatAgent:
    def __init__(self, customer_profile):
        self.customer_profile = customer_profile
        self.name = customer_profile.get("Customer_ID", "User")

    def greet_user(self):
        return f"Hi {self.name}, welcome back! What kind of products are you looking for today?"

    def suggest_from_profile(self):
        interests = self.customer_profile.get("Browsing_History", []) + self.customer_profile.get("Purchase_History", [])
        if not interests:
            return "I see you're new here. Would you like help exploring our top categories?"
        interest_summary = ', '.join(set(interests))
        return f"Based on your interests in {interest_summary}, I’ve got some cool recommendations. Want to check them out?"

    def respond_to_query(self, query):
        # A simple rule-based fallback (could be replaced with LLM API integration)
        if "discount" in query.lower():
            return "Looking for discounts? Let me fetch the latest deals for you!"
        elif "recommend" in query.lower():
            return self.suggest_from_profile()
        else:
            return "I'm still learning. Can you be more specific about what you're looking for?"

# Example use
# chat_agent = ChatAgent(customer_profile)
# print(chat_agent.greet_user())
# print(chat_agent.respond_to_query("Can you recommend something?"))
