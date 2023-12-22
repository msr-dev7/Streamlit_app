import streamlit as st


st.set_page_config(
    page_title="Sobre",
    page_icon="\u2B50",
    layout="wide",
    initial_sidebar_state="expanded")

def main():

    st.header('SENAI CIMATEC')
    st.header('ESPECIALIZAÇÃO EM DATA SCIENCE & ANALYTICS')
    st.markdown("---")
    st.title('Machine Learning Hands On')
    st.write("""
    Equipe:
    - Cleidiane de Souza Santos Xavier
    - Isabela Almeida Marinho da Silveira
    - Mônica Silva Rivas
    """)

    st.markdown("---")

    
if __name__ == "__main__":
    main()
