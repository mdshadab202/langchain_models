from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


embedding= OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

document=[

"hi i'm shadab from saharanpur",
"and currently i'm doing MBA in AI and ML",
"and i have had a degree og graduation in mathematics"
]

result= embedding.embed_documents(document)


print(str(result))