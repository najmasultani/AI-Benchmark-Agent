from dotenv import load_dotenv
from src.workflow import Workflow

load_dotenv()


def main():
    workflow = Workflow()
    print("AI Benchmark Evaluation Agent")

    while True:
        query = input("\n🔍 Benchmark Query (e.g., 'fast NLP models for QA'): ").strip()
        if query.lower() in {"quit", "exit"}:
            break

        if query:
            result = workflow.run(query)
            print(f"\n📊 Results for: {query}")
            print("=" * 60)

            for i, m in enumerate(result.models, 1):
                print(f"\n{i}. 🧠 {m.name}")
                print(f"   🔗 Source: {m.source_url}")
                if m.task:
                    print(f"   🎯 Task: {m.task}")
                if m.params:
                    print(f"   🧮 Params: {m.params}")
                if m.latency:
                    print(f"   ⚡ Latency: {m.latency}")
                if m.memory_footprint:
                    print(f"   🗄️  Memory: {m.memory_footprint}")
                if m.license:
                    print(f"   📜 License: {m.license}")
                if m.openness:
                    print(f"   🔓 Openness: {m.openness}")
                if m.benchmarks:
                    top = ", ".join([f"{k}: {v}" for k, v in list(m.benchmarks.items())[:5]])
                    print(f"   🧪 Benchmarks: {top}")
                if m.recommended_usage:
                    print(f"   ✅ Good for: {', '.join(m.recommended_usage[:4])}")
                if m.strengths:
                    print(f"   👍 Strengths: {', '.join(m.strengths[:3])}")
                if m.limitations:
                    print(f"   ⚠️ Limitations: {', '.join(m.limitations[:3])}")
                if m.description and m.description != "Analysis failed":
                    print(f"   📝 Summary: {m.description}")

            if result.analysis:
                print("\nRecommendation:")
                print("-" * 40)
                print(result.analysis)


if __name__ == "__main__":
    main()
