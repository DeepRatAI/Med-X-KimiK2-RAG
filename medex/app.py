from medex.adapters import build_pipeline, answer_query

def run_once(query: str, mode: str = "educational") -> str:
    pipe = build_pipeline()
    return answer_query(pipe, query=query, mode=mode)
