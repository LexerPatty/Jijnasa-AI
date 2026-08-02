from tools.tools import web_search , scrape_url
from pipeline import run_research_pipeline

# result = web_search.invoke("What is the latest news on AI?")
# print(result)

# scraped_content = scrape_url.invoke("https://tech.yahoo.com/ai")
# print(scraped_content)


topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)