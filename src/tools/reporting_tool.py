from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class ReportingToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    decision: str = Field(..., description="Either approve or reject")
    reason: str = Field(..., description="Reason for why expense was approved or rejected")

class ReportingTool(BaseTool):
    name: str = "Report Expense Tool"
    description: str = (
        "Call this tool when you have made the decision to approve or reject the expense in order to pass it into the system."
    )
    args_schema: Type[BaseModel] = ReportingToolInput

    def _run(self, decision: str, reason: str) -> str:
        # Implementation goes here
        print("Decision: ", decision)
        print("Reason: ", reason)
        return "Report Sent"
