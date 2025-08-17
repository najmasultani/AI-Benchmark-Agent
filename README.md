# 🕸️ AI Benchmark Agent

A web-based chatbot powered by **OpenAI GPT-4o-mini** and **Firecrawl (via MCP)**, wrapped inside a **Reflex app**. It can scrape, crawl, and extract data from websites — allowing you to ask natural questions and get real web-powered answers.

## ✨ Features
- Scrape a single web page  
- Crawl multiple pages from a site  
- Extract structured information (links, headlines, tables, etc.)  
- Chat interface built with Reflex (Python + React)  
- Powered by LangChain + LangGraph ReAct agent for reasoning + tool use  
- Built with uv (fast Python package manager)  

## 🚀 Demo
👉 Local Demo: Run it on your machine and visit [http://localhost:3000](http://localhost:3000)  
*(Cloud demo link can be added if you deploy to Vercel/Fly/Render — e.g. `https://ai-benchmark-agent.vercel.app`)*

## 🛠️ Tech Stack
- Reflex – Web framework (Python + React)  
- LangChain – LLM orchestration  
- LangGraph – ReAct agent builder  
- OpenAI – GPT-4o-mini LLM  
- MCP – Model Context Protocol for tools  
- Firecrawl – Web scraping + crawling tools  
- uv – Package/dependency manager  

## ⚙️ Setup Instructions
1. Clone the repo  
   `git clone https://github.com/najmasultani/AI-Benchmark-Agent.git && cd AI-Benchmark-Agent`  

2. Install dependencies with uv  
   `uv sync`  

3. Create a `.env` file in the project root and add:  
   ```
   OPENAI_API_KEY=your-openai-key
   FIRECRAWL_API_KEY=your-firecrawl-key
   ```  

4. Run the Reflex app  
   `uv run reflex run`  

Then open [http://localhost:3000](http://localhost:3000) in your browser.  

## 📖 Usage
- **Scraping a page** → `scrape https://example.com`  
- **Crawling multiple pages** → `crawl https://docs.python.org/3/tutorial/ depth=1`  
- **Extracting structured data** → `extract all links and their text from https://news.ycombinator.com`  
- **Reasoning + tool use** → `Find the top 3 headlines on https://www.bbc.com/news and summarize them.`  

## 📦 Project Structure
```
AI-Benchmark-Agent/
├── agent.py        # LLM + MCP + Firecrawl logic + Reflex UI
├── rxconfig.py     # Reflex config (points to agent.py)
├── .env            # API keys (ignored by git)
├── .gitignore      # Ignore secrets, cache, venv, build files
├── pyproject.toml  # uv project dependencies
└── README.md       # This file
```

## 🌍 Deployment
- Push your repo to GitHub  
- Connect it to Reflex Cloud or Vercel  
- Add environment variables:  
  - `OPENAI_API_KEY=your-openai-key`  
  - `FIRECRAWL_API_KEY=your-firecrawl-key`  
- Deploy and get your public demo link  

## 👩‍💻 Author
Built by [@najmasultani](https://github.com/najmasultani). Contributions welcome!  

## 🙏 Credits
This project was inspired and guided by a YouTube tutorial. Full credit goes to the creator for the excellent walkthrough.  
