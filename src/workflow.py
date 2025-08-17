from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from .models import ResearchState, ModelInfo, ModelAnalysis
from .firecrawl import FirecrawlService
from .prompts import BenchmarkPrompts



class Workflow:
    def __init__(self):
        self.firecrawl = FirecrawlService()
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
        self.prompts = BenchmarkPrompts()
        self.workflow = self._build_workflow()

    def _build_workflow(self):
        graph = StateGraph(ResearchState)
        graph.add_node("extract_models", self._extract_models_step)
        graph.add_node("research", self._research_step)
        graph.add_node("analyze", self._analyze_step)
        graph.set_entry_point("extract_models")
        graph.add_edge("extract_models", "research")
        graph.add_edge("research", "analyze")
        graph.add_edge("analyze", END)
        return graph.compile()

    # 1) Find candidate model names from relevant pages
    def _extract_models_step(self, state: ResearchState) -> Dict[str, Any]:
        print(f"🔎 Finding models for: {state.query}")

        article_query = f"{state.query} best models benchmark comparison"
        search_results = self.firecrawl.search_models(article_query, num_results=3)

        all_content = ""
        if search_results and getattr(search_results, "data", None):
            for result in search_results.data:
                url = result.get("url", "")
                scraped = self.firecrawl.scrape_page(url)
                if scraped and getattr(scraped, "markdown", ""):
                    all_content += scraped.markdown[:1500] + "\n\n"

        messages = [
            SystemMessage(content=self.prompts.MODEL_EXTRACTION_SYSTEM),
            HumanMessage(content=self.prompts.model_extraction_user(state.query, all_content))
        ]

        try:
            response = self.llm.invoke(messages)
            raw_lines = [ln.strip() for ln in response.content.splitlines() if ln.strip()]

            # Heuristics: keep 1–5 token-ish names; drop clearly narrative sentences
            model_names = []
            for ln in raw_lines:
                # If line looks like a whole sentence, skip
                if ln.endswith(('.', '!', '?')) or len(ln.split()) > 6:
                    continue
                model_names.append(ln)

            model_names = model_names[:5]
            if not model_names:
                print("No clean model names extracted.")
            else:
                print(f"Extracted models: {', '.join(model_names[:5])}")
            return {"extracted_models": model_names}
        except Exception as e:
            print(e)
            return {"extracted_models": []}


    # Helper: structured analysis for one model
    def _analyze_model_content(self, model_name: str, content: str) -> ModelAnalysis:
        # 👇 add method="function_calling"
        structured_llm = self.llm.with_structured_output(ModelAnalysis, method="function_calling")

        messages = [
            SystemMessage(content=self.prompts.MODEL_ANALYSIS_SYSTEM),
            HumanMessage(content=self.prompts.model_analysis_user(model_name, content))
        ]

        try:
            analysis = structured_llm.invoke(messages)
            return analysis
        except Exception as e:
            print(e)
            return ModelAnalysis(description="Analysis failed")


    # 2) For each model, find its best source page and extract structured fields
    def _research_step(self, state: ResearchState) -> Dict[str, Any]:
        extracted_models = getattr(state, "extracted_models", [])

        if not extracted_models:
            print("⚠️ No extracted models found, falling back to direct search + seeds")
            # Seed list for this class of query
            seed_models = ["DistilBERT", "TinyBERT", "MobileBERT", "MiniLM"]
            model_names = seed_models
        else:
            model_names = extracted_models[:4]

        print(f"🧪 Researching models: {', '.join(model_names) if model_names else '—'}")

        models = []
        for model_name in model_names:
            search_hits = self.firecrawl.search_models(f"{model_name} model card benchmark", num_results=1)
            if not (search_hits and getattr(search_hits, "data", None)):
                continue

            result = search_hits.data[0]
            url = result.get("url", "")

            scraped = self.firecrawl.scrape_page(url)
            content = scraped.markdown if scraped and getattr(scraped, "markdown", "") else ""

            analysis = self._analyze_model_content(model_name, content)

            info = ModelInfo(
                name=model_name,
                source_url=url,
                description=(analysis.description or ""),
                task=analysis.task,
                benchmarks=(analysis.benchmarks or {}),
                params=analysis.params,
                latency=analysis.latency,
                memory_footprint=analysis.memory_footprint,
                license=analysis.license,
                openness=analysis.openness,
                strengths=(analysis.strengths or []),
                limitations=(analysis.limitations or []),
                recommended_usage=(analysis.recommended_usage or []),
            )
            models.append(info)

        return {"models": models}


    # 3) Short recommendation across options
    def _analyze_step(self, state: ResearchState) -> Dict[str, Any]:
        print("🧭 Generating benchmark-driven recommendation")

        model_data = ", ".join([m.json() for m in state.models])

        messages = [
            SystemMessage(content=self.prompts.RECOMMENDATIONS_SYSTEM),
            HumanMessage(content=self.prompts.recommendations_user(state.query, model_data))
        ]

        response = self.llm.invoke(messages)
        return {"analysis": response.content}

    def run(self, query: str) -> ResearchState:
        initial_state = ResearchState(query=query)
        final_state = self.workflow.invoke(initial_state)
        return ResearchState(**final_state)
