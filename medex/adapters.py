try:
    from MEDEX_FINAL import build_full_pipeline as _build_full_pipeline  # ejemplo
except ImportError:
    _build_full_pipeline = None

try:
    from medical_rag_system import answer as _legacy_answer  # ejemplo
except ImportError:
    _legacy_answer = None

def build_pipeline():
    if _build_full_pipeline is None:
        raise RuntimeError("No se encontró build_full_pipeline en MEDEX_FINAL.py. Ajusta adapters.py.")
    return _build_full_pipeline()

def answer_query(pipeline, query: str, mode: str = "educational"):
    if _legacy_answer is None:
        raise RuntimeError("No se encontró answer en medical_rag_system.py. Ajusta adapters.py.")
    return _legacy_answer(pipeline, query=query, mode=mode)
