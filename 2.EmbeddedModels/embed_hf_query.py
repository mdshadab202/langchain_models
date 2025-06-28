from langchain_huggingface import HuggingFaceEmbeddings


embedding= HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')

text = "HI my name is shadab ali i'm from noida currently i'm doing internship in cognifyz"


vector =embedding.embed_query(text)

print(str(vector))