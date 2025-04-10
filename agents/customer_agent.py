class CustomerAgent:
    def __init__(self, customer_id, profile):
        self.customer_id = customer_id
        self.profile = profile
        self.history = {
            "browsing": eval(profile.get("Browsing_History", "[]")),
            "purchases": eval(profile.get("Purchase_History", "[]"))
        }

    def get_interests(self):
        return set(self.history["browsing"] + self.history["purchases"])

    def get_segment(self):
        return self.profile.get("Customer_Segment", "Unknown")

    def get_location(self):
        return self.profile.get("Location", "Unknown")

    def get_seasonal_context(self):
        return {
            "Holiday": self.profile.get("Holiday", "No"),
            "Season": self.profile.get("Season", "All")
        }

    def get_age(self):
        return self.profile.get("Age", None)

    def get_gender(self):
        return self.profile.get("Gender", "Unknown")


class CustomerAgentManager:
    def __init__(self, customer_df):
        self.customers = {
            row["Customer_ID"]: CustomerAgent(row["Customer_ID"], row)
            for _, row in customer_df.iterrows()
        }

    def get_customer_by_id(self, customer_id):
        return self.customers.get(customer_id)
