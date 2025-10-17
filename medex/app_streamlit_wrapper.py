"""
MedeX Streamlit Wrapper (Optional Integration Example)

This file demonstrates how the medex package can be integrated with Streamlit,
but is NOT used by the existing streamlit_app.py which continues to work
as before without any modifications.

This is purely for demonstration and future integration purposes.
"""

from medex.app import run_once


def run_streamlit_query(query: str, mode: str = "educational") -> str:
    """
    Wrapper function that can be called from a Streamlit app.
    
    Example usage in a new Streamlit app:
    
    ```python
    import streamlit as st
    from medex.app_streamlit_wrapper import run_streamlit_query
    
    st.title("MedeX Medical AI")
    
    query = st.text_input("Enter your medical query:")
    mode = st.selectbox("Mode:", ["educational", "professional"])
    
    if st.button("Ask MedeX"):
        with st.spinner("Processing..."):
            response = run_streamlit_query(query, mode)
            st.write(response)
    ```
    
    Args:
        query: Medical query string
        mode: Query mode - "educational" or "professional"
    
    Returns:
        str: Generated response
    """
    return run_once(query, mode=mode)


# Example of how to adapt the existing streamlit_app.py to use the package
# (This is just documentation, NOT actual code that runs)
INTEGRATION_EXAMPLE = """
# Optional future integration with existing streamlit_app.py:
# 
# Instead of:
#     from MEDEX_FINAL import MedeXv2583
#     medex = MedeXv2583()
#     response = await medex.generate_response(query)
# 
# You could use:
#     from medex.app import run_once
#     response = run_once(query, mode="educational")
# 
# However, the existing streamlit_app.py continues to work as-is
# with NO modifications required.
"""
