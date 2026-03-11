# IntentMesh Examples

This document provides example intent contracts and negotiation responses.

## Example Intent Contract

A consumer agent searching for a home.

{
  "intent_id": "example-001",
  "objective": "purchase_primary_residence",
  "constraints": {
    "location": "Austin, TX",
    "budget_max": 750000,
    "bedrooms_min": 3
  },
  "execution_policy": {
    "require_verified_counterparty": true,
    "max_agents_involved": 5
  }
}

## Example Negotiation Response

{
  "intent_id": "example-001",
  "accepted": true,
  "plan_options": [
    {
      "execution_path": [
        "listing_agent",
        "mortgage_agent",
        "insurance_agent"
      ],
      "risk_score": 0.12,
      "estimated_cost": 740000
    }
  ]
}
