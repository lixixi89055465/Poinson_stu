#安装包:langchain-tavily
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv("openai.env")
tool = TavilySearch(max_results = 2)
result = tool.invoke("今天几号?")
print(result)

