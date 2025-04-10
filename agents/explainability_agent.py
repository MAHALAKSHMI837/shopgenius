# # # agents/explainability_agent.py

# # class ExplainabilityAgent:
# #     def __init__(self, customer_agent, recommended_items):
# #         self.customer_agent = customer_agent
# #         self.recommended_items = recommended_items

# #     def generate_explanations(self):
# #         explanations = []
# #         interests = self.customer_agent.get_interests()
# #         segment = self.customer_agent.get_segment()
# #         location = self.customer_agent.get_location()
# #         seasonal = self.customer_agent.get_seasonal_context()

# #         for item in self.recommended_items:
# #             explanation = self._explain_single_item(item, interests, segment, location, seasonal)
# #             explanations.append(explanation)

# #         return explanations

# #     def explain(self, customer_id, product):
# #         # Direct explanation for a single product
# #         interests = self.customer_agent.get_interests()
# #         segment = self.customer_agent.get_segment()
# #         location = self.customer_agent.get_location()
# #         seasonal = self.customer_agent.get_seasonal_context()

# #         return self._explain_single_item(product, interests, segment, location, seasonal)

# #     def _explain_single_item(self, item, interests, segment, location, seasonal):
# #         reasons = []

# #         if item in interests:
# #             reasons.append("based on your browsing and purchase history")

# #         if "Winter" in seasonal.get("Season", "") and "Jackets" in item:
# #             reasons.append("it's a seasonal favorite for winter")

# #         if segment == "Premium" and "Luxury" in item:
# #             reasons.append("tailored for premium customers like you")

# #         if location and "Local" in item:
# #             reasons.append("trending in your region")

# #         explanation = f"{item} was recommended " + (
# #             " and ".join(reasons) if reasons else "based on general popularity"
# #         )
# #         return explanation

# # agents/explainability_agent.py

# class ExplainabilityAgent:
#     def __init__(self, customer_agent, recommended_items):
#         self.customer_agent = customer_agent
#         self.recommended_items = recommended_items

#     def generate_explanations(self):
#         explanations = []
#         interests = self.customer_agent.get_interests()
#         segment = self.customer_agent.get_segment()
#         location = self.customer_agent.get_location()
#         seasonal = self.customer_agent.get_seasonal_context()

#         for item in self.recommended_items:
#             explanation = self._explain_single_item(item, interests, segment, location, seasonal)
#             explanations.append(explanation)

#         return explanations

#     def explain(self, customer_id, product):
#         interests = self.customer_agent.get_interests()
#         segment = self.customer_agent.get_segment()
#         location = self.customer_agent.get_location()
#         seasonal = self.customer_agent.get_seasonal_context()

#         return self._explain_single_item(product, interests, segment, location, seasonal)

#     # def _explain_single_item(self, item, interests, segment, location, seasonal):
#     #     reasons = []

#     #     # Normalize fields
#     #     category = item.get("Category", "").lower()
#     #     subcategory = item.get("Subcategory", "").lower()
#     #     item_tags = f"{category} {subcategory}"

#     #     # Check interest match
#     #     if any(interest.lower() in item_tags for interest in interests):
#     #         reasons.append("based on your browsing and purchase history")

#     #     # Check seasonal match
#     #     if "winter" in seasonal.get("Season", "").lower() and "jacket" in subcategory:
#     #         reasons.append("it's a seasonal favorite for winter")

#     #     # Check segment-based match
#     #     if segment.lower() == "premium" and "luxury" in category:
#     #         reasons.append("tailored for premium customers like you")

#     #     # Check location match (if the item has location metadata)
#     #     available_locations = item.get("Available_Locations", "")
#     #     if location.lower() in available_locations.lower():
#     #         reasons.append("trending in your region")

#     #     product_name = item.get("Product_Name", "This product")

#     #     # Combine explanation
#     #     explanation = f"**{product_name}** was recommended " + (
#     #         " because " + " and ".join(reasons) if reasons else "based on general popularity"
#     #     )

#     #     return explanation

# def _explain_single_item(self, item, interests, segment, location, seasonal):
#     reasons = []
#     product_name = item.get("Product_Name", "This product")

#     # Check conditions and append reasons
#     if item.get("Category") in interests or item.get("Subcategory") in interests:
#         reasons.append("based on your browsing and purchase history")

#     if "Winter" in seasonal.get("Season", "") and "Jacket" in product_name:
#         reasons.append("it's a seasonal favorite for winter")

#     if segment == "Premium" and "Luxury" in product_name:
#         reasons.append("tailored for premium customers like you")

#     if location and "Local" in product_name:
#         reasons.append("it's trending in your region")

#     # Combine explanation
#     if reasons:
#         explanation = f"**{product_name}** was recommended because " + " and ".join(reasons)
#     else:
#         explanation = f"**{product_name}** was recommended based on general popularity"

#     return explanation

class ExplainabilityAgent:
    def __init__(self, customer_agent, recommended_items):
        self.customer_agent = customer_agent
        self.recommended_items = recommended_items

    def generate_explanations(self):
        explanations = []
        interests = self.customer_agent.get_interests()
        segment = self.customer_agent.get_segment()
        location = self.customer_agent.get_location()
        seasonal = self.customer_agent.get_seasonal_context()

        for item in self.recommended_items:
            explanation = self._explain_single_item(item, interests, segment, location, seasonal)
            explanations.append(explanation)

        return explanations

    def explain(self, customer_id, product):
        interests = self.customer_agent.get_interests()
        segment = self.customer_agent.get_segment()
        location = self.customer_agent.get_location()
        seasonal = self.customer_agent.get_seasonal_context()

        return self._explain_single_item(product, interests, segment, location, seasonal)

    # ✅ Ensure this method is not indented inside another function!
    def _explain_single_item(self, item, interests, segment, location, seasonal):
        reasons = []
        product_name = item.get("Product_Name", "This product")

        if item.get("Category") in interests or item.get("Subcategory") in interests:
            reasons.append("based on your browsing and purchase history")

        if "Winter" in seasonal.get("Season", "") and "Jacket" in product_name:
            reasons.append("it's a seasonal favorite for winter")

        if segment == "Premium" and "Luxury" in product_name:
            reasons.append("tailored for premium customers like you")

        if location and "Local" in product_name:
            reasons.append("it's trending in your region")

        if reasons:
            explanation = f"**{product_name}** was recommended because " + " and ".join(reasons)
        else:
            explanation = f"**{product_name}** was recommended based on general popularity"

        return explanation
