from fastapi import APIRouter
from mindmap.generator import MindMapGenerator
from pydantic import BaseModel

router = APIRouter()
mindmap_gen = MindMapGenerator()

class MindMapRequest(BaseModel):
    topics: dict

@router.post("/generate")
async def generate_mindmap(request: MindMapRequest):
    """Generate mind map from topics"""
    html = mindmap_gen.create_mindmap(request.topics)
    return {"mindmap_html": html}