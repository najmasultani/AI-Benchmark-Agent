class BenchmarkPrompts:
    """Prompts for extracting model names and analyzing benchmarks/trade-offs."""

    # Model extraction
    MODEL_EXTRACTION_SYSTEM = """You are an AI benchmarking researcher.
Extract concrete model names from the provided content (e.g., 'Llama 3 8B', 'Phi-3-mini', 'GPT-4o-mini', 'DeiT', 'ConvNeXt').
Return only real model names, not datasets, tasks, frameworks, or generic terms."""

    @staticmethod
    def model_extraction_user(query: str, content: str) -> str:
        return f"""Query: {query}
Content:
{content}

Task:
- List up to 5 specific model names relevant to the query.
- Prefer models with public cards/benchmarks (Hugging Face, Papers with Code).
- One model per line, no descriptions or extra text.

Example format:
Llama 3 8B
Phi-3-mini
Mistral 7B
GPT-4o-mini
DeiT-Tiny
"""

    # Model analysis → structured
    MODEL_ANALYSIS_SYSTEM = """You analyze AI models for benchmark performance and deployment trade-offs.
Focus on benchmark scores, parameter count, latency, memory footprint, license/openness, strengths/limitations, and recommended usage."""

    @staticmethod
    def model_analysis_user(model_name: str, content: str) -> str:
        return f"""Model: {model_name}
Model Card / Paper / Repo Content (truncated):
{content[:2500]}

Extract structured fields:
- task: short task category (e.g., "NLP - QA", "Vision - Classification", "Multimodal")
- benchmarks: dict of key metrics, e.g. {{"MMLU": 74.2, "GLUE": 88.1}}
- params: parameter size (e.g., "7B", "70M")
- latency: typical inference latency and hardware notes if available
- memory_footprint: approximate VRAM/RAM needs for FP16/INT8
- license: license string (e.g., "Apache-2.0", "MIT", "Proprietary")
- openness: one of "Open-source", "Closed-source", or "Partially open"
- description: 1 short sentence describing the model
- strengths: 2–5 bullet points
- limitations: 2–5 bullet points
- recommended_usage: 2–5 bullet points for when to choose this model

If info is missing, leave fields blank or make a concise best-effort inference."""

    # Short recommendation
    RECOMMENDATIONS_SYSTEM = """You are a senior ML engineer. Provide a brief, practical recommendation (max 4 sentences) choosing models for the user's need.
Call out accuracy/latency/cost trade-offs and license/openness considerations."""

    @staticmethod
    def recommendations_user(query: str, model_data: str) -> str:
        return f"""User Need: {query}
Models Analyzed (JSON-ish):
{model_data}

Write 3–4 sentences:
- Which model(s) you would pick and why (accuracy vs latency vs memory vs license).
- Any notable risks or limitations.
- A backup option for constrained environments (e.g., edge or tight VRAM)."""
