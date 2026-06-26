from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer(
"all-MiniLM-L6-v2"
)



def create_vector_database(text):

    chunks=[]

    size=500


    for i in range(0,len(text),size):

        chunks.append(
        text[i:i+size]
        )


    vectors=model.encode(chunks)


    index=faiss.IndexFlatL2(
        vectors.shape[1]
    )


    index.add(
        np.array(vectors)
    )


    return index,chunks