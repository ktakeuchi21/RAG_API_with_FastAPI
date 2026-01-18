import chromadb

client = chromadb.PersistentClient(path="./db")
collection = client.get_or_create_collection("docs")

with open("kb.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["kb"])

print("Embedding stored in Chroma")
