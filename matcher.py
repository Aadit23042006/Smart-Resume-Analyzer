from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity



model=SentenceTransformer(
"all-MiniLM-L6-v2"
)



def match_resume_job(
resume,
job
):


    r=model.encode(resume)

    j=model.encode(job)


    score=cosine_similarity(
    [r],
    [j]
    )


    return round(
    score[0][0]*100,
    2
    )