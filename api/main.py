from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.engine import AgenticOrchestrator

app = FastAPI(title="GenAI Networking Orchestrator API")
orchestrator = AgenticOrchestrator()

class NetworkIntent(BaseModel):
    command: str
    target_env: str = "production"

@app.post("/api/v1/orchestrate")
async def trigger_workflow(intent: NetworkIntent):
    """
    Gateway to trigger autonomous network orchestration.
    Handles natural language commands and routes to the reasoning engine.
    """
    try:
        result = await orchestrator.process_intent(intent.command)
        return {"status": "success", "execution_plan": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "operational", "scale": "100M+ handled"}
