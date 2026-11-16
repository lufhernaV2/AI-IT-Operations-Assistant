# AI IT Operations Assistant

**A Python-based enterprise AI engineering portfolio project**

An AI-powered IT support assistant designed to help managed service providers (MSPs) and internal IT departments streamline ticket triage, troubleshoot common issues, and safely automate support workflows.

This project is being developed incrementally through a 30-session Python Forward Deployed AI Engineer bootcamp.

## Project Status

**Current phase:** Week 1 — Python Foundations  
**Progress:** Day 1 of 30 completed  
**Development status:** Early prototype

The application currently consists of basic Python functions for processing support tickets and validating ticket IDs. AI integration, backend APIs, databases, and deployment are planned for later development phases.

## Business Problem

IT support departments frequently handle repetitive requests involving account access, network connectivity, software installation, and technical troubleshooting.

Manual ticket triage and investigation can increase resolution times and create unnecessary workloads for support teams.

The goal is to build a system that assists technicians by analyzing incoming tickets, retrieving relevant troubleshooting information, recommending actions, and executing approved operations through authorized integrations.

## Target Architecture

The planned system will follow this general architecture:

```text
IT Support Ticket / External System
                |
                v
         FastAPI Backend
                |
                v
       Ticket Validation
                |
                v
        AI Agent / LLM
                |
       +--------+--------+
       |        |        |
       v        v        v
      RAG     Tools   PostgreSQL
       |        |
       +----+---+
            |
            v
    Authorization / Approval
            |
            v
    Result and Execution Log
```

The backend will control execution, enforce authorization policies, and validate AI-generated tool requests.

## Technology Stack

| Area | Technology | Status |
|---|---|---|
| Programming | Python | In use |
| Backend API | FastAPI, Pydantic | Planned |
| AI | LLM integration, function calling | Planned |
| Agent architecture | Python agent execution loop | Planned |
| Retrieval | RAG and embeddings | Planned |
| Database | PostgreSQL | Planned |
| Integrations | REST APIs, OAuth, webhooks | Planned |
| Testing | PyTest, DeepEval | Planned |
| Infrastructure | Docker, GitHub Actions | Planned |
| Observability | Structured logging and tracing | Planned |

## Current Capabilities

The initial Python implementation demonstrates:

- Reusable ticket-processing functions.
- Dictionary-based ticket representation.
- Safe fallback messages for missing descriptions.
- Ticket ID retrieval and basic runtime type validation.
- Exception handling for missing dictionary keys.
- Conditional control flow and early returns.

These are foundational exercises, not yet a complete ticket-processing backend.

## Planned Development Roadmap

### Week 1 — Python and AI Foundations
- Python functions, modules, data structures, and type hints.
- FastAPI ticket intake.
- LLM integration.
- Structured outputs.
- Function calling and basic agent loops.

### Week 2 — Persistence and Enterprise Integrations
- PostgreSQL and database models.
- External REST APIs.
- Authentication and authorization.
- OAuth fundamentals.
- Event-driven processing and webhooks.

### Week 3 — RAG and Reliable AI Systems
- Knowledge-base retrieval.
- Embeddings and grounded responses.
- Human approval workflows.
- Retry handling and idempotency.
- Automated AI evaluations and security testing.

### Week 4 — Deployment and Customer Delivery
- Docker containerization.
- Deployment to an appropriate environment.
- Observability and tracing.
- GitHub Actions CI/CD.
- Incident troubleshooting.
- Simulated customer implementation and final demo.

The roadmap may change as technical requirements and findings evolve.

## Getting Started

### Requirements

- Python 3.10 or newer for the current foundational exercises.
- Git.
- A Python virtual environment.

Later features may require a newer supported Python version.

### Local Setup (Windows PowerShell)

```powershell
git clone https://github.com/lufhernaV2/AI-IT-Operations-Assistant.git
cd AI-IT-Operations-Assistant

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python main.py
```

The repository URL above will work after the repository is created and pushed.

The current project requires no third-party Python dependencies.

## Development Journal

### Day 1 — FDE Fundamentals and Python Foundations

**Status:** Completed

**Topics covered**
- Forward Deployed Engineer responsibilities and technical discovery.
- LLMs versus AI applications, agents, and workflows.
- Python virtual environments.
- Functions, dictionaries, and return values.
- Type hints and conditional logic.
- `None`, `.get()`, and fallback values.
- Exception handling using `try` and `except`.
- Runtime validation using `isinstance()`.

**Implemented**
- Created and verified the local Python environment.
- Developed initial ticket-processing functions.
- Added basic ticket ID validation.
- Handled missing descriptions and missing ticket IDs.
- Executed manual verification scenarios.

**Verification**
- Python scripts executed successfully.
- Ticket-processing examples returned expected outputs.
- Three ticket ID validation scenarios passed.
- Automated tests have not yet been implemented.

**Key engineering lessons**
- Application logic must enforce permissions and approval rules independently of an LLM.
- Type hints do not enforce runtime validation.
- Missing dictionary keys and invalid data types require different handling.
- Early returns help prevent invalid inputs from reaching later operations.

**Areas to revisit**
- Function execution flow and early returns.
- Exceptions versus returned error values.
- Input validation and data contracts.

### Day 2 — Python Data Structures, Modules, and Unit Testing

**Status:** Completed

#### Concepts Learned
- Python lists and zero-based indexing.
- Iteration using `for` loops.
- Processing collections of dictionaries.
- Separation of concerns and reusable functions.
- Organizing code using Python modules and imports.
- `continue` versus `return`.
- Writing unit tests with PyTest.
- Arrange–Act–Assert testing methodology.

#### Features Implemented
- Extended the application to process multiple IT support tickets.
- Created `ticket_processor.py` to separate ticket-processing logic from `main.py`.
- Implemented ticket ID validation before processing.
- Added logic to skip tickets containing invalid IDs.
- Created `tests/test_ticket_processor.py`.
- Installed PyTest 9.2.0.

#### Automated Testing Results

| Test | Result |
|---|---|
| Valid ticket ID | PASSED |
| Missing ticket ID | PASSED |
| Invalid ticket ID type | PASSED |

**Total: 3 tests passed, 0 failed.**

#### Engineering Takeaways
- Modularity improves application maintainability and testability.
- Functions should have clearly defined responsibilities.
- Input validation should occur before business logic executes.
- Invalid individual records should not necessarily interrupt an entire batch.
- Automated tests protect existing functionality against regressions.

#### Areas for Improvement
- Add additional edge-case validation.
- Improve error reporting for rejected tickets.
- Introduce structured ticket models.
- Expand automated coverage to ticket formatting and batch processing.

## Day 3 — FastAPI Backend and API Testing

**Status:** Completed

### Objectives

Build the first HTTP API for the AI IT Operations Assistant, integrate existing Python ticket-processing logic, validate incoming requests, and introduce automated API integration tests.

### Implemented

- Created a FastAPI application in `api.py`.
- Added `GET /` to return an application status message.
- Added `POST /tickets` to accept support-ticket data in JSON format.
- Introduced a Pydantic `Ticket` model to validate incoming data.
- Enforced the permitted priority values `High`, `Medium`, and `Low` using Python's `Literal` type.
- Integrated the existing `process_ticket()` function from `ticket_processor.py`.
- Used `model_dump()` to convert validated Pydantic data into a dictionary for existing business logic.
- Verified both endpoints using Swagger UI.
- Added automated API integration tests using FastAPI's `TestClient` and PyTest.

### Validation Scenarios

Manually verified:
- Successful ticket submission.
- Malformed JSON rejection.
- Missing required priority field.
- Unsupported priority value.

Automated tests:
- `test_create_ticket_success`
- `test_create_ticket_invalid_priority`
- Three existing ticket ID validation unit tests.

**Regression result: 5 tests passed, 0 failed.**

### Architecture

The application now separates:

- **API layer (`api.py`):** HTTP routing, request validation, and response generation.
- **Business logic (`ticket_processor.py`):** Reusable Python ticket-processing functions.
- **Test layer (`tests/`):** Unit tests and API integration tests.

### Important Engineering Concepts Learned

- HTTP GET versus POST
- REST-style API endpoints
- JSON request and response bodies
- HTTP status codes and validation errors
- FastAPI routing decorators
- Pydantic models and required fields
- Type validation versus business-rule validation
- Python `Literal`
- Pydantic `model_dump()`
- Separation of concerns
- Unit testing versus API integration testing
- Automated positive and negative API testing

### Current Limitations

The API currently validates and formats ticket data but does not persist tickets to a database.

It also does not yet perform AI classification, troubleshoot IT incidents, execute tools, or enforce an operational escalation workflow.

### Next Steps

- Improve ticket validation and error handling.
- Develop structured response models.
- Extend reusable business logic.
- Continue toward LLM-assisted ticket classification and investigation.