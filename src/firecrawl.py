import os
from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()


class FirecrawlService:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("Missing FIRECRAWL_API_KEY environment variable")
        self.app = FirecrawlApp(api_key=api_key)

    def search_models(self, query: str, num_results: int = 5):
        """
        Prioritize model-centric sources: Hugging Face, Papers with Code, ArXiv, GitHub.
        """
        try:
            return self.app.search(
                query=(
                    f'{query} model benchmark '
                    f'site:huggingface.co OR site:paperswithcode.com OR site:arxiv.org OR site:github.com'
                ),
                limit=num_results,
                scrape_options=ScrapeOptions(formats=["markdown"])
            )
        except Exception as e:
            print(e)
            return None

    def scrape_page(self, url: str):
        try:
            return self.app.scrape_url(url, formats=["markdown"])
        except Exception as e:
            print(e)
            return None
