class ProductAgent:
    def __init__(self, product_id, profile):
        self.product_id = product_id
        self.profile = profile

    def calculate_relevance(self, interests, context, location):
        score = 0

        if self.profile["Subcategory"] in interests or self.profile["Category"] in interests:
            score += 1

        if self.profile["Holiday"] == context.get("Holiday"):
            score += 0.5

        if self.profile["Season"] == context.get("Season"):
            score += 0.5

        if self.profile["Geographical_Location"] == location:
            score += 0.5

        score += float(self.profile.get("Probability_of_Recommendation", 0))

        return score

    def to_dict(self):
        return {
            "Product_ID": self.product_id,
            "Category": self.profile.get("Category", ""),
            "Subcategory": self.profile.get("Subcategory", ""),
            "Brand": self.profile.get("Brand", ""),
            "Price": self.profile.get("Price")  

        }
