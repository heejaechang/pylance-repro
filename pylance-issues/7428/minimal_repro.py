# Minimal repro without langchain-openai dependency
# This demonstrates the same underlying issue with Pydantic's populate_by_name
from pydantic import BaseModel, Field


class MyModel(BaseModel):
    model_config = {"populate_by_name": True}
    openai_api_key: str = Field(alias="api_key")
    openai_api_version: str = Field(alias="api_version")


# These should NOT produce errors (populate_by_name=True allows original names)
m1 = MyModel(openai_api_key="sk-xxx", openai_api_version="2024-01-01")

# These use aliases (always valid)
m2 = MyModel(api_key="sk-xxx", api_version="2024-01-01")
