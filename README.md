🛒 E-Commerce GenAI-Powered Recommender System
An AI-driven personalized shopping experience platform that uses intelligent agents to recommend products, explain recommendations, and adapt to user behavior based on interests, location, seasonality, and customer segment.

📌 Features
✅ Customer Profiling Agent – Understands user interests, location, segment (e.g., Premium), and seasonal context.
✅ Product Agent – Scores and ranks product relevance per user.
✅ Recommendation Engine – Ranks top-N products using intelligent matching.
✅ Explainability Agent – Offers human-readable reasoning for each recommendation.
✅ Streamlit Dashboard – Simple and interactive UI for users to select their ID and view recommendations with explanations.
✅ Expandable AI Capabilities – Designed to support GenAI chat, promo agents, feedback loops, and more.

🧠 How It Works
Load customer and product datasets.

For each customer:
Generate top product recommendations.
Explain why those items were selected.
Display recommendations on an interactive dashboard using Streamlit.

🚀 Setup Instructions
Clone the repo
git clone [https://github.com/MAHALAKSHMI837/shopgenius.git]
cd ecommerce_recommender

Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run the app
streamlit run dashboard.py

📁 Project Structure
kotlin
Copy code
ecommerce-genai/
│
├── agents/
│   ├── customer_agent.py
│   ├── product_agent.py
│   ├── explainability_agent.py
│
├── data/
│   ├── customers.csv
│   ├── products.csv 
│
├── dashboard.py
├── recommendation_engine.py
├── requirements.txt
└── README.md
📸 Screenshots
Include images of your dashboard UI showing personalized recommendations and explanations.

✅ To Do (or Optional Extensions)
Add Chat-based GenAI Shopping Assistant
Real-time Feedback Loop Agent
Admin Dashboard with Insights
Explainable AI Visualizations
Integration with Payment and Inventory Systems

💡 Inspiration
Built as part of a hackathon to showcase personalized e-commerce experiences using GenAI, ML, and intelligent agent design.

🧑‍💻 Author
Mahalakshmi S ,Varsha A
Feel free to reach out on LinkedIn or contribute via GitHub!
