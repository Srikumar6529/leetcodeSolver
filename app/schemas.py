from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class TestCase(BaseModel):
    input: List[Any]
    output: Any


class SolveRequest(BaseModel):
    problem: str
    examples: Optional[str] = ""
    constraints: Optional[str] = ""
    test_cases: List[TestCase]


class SolveResponse(BaseModel):
    success: bool
    attempts: int
    pattern: Dict[str, Any]
    plan: Dict[str, Any]
    code: str
    evaluation: Dict[str, Any]