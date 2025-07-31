from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []
    def add_document(self, text):
        # Split into smaller chunks
        chunks = self._split_text(text)
        embeddings = self.model.encode(chunks)
        self.documents.extend(chunks)

        if self.index is None:
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def search(self, query, top_k=1):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), top_k)
        results = [self.documents[i] for i in indices[0]]
        return results

    def _split_text(self, text, chunk_size=500):
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
