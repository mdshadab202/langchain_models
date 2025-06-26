# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

# from dotenv import load_dotenv

# load_dotenv()

# llm =HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task='text-generation'
    
# )

# model =ChatHuggingFace(llm=llm)

# result= model.invoke("what is the capital of iraq")

# print(result.content)

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Create the underlying endpoint first
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational"
)

# Now wrap it in ChatHuggingFace
chat_model = ChatHuggingFace(llm=llm,temperature = 1.0,max_completion_tokens=10)

# Send a prompt
response = chat_model.invoke([
    HumanMessage(content="Give only the name of the capital city of India")
])

print(response.content)
