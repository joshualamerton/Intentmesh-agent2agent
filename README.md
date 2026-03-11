IntentMesh-agent2agent

IntentMesh is an open protocol and reference architecture for structured negotiation between autonomous software agents.

As software systems become agentic, the interaction model is shifting from:

human → software → outcome

to

agent → agent → coordinated outcome

Most current agent frameworks enable agents to call APIs, invoke functions, or exchange messages. However they lack mechanisms for:

• constraint validation
• negotiation between agents
• counterfactual outcome simulation
• trust evaluation between systems

IntentMesh proposes a negotiation layer that allows agents to exchange structured intent contracts, simulate outcomes, and coordinate execution safely.

Motivation

Autonomous systems will increasingly interact directly with other autonomous systems.

Examples include:

consumer agents negotiating purchases
supply chain agents coordinating logistics
financial agents executing transactions
infrastructure agents allocating compute resources

Without structured negotiation infrastructure, these systems remain fragile.

IntentMesh introduces a layer that enables agents to:

express goals
evaluate constraints
simulate outcomes
assess trust before execution

Core Idea

Instead of simple API requests, agents exchange Intent Contracts.

An Intent Contract describes:

objective
constraints
preferences
execution policies
risk tolerance

Receiving agents evaluate the request and return execution plans rather than simple responses.

Execution plans include:

possible execution paths
estimated costs
risk scores
simulation results

System Architecture

IntentMesh sits between communication protocols and execution layers.

Applications
commerce | travel | procurement | real estate

Execution Layer
APIs | payments | booking | compute services

IntentMesh Core
intent schema
constraint engine
negotiation engine
counterfactual simulator
trust ledger

Communication Layer
HTTP | WebSocket | A2A | MCP | gRPC

IntentMesh integrates with existing communication protocols rather than replacing them.

Core Components

Intent Schema
Defines the machine-readable structure of agent requests.

Constraint Engine
Evaluates whether requests comply with local policies.

Negotiation Engine
Allows agents to modify requests, propose alternatives, or reject actions.

Counterfactual Sandbox
Simulates potential outcomes before execution.

Trust Ledger
Records historical interactions between agents to evaluate reliability.

Example Intent Contract
{
  "intent_id": "abc-123",
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
Negotiation Response
{
  "intent_id": "abc-123",
  "accepted": true,
  "plan_options": [
    {
      "execution_path": [
        "listing_agent",
        "mortgage_agent",
        "insurance_agent"
      ],
      "score": 0.89,
      "risk_score": 0.11,
      "estimated_cost": 742000
    }
  ]
}
Example Use Case

US home purchase coordination.

A buyer agent submits constraints:

budget under $750k
minimum 3 bedrooms
school rating above 7

Multiple agents respond:

listing portal agent
mortgage underwriting agent
insurance pricing agent
title verification agent

IntentMesh aggregates results and returns ranked transaction paths.

Minimal Agent Flow

Buyer Agent
↓
Intent Contract
↓
IntentMesh Core
↓
Listing Agent evaluation
↓
Mortgage Agent simulation
↓
Negotiation Engine ranking
↓
Execution Plan returned

Repository Roadmap

Phase 1

Define intent schema
Publish protocol documentation
Build minimal Python SDK

Phase 2

Constraint evaluation engine
Negotiation engine
Simulation framework

Phase 3

Trust ledger implementation
Agent reputation scoring

Phase 4

Agent discovery systems
Economic negotiation models
Adversarial agent defense

Proposed Repository Structure

intentmesh

docs
architecture.md
protocol.md

spec
intent_schema.json
trust_event_schema.json

core
constraint_engine
negotiation_engine
simulation_engine

sdk
python
typescript

examples
commerce_agent
property_agent

Contribution Areas

constraint evaluation systems
counterfactual simulation frameworks
agent reputation models
economic negotiation algorithms

License

Apache 2.0
