from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class EvaluationOutput(BaseModel):
    score: float
    feedback: str


class EvaluationBatchOutput(BaseModel):
    job_id: str = Field(..., description="ID of the batch job")
    status: JobStatus = Field(..., description="Status of the job")
    results: Optional[List[EvaluationOutput]] = Field(None, description="Results of the evaluation")
    error: Optional[str] = Field(None, description="Error message (only when status is FAILED)")
