import streamlit as st

st.set_page_config(
    page_title="Machine Learning Hands On",
    page_icon="\u2B50",
    layout="wide",
    initial_sidebar_state="expanded")

st.header('SENAI CIMATEC')
st.header('ESPECIALIZAÇÃO EM DATA SCIENCE & ANALYTICS')
st.markdown("---")
st.title('Machine Learning Hands On')

st.markdown("---")


# Texto de introdução
st.markdown("""
## 

**Detalhamento do WebApp Streamlit:**

**- Deploy do modelo 1 e do modelo 2 de Machine Learning para doenças cardíacas**

O usuário deve informar os dados solicitados da pessoa e clicar no botão da aplicação que realizará previsões 
sobre o risco de doenças cardíacas. Este recurso utiliza um modelo de machine learning avançado, alimentado por 
características e dados pessoais, treinado com uma vasta gama de informações médicas.

**- Chatbot com um assistente que conversará sobre a história do Brasil** 

Para realizar apenas uma simples conversa com o assistente, o usuário deve informar apenas a chave da API OpenAI.

Para utilizar o conhecimento de um arquivo PDF, o usuário deve informar a chave da API OpenAI, a chave do Pinecone e um arquivo PDF com dados mais recentes da história do Brasil.
Como sugestão temos o [PDF Retrospectiva de 2023](https://drive.google.com/file/d/117PS69h2xIQ1K7S0x8JIoy0ABKioJwy2/view?usp=sharing), que foi extraído do site [Startupi](https://startupi.com.br/retrospectiva-2023/).

É possível ainda configurar diretamente no aplicativo o nível de criatividade, o tamanho e o estilo das respostas do assistente virtual. 
Ao finalizar a conversa clicando diretamente no botão específico, o usuário obterá todo o histórico conversado em um arquivo PDF, 
disponibilizado para download na aplicação.

**- Chat por voz - Bônus**

O usuário deve clicar no botão específico para iniciar a interação por voz, realizar o diálogo por voz com o assistente e, quando desejar, 
finalizar o diálogo clicando no botão específico.

**- Sobre**

Dados básicos do curso e da equipe. 

""")

st.markdown("---")
