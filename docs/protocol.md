Protocol development for IntentMesh is tracked in Issue #1.

This document evolves alongside that discussion and reflects the current working protocol draft.

# IntentMesh Protocol

The IntentMesh protocol defines how agents negotiate structured intents.

## Interaction Flow

1. Agent publishes intent contract
2. Receiving agent validates schema
3. Constraint engine evaluates request
4. Negotiation engine generates execution plans
5. Counterfactual simulator tests scenarios
6. Response returned to requesting agent

## Intent Contract Structure

Intent contracts contain:

intent_id
objective
constraints
preferences
execution_policy
risk_tolerance

These contracts allow heterogeneous systems to interpret requests consistently.

## Response Structure

Agents return execution plans containing:

execution_path
risk_score
estimated_cost
simulation_summary
