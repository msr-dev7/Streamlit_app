import streamlit as st
import speech_recognition as sr
from langchain.llms import OpenAI
from gtts import gTTS
import os

openai_api_key = st.sidebar.text_input('Chave da API OpenAI', type = 'password')
llm = OpenAI(api_key=openai_api_key, temperature = 0)
# Função para reconhecimento de fala
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Fale algo...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')  # STT para texto
            return text
        except sr.UnknownValueError:
            return "Desculpe, não entendi o áudio."
        except sr.RequestError:
            return "Não foi possível acessar o serviço de reconhecimento de fala."

# Função para interagir com o ChatGPT
def chat_with_gpt(prompt):
    try:
        saida = llm(prompt)
        return saida
    except Exception as e:
        return f"Erro ao interagir com o modelo: {str(e)}"

# Função para síntese de voz
def text_to_speech(text):
    tts = gTTS(text=text, lang='pt-br')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

# Interface do Streamlit
st.header("Chat por Voz")

# Botão para iniciar a interação por voz
c0,_,c1 = st.columns(3)
with c0:
    inicio = st.button("Iniciar Interacao por Voz")
with c1:
    stop_button = st.button("Encerrar Conversa", key="encerrar_conversa")            

# Antes do loop while
conversa = []  # Lista para armazenar o histórico da conversa
interagindo = False  # Variável de controle para interação

# Durante a interação
if inicio:
    interagindo = True

while interagindo:
    input_text = recognize_speech()
    if input_text and "Desculpe, não entendi o áudio." not in input_text:
        conversa.append(("Usuário:", input_text))  # Adiciona entrada do usuário ao histórico
        st.write("Usuário:", input_text)
        response_text = chat_with_gpt(input_text)
        conversa.append(("ChatGPT:", response_text))  # Adiciona resposta do modelo ao histórico
        st.write("ChatGPT:", response_text)
        if "Erro ao interagir com o modelo" not in response_text:
            text_to_speech(response_text)
            st.audio("response.mp3")
    else:
        st.write("Não foi detectado texto na fala. Por favor, fale novamente.")
    
    if stop_button:
        interagindo = False  # Encerra a interação

# Após o encerramento da conversa
st.write("Histórico da Conversa:")
for entry in conversa:
    if "ChatGPT:" in entry[0]:  # Verifica se é uma resposta do modelo para formatar a exibição
        st.text(entry[0] + " " + entry[1])
    else:
        st.write(entry[0], entry[1])  # Mostra entrada do usuário
            
