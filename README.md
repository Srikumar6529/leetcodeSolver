# Agentic LeetCode Solver using Claude API

## Overview

This project implements an **agentic coding workflow** that solves algorithmic problems by combining structured reasoning, pattern retrieval, code generation, and execution-based validation.

Instead of relying on a single prompt, the system decomposes problem solving into multiple stages, enabling more reliable, interpretable, and correct solutions.

The system is designed to reflect how real-world AI systems operate: iterative, modular, and evaluation-driven.

---

## Architecture

The system follows a multi-stage pipeline:


Problem Input

→ Classification

→ Pattern Retrieval

→ Planning

→ Code Generation

→ Execution

→ Evaluation

→ Retry Loop


### Components

**Classifier**  
Identifies the underlying algorithmic pattern (e.g., sliding window, dynamic programming, graph traversal).

**Retriever**  
Fetches structured pattern knowledge, including usage conditions and implementation templates.

**Planner**  
Generates a structured solution plan including:
- approach
- pseudocode
- edge cases

**Code Generator**  
Produces Python code aligned with the plan and selected pattern.

**Tester**  
Executes generated code against test cases.

**Evaluation Loop**  
If the solution fails, the system uses feedback to iteratively refine and fix the code.

---

## Key Features

- Multi-stage reasoning pipeline (not single-shot prompting)
- Pattern-aware problem solving
- Execution-based validation of generated code
- Automatic retry and repair loop
- Modular agent-based architecture
- FastAPI backend for API access
- Streamlit UI for interactive usage

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- Claude API (Anthropic)
- FAISS (optional for vector retrieval)

---

## Benchmark Results

The system was evaluated on curated algorithm problem sets.

### Easy / Medium Benchmark
- 8 / 8 problems solved
- 100% pattern classification accuracy
- 100% test pass rate

### Hard Benchmark
- 8 / 8 problems solved
- 7 / 8 correct pattern predictions (acceptable alternate patterns observed)
- Retry loop successfully corrected errors in complex problems

### Problem Coverage

- Sliding Window
- Hash Maps
- Stacks
- Binary Search
- Dynamic Programming
- Graph Traversal
- Backtracking
- Heaps / Priority Queues
- Trees

---

## Project Structure
<pre>
leetcodeSolver/
├── app/
│   ├── agent/
│   │   ├── classifier.py
│   │   ├── retriever.py
│   │   ├── planner.py
│   │   ├── coder.py
│   │   ├── tester.py
│   │   └── workflow.py
│   ├── utils/
│   │   └── json_utils.py
│   ├── data/
│   │   └── patterns.json
│   ├── main.py
│   ├── schemas.py
│   └── config.py
├── streamlit_app.py
├── requirements.txt
└── README.md
</pre>

## Getting Started
1. Setup Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Start FastAPI backend
python -m uvicorn app.main:app --reload

Open API docs:
http://127.0.0.1:8000/docs
3. Start Streamlit UI
streamlit run streamlit_app.py

Example Workflow Output
Given a problem:
Predicted Pattern: sliding_window
    Generated Plan:
    Approach description
    Pseudocode
    Edge cases
    Generated Code:
    Python function implementation
    Evaluation:
    Test results
    Pass/fail status
    Retry attempts (if needed)

Design Considerations
    The system separates reasoning (planning) from execution (coding), improving reliability.
    Execution-based evaluation ensures correctness beyond surface-level responses.
    Retry loop introduces feedback-driven refinement, making the system robust on harder problems.
    Structured JSON outputs enable modular composition of agents.

Limitations
    Relies on LLM quality for reasoning and code generation
    Execution uses Python exec, which is not sandboxed for production environments
    Complex data structures (e.g., trees with custom classes) require additional abstraction handling

Summary

    This project demonstrates how to build a production-style agentic system for solving algorithmic problems by combining:
        structured reasoning
        retrieval-augmented guidance
        code generation
        execution-based validation
        iterative self-correction

    It is designed to showcase practical skills in:
        LLM application development
        system design
        evaluation.