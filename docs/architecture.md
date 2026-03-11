# IntentMesh Architecture

IntentMesh introduces a negotiation layer between communication protocols and execution systems.

The system allows autonomous agents to exchange structured intent contracts, evaluate constraints, simulate outcomes, and negotiate execution paths.

## Layer Model

Applications
commerce | travel | procurement | real estate | infrastructure

Execution Layer
APIs | payments | booking | compute resources | databases

IntentMesh Core
intent schema
constraint engine
negotiation engine
counterfactual simulator
trust ledger

Communication Layer
HTTP | WebSocket | A2A | MCP | gRPC

IntentMesh sits between communication and execution.

Agents communicate through existing protocols but rely on IntentMesh to validate and negotiate requests before actions occur.
