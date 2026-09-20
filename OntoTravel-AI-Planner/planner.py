import json

# ==========================================
# 1. KNOWLEDGE BASES (Simulated Ontologies)
# ==========================================

TOURIST_ONTOLOGY = {
    "Paris": {"tags": ["art", "history", "romantic"], "region": "Europe"},
    "Rome": {"tags": ["history", "architecture", "food"], "region": "Europe"},
    "Kyoto": {"tags": ["history", "culture", "nature"], "region": "Asia"},
    "Napa_Valley": {"tags": ["nature", "relaxation", "wine"], "region": "North America"}
}

FOOD_ONTOLOGY = {
    "Paris": ["Croissant", "Coq au Vin", "Escargot"],
    "Rome": ["Carbonara", "Gelato", "Cacio e Pepe"],
    "Kyoto": ["Kaiseki", "Matcha", "Sushi"],
    "Napa_Valley": ["Farm-to-table salads", "Artisan Cheese", "Grilled Steak"]
}

WINE_ONTOLOGY = {
    "Coq au Vin": "Burgundy Pinot Noir",
    "Carbonara": "Frascati Superiore",
    "Artisan Cheese": "Cabernet Sauvignon",
    "Kaiseki": "Junmai Daiginjo Sake (Rice Wine substitute)"
}

COST_ASSESSMENT_KB = {
    "Paris": {"accommodation": 200, "daily_expenses": 150},
    "Rome": {"accommodation": 150, "daily_expenses": 100},
    "Kyoto": {"accommodation": 120, "daily_expenses": 90},
    "Napa_Valley": {"accommodation": 300, "daily_expenses": 200}
}

# ==========================================
# 2. AI PLANNER LOGIC
# ==========================================

class AITravelPlanner:
    def __init__(self, days, budget, interests):
        self.days = days
        self.budget = budget
        self.interests = set(interests)

    def assess_cost(self, destination):
        """Calculates total estimated cost based on the Cost KB."""
        costs = COST_ASSESSMENT_KB.get(destination)
        total_cost = (costs["accommodation"] + costs["daily_expenses"]) * self.days
        return total_cost

    def find_best_destination(self):
        """Matches user interests with the Tourist Ontology."""
        best_match = None
        highest_score = 0
        
        for place, data in TOURIST_ONTOLOGY.items():
            # Calculate interest intersection
            score = len(self.interests.intersection(set(data["tags"])))
            
            # Check budget constraints
            if score > highest_score and self.assess_cost(place) <= self.budget:
                highest_score = score
                best_match = place
                
        return best_match

    def generate_recommendations(self, destination):
        """Queries Food and Wine Ontologies for the chosen destination."""
        foods = FOOD_ONTOLOGY.get(destination, [])
        recommendations = []
        
        for food in foods:
            pairing = WINE_ONTOLOGY.get(food, "Local House Beverage")
            recommendations.append(f"Dish: {food} | Perfect Pairing: {pairing}")
            
        return recommendations

    def build_itinerary(self):
        """Compiles the final personalized plan."""
        print("🤖 Analyzing Knowledge Bases to build your plan...\n")
        
        destination = self.find_best_destination()
        
        if not destination:
            return "No destinations found matching your budget and interests. Try increasing your budget."

        total_cost = self.assess_cost(destination)
        gastronomy = self.generate_recommendations(destination)

        itinerary = {
            "Destination": destination,
            "Duration": f"{self.days} days",
            "Estimated Cost": f"${total_cost}",
            "Why we chose this": f"Matches your interests in: {', '.join(TOURIST_ONTOLOGY[destination]['tags'])}",
            "Gastronomy & Wine Pairings": gastronomy
        }
        
        return json.dumps(itinerary, indent=4)

# ==========================================
# 3. EXECUTION (Main)
# ==========================================
if __name__ == "__main__":
    # Example User Profile
    user_budget = 2000 # in USD
    user_days = 5
    user_interests = ["history", "architecture", "food"]
    
    print("User Profile:")
    print(f"- Budget: ${user_budget}\n- Days: {user_days}\n- Interests: {user_interests}\n")

    planner = AITravelPlanner(days=user_days, budget=user_budget, interests=user_interests)
    final_plan = planner.build_itinerary()
    
    print("🎯 FINAL PERSONALIZED ITINERARY:")
    print(final_plan)