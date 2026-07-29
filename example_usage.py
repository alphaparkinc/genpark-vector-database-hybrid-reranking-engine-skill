from client import VectorDatabaseHybridRerankingEngineClient

def main():
    client = VectorDatabaseHybridRerankingEngineClient()
    res = client.rerank_hybrid_search("How to improve RAG accuracy?", 2)
    print(f"Reciprocal Rank: {res['reciprocal_rank']}")
    for r in res["reranked_results"]:
        print(f"  [{r['doc_id']}] Score: {r['score']} | {r['snippet']}")

if __name__ == "__main__":
    main()
