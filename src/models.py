from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class ModelAnalysis(BaseModel):
    """Structured output for LLM model analysis focused on benchmarks & deployment trade-offs"""
    task: Optional[str] = None  # e.g., "NLP - QA", "Vision - Classification"
    benchmarks: Dict[str, float] = {}  # {"MMLU": 74.2, "GLUE": 88.1}
    params: Optional[str] = None       # e.g., "7B", "70M"
    latency: Optional[str] = None      # e.g., "35ms (A100, bs=1)"
    memory_footprint: Optional[str] = None  # e.g., "~8GB FP16"
    license: Optional[str] = None      # e.g., "Apache-2.0", "Proprietary"
    openness: Optional[str] = None     # "Open-source", "Closed-source", "Partially open"
    description: str = ""              # 1-sentence overview
    strengths: List[str] = []
    limitations: List[str] = []
    recommended_usage: List[str] = []  # e.g., ["Edge devices", "Low-latency chatbots"]


class ModelInfo(BaseModel):
    name: str
    source_url: str
    description: str = ""
    task: Optional[str] = None
    benchmarks: Dict[str, float] = {}
    params: Optional[str] = None
    latency: Optional[str] = None
    memory_footprint: Optional[str] = None
    license: Optional[str] = None
    openness: Optional[str] = None
    strengths: List[str] = []
    limitations: List[str] = []
    recommended_usage: List[str] = []


class ResearchState(BaseModel):
    query: str
    extracted_models: List[str] = []     # model names pulled from sources
    models: List[ModelInfo] = []         # enriched model entries
    search_results: List[Dict[str, Any]] = []
    analysis: Optional[str] = None
