import json
import requests
import streamlit as st

API_BASE = "http://127.0.0.1:8000"
REQUEST_TIMEOUT = 120

st.set_page_config(
    page_title="LeetCode Solver Agent",
    layout="wide",
)

st.title("LeetCode Solver Agent")
st.caption(
    "An agentic coding workflow that classifies problems, retrieves patterns, plans solutions, generates Python code, and validates outputs against test cases."
)


def call_solve_api(payload: dict):
    response = requests.post(
        f"{API_BASE}/solve",
        json=payload,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def render_result(result: dict):
    st.subheader("Workflow Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Success", str(result.get("success")))
    col2.metric("Attempts", result.get("attempts", "N/A"))
    col3.metric("Predicted Pattern", result.get("pattern", {}).get("pattern", "N/A"))

    st.subheader("Pattern Classification")
    st.json(result.get("pattern", {}))

    st.subheader("Solution Plan")
    st.json(result.get("plan", {}))

    st.subheader("Generated Code")
    st.code(result.get("code", ""), language="python")

    st.subheader("Evaluation")
    st.json(result.get("evaluation", {}))


default_problem = """Given an array of integers nums and an integer k, return the maximum sum of any contiguous subarray of size k."""
default_examples = """Input: nums = [2,1,5,1,3,2], k = 3
Output: 9"""
default_constraints = """1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= len(nums)"""

default_test_cases = [
    {"input": [[2, 1, 5, 1, 3, 2], 3], "output": 9},
    {"input": [[1, 2, 3, 4, 5], 2], "output": 9},
    {"input": [[5, 5, 5, 5], 1], "output": 5},
]

with st.sidebar:
    st.header("System")
    st.write("Make sure the FastAPI backend is running before submitting.")
    st.code("uvicorn app.main:app --reload", language="bash")

    st.header("Sample Test Cases Format")
    st.code(
        json.dumps(default_test_cases, indent=2),
        language="json",
    )

problem = st.text_area(
    "Problem Statement",
    value=default_problem,
    height=180,
)

examples = st.text_area(
    "Examples",
    value=default_examples,
    height=120,
)

constraints = st.text_area(
    "Constraints",
    value=default_constraints,
    height=120,
)

test_cases_text = st.text_area(
    "Test Cases (JSON)",
    value=json.dumps(default_test_cases, indent=2),
    height=220,
)

submit = st.button("Run Agent", use_container_width=True)

if submit:
    if not problem.strip():
        st.warning("Problem statement is required.")
    else:
        try:
            parsed_test_cases = json.loads(test_cases_text)

            payload = {
                "problem": problem,
                "examples": examples,
                "constraints": constraints,
                "test_cases": parsed_test_cases,
            }

            with st.spinner("Running agent workflow..."):
                result = call_solve_api(payload)

            render_result(result)

        except json.JSONDecodeError:
            st.error("Test cases must be valid JSON.")
        except requests.exceptions.RequestException as exc:
            st.error(f"Could not connect to backend: {exc}")
        except Exception as exc:
            st.error(f"Unexpected error: {exc}")