Agentic LeetCode Solver using Claude API
Overview

This project implements an agentic coding workflow that solves algorithmic problems by combining structured reasoning, pattern retrieval, code generation, and execution-based validation.

Instead of relying on a single prompt, the system decomposes the problem-solving process into multiple stages, enabling more reliable and interpretable solutions.

Architecture

The system follows a multi-stage pipeline:

Problem Input
→ Classification
→ Pattern Retrieval
→ Planning
→ Code Generation
→ Execution
→ Evaluation
→ Retry Loop
Components
Classifier
Identifies the underlying algorithmic pattern (e.g., sliding window, dynamic programming, graph traversal).
Retriever
Fetches structured pattern knowledge including usage guidelines and templates.
Planner
Generates a step-by-step solution strategy, pseudocode, and edge cases.
Code Generator
Produces Python code based on the plan and retrieved pattern.
Tester
Executes the generated code against test cases.
Evaluation Loop
If tests fail, the system uses feedback to iteratively refine and fix the solution.
Key Features
Multi-stage reasoning pipeline instead of single-shot prompting
Pattern-aware problem solving
Execution-based validation of generated code
Automatic retry and repair loop for failed solutions
FastAPI backend for programmatic access
Streamlit interface for interactive usage
Tech Stack
Python
FastAPI
Streamlit
Claude API (Anthropic)
FAISS (for vector-based retrieval, if enabled)
Benchmark Results

The system was evaluated on curated algorithm problem sets:

Easy / Medium Benchmark: 8/8 problems solved
Hard Benchmark: 8/8 problems solved
Retry loop successfully corrected errors in complex cases

These benchmarks include problems across:

Sliding Window
Hash Maps
Stacks
Binary Search
Dynamic Programming
Graph Traversal
Backtracking
Heaps
Project Structure
leetcodeSolver/
├── app/
│   ├── agent/
│   │   ├── classifier.py
│   │   ├── retriever.py
│   │   ├── planner.py
│   │   ├── coder.py
│   │   ├── tester.py
│   │   ├── workflow.py
│   ├── utils/
│   │   ├── json_utils.py
│   ├── main.py
│   ├── schemas.py
│   ├── config.py
├── streamlit_app.py
├── requirements.txt
└── README.md
Running the Project
1. Setup environment
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
Future Work
Sandboxed execution environment
Improved pattern taxonomy and retrieval
Model-agnostic optimization for lower-cost inference
Deployment as a hosted API
Integration with real coding platforms
Summary

This project demonstrates how to build a production-style agentic system for solving algorithmic problems by combining:

structured reasoning
retrieval-augmented guidance
code generation
execution-based validation
iterative self-correction

It is designed to showcase practical skills in LLM application development, system design, and evaluation.