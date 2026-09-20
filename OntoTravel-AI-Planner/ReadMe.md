# 🌍 OntoTravel: AI-Based Travel Planner

OntoTravel is an AI-driven travel recommendation system built to demonstrate the integration and reuse of domain-specific Knowledge Bases (KBs) and ontologies. By querying interconnected data regarding tourist destinations, local gastronomy, wine pairings, and cost assessments, the system generates highly personalized, budget-conscious travel itineraries.

## 🧠 System Architecture & Knowledge Bases

This project simulates Semantic Web concepts by defining discrete knowledge domains and using a rule-based AI agent to traverse them:

1. **Tourist Ontology:** Maps geographic locations to specific metadata tags (e.g., history, art, nature).
2. **Gastronomy / Food KB:** Links destinations to local culinary specialties.
3. **Wine Ontology:** Maps specific local dishes to their optimal wine/beverage pairings.
4. **Cost Assessment KB:** Defines standard daily expenses and accommodation metrics for budget filtering.

## ⚙️ How the AI Agent Works

The `AITravelPlanner` class acts as the intelligent agent. Its decision-making pipeline follows these steps:
1. **Constraint Satisfaction:** Evaluates the user's maximum budget against the `Cost Assessment KB`.
2. **Semantic Matching:** Calculates a heuristic score by intersecting the user's explicit interests with the `Tourist Ontology` tags.
3. **Data Retrieval:** Once an optimal destination is selected, the agent traverses the `Food` and `Wine` ontologies to extract contextual recommendations.

## 🚀 Installation & Usage

### Prerequisites
- Python 3.x
- No external libraries required (uses standard built-in libraries).

### Running the Planner
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/OntoTravel-AI-Planner.git](https://github.com/your-username/OntoTravel-AI-Planner.git)