from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o",temperature = 1.0,max_completion_tokens=10)

result = model.invoke("give me a poem on sun")

print(result.content)

