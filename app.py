import streamlit as st

st.set_page_config(
    page_title="Trabalho final da disciplina Machine Learning Hands On",
    page_icon="\u2B50",
    layout="wide",
    initial_sidebar_state="expanded")


st.title('Trabalho final da disciplina Machine Learning Hands On')

# Texto de introdução
st.markdown("""
## 
Reunir em um WebApp Streamlit as tarefas solicitadas em aula, isto é, esse WebApp deve conter as seguintes páginas:

- O deploy de pelo menos um modelo de Machine Learning (vocês fizeram nas aulas passadas).
- O chatbot com um assistente definido por vocês e com as características solicitadas no exercício. 
- Uma página 'Sobre', com os nomes dos envolvidos na criação do app e informações adicionais que julgarem pertinentes.

Capriche e descreva toda a funcionalidade do seu WebApp para o usuário! 

Utilize com criatividade os recursos do Streamlit. Deixe seu app pronto para que um usuário qualquer possa utilizá-lo!

O trabalho pode ser feito em grupo de até 3 pessoas.

Submeter o trabalho no link de submissão: https://forms.gle/s1cADrEATWjcmcVt6


Assistente Virtual:

Crie um assistente pessoal com instruções específicas para um problema de sua escolha. 
Inclua opções ao usuário para controlar a criatividade da resposta, o tamanho da resposta e o estilo de escrita da resposta. 
Adicione mais, ou outras, opções como widgets de interação com usuário se desejar.

No uso do assistente, inclua um escape de moderação, isto é, caso o input do usuário violar as regras (você define), 
uma resposta automática deve ser dada, ao invés de acionar a API de chat.

Faça com que o programa tenha uma opção para 'finalizar a conversa' e quando isso acontecer, um conjunto de dados (pandas mesmo) 
deve ser alimentado com as seguintes informações: dia e horário da conversa, tokens utilizados na conversa, custo estimado da conversa, 
histórico do diálogo.

Além disso, gere um arquivo em PDF com o histórico da conversa e permita ao usuário baixar esse arquivo.

Complemento: adicione o modo RAG na conversa, isto é, permita ao usuário subir um arquivo de texto e que a informação do arquivo seja 
levada em consideração na conversa com o chatbot. 

Exercício Bônus [NÃO OBRIGATÓRIO] - Crie um app para interagir por voz com o ChatGPT
""")
