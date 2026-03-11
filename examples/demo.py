class Intent:
    def __init__(self, intent_id, objective, constraints):
        self.intent_id = intent_id
        self.objective = objective
        self.constraints = constraints


class Agent:
    def __init__(self, name):
        self.name = name

    def evaluate_intent(self, intent):
        if intent.objective == "purchase_property":
            budget = intent.constraints.get("budget_max", 0)

            if budget >= 700000:
                return {
                    "accepted": True,
                    "plan": {
                        "execution_path": [
                            "listing_agent",
                            "mortgage_agent",
                            "insurance_agent"
                        ],
                        "estimated_cost": 720000,
                        "risk_score": 0.12
                    }
                }

        return {"accepted": False}


def run_demo():
    intent = Intent(
        intent_id="demo-001",
        objective="purchase_property",
        constraints={
            "location": "Austin, TX",
            "budget_max": 750000,
            "bedrooms_min": 3
        }
    )

    negotiation_agent = Agent("intentmesh_negotiator")

    result = negotiation_agent.evaluate_intent(intent)

    print("Intent submitted:")
    print(intent.__dict__)

    print("\nNegotiation result:")
    print(result)


if __name__ == "__main__":
    run_demo()
