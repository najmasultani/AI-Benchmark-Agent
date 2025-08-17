import reflex as rx
from dotenv import load_dotenv
load_dotenv()

from dataclasses import dataclass
from typing import List, Dict, Optional

# ---------- Lazy backend init ----------
_workflow: Optional["Workflow"] = None
def get_workflow():
    global _workflow
    if _workflow is None:
        from src.workflow import Workflow
        _workflow = Workflow()
    return _workflow

# ---------- Strongly-typed conversation turn ----------
@dataclass
class Turn:
    user: str
    logs_text: str                 # single string block
    models: List[Dict[str, str]]   # flat string dicts (for simple rendering)
    recommendation: str


# ---------- App State ----------
class AppState(rx.State):
    # Input + status
    query: str = ""
    running: bool = False
    error: str = ""
    logs: List[str] = []           # temp logs while a run is in progress

    # History (typed)
    turns: List[Turn] = []

    def set_query(self, q: str):
        self.query = q

    @rx.event(background=True)
    async def run_benchmark(self):
        q = self.query.strip()
        if q == "":
            return

        # start this run
        async with self:
            self.running = True
            self.error = ""
            self.logs = [f"Searching for: {q}"]

        # run backend
        try:
            result = get_workflow().run(q)
        except Exception as e:
            async with self:
                self.error = f"{type(e).__name__}: {e}"
                self.running = False
            return

        # make each model a flat string dict for simple rendering
        def clean_url(u: str) -> str:
            if not u:
                return ""
            # If the URL string accidentally contains two concatenated "http", keep the first segment.
            if u.count("http") >= 2:
                first = u.find("http")
                second = u.find("http", first + 4)
                if second != -1:
                    return u[first:second]
            return u

        def to_plain(m) -> Dict[str, str]:
            try:
                d = m.dict()
            except Exception:
                d = m.model_dump()

            def s(x, default="—"):
                return str(x) if (x is not None and str(x) != "") else default

            # benchmarks -> one string
            bmk = d.get("benchmarks") or {}
            if isinstance(bmk, dict) and len(bmk) > 0:
                items = list(bmk.items())[:5]
                bmk_txt = ", ".join([f"{k}: {v}" for k, v in items])
            else:
                bmk_txt = "—"

            def join_top(key, n):
                arr = d.get(key) or []
                return ", ".join([str(x) for x in arr[:n]]) if len(arr) > 0 else "—"

            return {
                "name": s(d.get("name"), "Unknown"),
                "source_url": clean_url(s(d.get("source_url"), "")),
                "task": s(d.get("task")),
                "params": s(d.get("params")),
                "latency": s(d.get("latency")),
                "memory_footprint": s(d.get("memory_footprint")),
                "license": s(d.get("license")),
                "openness": s(d.get("openness")),
                "description": s(d.get("description")),
                "benchmarks_text": bmk_txt,
                "strengths_text": join_top("strengths", 3),
                "limitations_text": join_top("limitations", 3),
                "recommended_text": join_top("recommended_usage", 4),
            }

        processed = [to_plain(m) for m in getattr(result, "models", [])]

        # finish this turn: append to history and reset input/logs
        async with self:
            self.logs.append("Parsing results…")
            turn = Turn(
                user=q,
                logs_text="\n".join(self.logs),
                models=processed,
                recommendation=str(result.analysis or ""),
            )
            self.turns = self.turns + [turn]
            self.running = False
            self.logs = []
            self.query = ""


# ---------- Render helpers (dark theme; no lambdas) ----------
DARK_BG = "#0b0b0b"
CARD_BG = "#14161a"
CARD_BORDER = "#2a2f3a"
TEXT = "#e5e7eb"
MUTED = "#9ca3af"
ACCENT = "#60a5fa"

def render_log_block(text: str) -> rx.Component:
    return rx.box(
        rx.text("Logs", weight="bold", color=TEXT),
        rx.text(text, color=MUTED),
        border=f"1px dashed {CARD_BORDER}",
        background=CARD_BG,
        border_radius="12px",
        padding="10px",
        width="100%",
    )

def model_card(m: Dict[str, str]) -> rx.Component:
    return rx.box(
        rx.box(
            rx.hstack(
                rx.text("🧠"),
                rx.heading(m["name"], size="6", color=TEXT),
                spacing="2",
                align="center",
            ),
            rx.link("Open model card ↗", m["source_url"], color=ACCENT, underline="always"),
            rx.divider(margin_y="8px", border_color=CARD_BORDER),
            rx.vstack(
                rx.hstack(rx.text("🎯 Task: ", color=MUTED), rx.text(m["task"], color=TEXT)),
                rx.hstack(rx.text("🧮 Params: ", color=MUTED), rx.text(m["params"], color=TEXT)),
                rx.hstack(rx.text("⚡ Latency: ", color=MUTED), rx.text(m["latency"], color=TEXT)),
                rx.hstack(rx.text("🗄️  Memory: ", color=MUTED), rx.text(m["memory_footprint"], color=TEXT)),
                rx.hstack(rx.text("📜 License: ", color=MUTED), rx.text(m["license"], color=TEXT)),
                rx.hstack(rx.text("🔓 Openness: ", color=MUTED), rx.text(m["openness"], color=TEXT)),
                rx.hstack(rx.text("🧪 Benchmarks: ", color=MUTED), rx.text(m["benchmarks_text"], color=TEXT)),
                rx.hstack(rx.text("✅ Good for: ", color=MUTED), rx.text(m["recommended_text"], color=TEXT)),
                rx.hstack(rx.text("👍 Strengths: ", color=MUTED), rx.text(m["strengths_text"], color=TEXT)),
                rx.hstack(rx.text("⚠️ Limitations: ", color=MUTED), rx.text(m["limitations_text"], color=TEXT)),
                rx.hstack(rx.text("📝 Summary: ", color=MUTED), rx.text(m["description"], color=TEXT)),
                align="start",
                spacing="1",
            ),
        ),
        border=f"1px solid {CARD_BORDER}",
        border_radius="12px",
        padding="14px",
        width="100%",
        background=CARD_BG,
    )

def render_turn(turn: Turn) -> rx.Component:
    return rx.vstack(
        rx.box(  # user message
            rx.text("You", weight="bold", color=TEXT),
            rx.text(turn.user, color=TEXT),
            border=f"1px solid {CARD_BORDER}",
            background=CARD_BG,
            border_radius="12px",
            padding="10px",
            width="100%",
        ),
        rx.cond(
            turn.logs_text != "",
            render_log_block(turn.logs_text),
        ),
        # Always render the results container; if empty, foreach yields nothing.
        rx.box(
            rx.foreach(turn.models, model_card),
            width="100%",
        ),
        rx.cond(
            turn.recommendation != "",
            rx.box(
                rx.text("Recommendation", weight="bold", color=TEXT),
                rx.text(turn.recommendation, color=TEXT),
                border=f"1px solid {CARD_BORDER}",
                background=CARD_BG,
                border_radius="12px",
                padding="10px",
                width="100%",
            ),
        ),
        spacing="3",
        width="100%",
    )

def page() -> rx.Component:
    return rx.center(
        rx.container(
            rx.vstack(
                rx.heading("AI Benchmark Evaluation Agent (Demo)", size="6", color=TEXT),
                rx.text(
                    "Type a question, click Run. Each turn is saved below so you can continue the conversation.",
                    color=MUTED,
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Ask anything (e.g., 'fast NLP models for QA')",
                        value=AppState.query,
                        on_change=AppState.set_query,
                        width="100%",
                        color=TEXT,
                        background=CARD_BG,
                        border=f"1px solid {CARD_BORDER}",
                    ),
                    rx.button(
                        rx.cond(AppState.running, rx.text("Running…", color=TEXT), rx.text("Run", color=TEXT)),
                        on_click=AppState.run_benchmark,
                        disabled=AppState.running,
                        background=CARD_BG,
                        border=f"1px solid {CARD_BORDER}",
                        border_radius="10px",
                    ),
                    width="100%",
                    spacing="3",
                ),
                rx.vstack(
                    rx.foreach(AppState.turns, render_turn),
                    spacing="5",
                    width="100%",
                ),
                spacing="5",
                width="100%",
                padding_y="2rem",
            ),
            max_width="900px",
        ),
        min_h="100vh",
        background=DARK_BG,
    )

app = rx.App()
app.add_page(page, route="/")
