from fastapi import FastAPI, HTTPException

from app.agent.workflow import run_agent
from app.schemas import SolveRequest, SolveResponse

app = FastAPI(title="LeetCode Solver Agent")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/solve", response_model=SolveResponse)
def solve_problem(request: SolveRequest):
    try:
        result = run_agent(
            problem=request.problem,
            examples=request.examples,
            constraints=request.constraints,
            test_cases=[tc.model_dump() for tc in request.test_cases],
        )
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))