import streamlit as st 
import pandas as pd
import numpy as np
from pycaret.regression import load_model, predict_model
from pycaret.datasets import get_data

dados = get_data('heart_disease')
dados.rename(columns=lambda x: x.strip(), inplace=True)
modelo = load_model('recursos/modelo-previsao-heart-disease')

def trad(x):
	return 'Masculino' if x == '1' else 'Feminino'

def trad2(x):
	return 'Não' if x == '0' else 'Sim'

st.header('Modelo de Previsão de Doença do Coração')

st.divider()

st.write('Entre com as características da pessoa:')

#Widgets para fazer os inputs do modelo

col0, col1, col2, col3 = st.columns([3,3,3,3])

with col0:
	age = st.slider(label = 'Idade', 
		min_value=29, 
		max_value=77, 
		value= 50, 
		step=1)
		
	st.markdown("---")			
		
	chest = st.selectbox(label = 'Tipo de dor no peito', 
		options = sorted(dados['chest pain type'].unique()))
		
	st.markdown("---")	
	
		
	number = st.selectbox(label = 'Número de vasos principais', 
		options = sorted(dados['number of major vessels'].unique()))
		
with col1:
	sex	= st.radio('Sexo', ['1', '0'], format_func = trad)
	
	st.markdown("---")	

	fasting = st.radio('Açúcar no sangue em jejum > 120 mg/dl', ['0', '1'], format_func = trad2)
	
	st.markdown("---")	
			
	exercise = st.radio('Angina induzida por exercício', ['0', '1'], format_func = trad2)
	
with col2: 
		
	electrocardiographic = st.selectbox(label = 'Resultados eletrocardiográfico em repouso', 
		options = sorted(dados['resting electrocardiographic results'].unique()))
		
	st.markdown("---")	
		
	slope = st.selectbox(label = 'Inclinação do pico do segmento ST do exercício', 
		options = sorted(dados['slope of peak'].unique()))
		
	st.markdown("---")	
		
	thal = st.selectbox(label = 'Thal', 
		options = sorted(dados['thal'].unique()))
		
with col3:
	resting	= st.number_input(label = 'Pressão arterial em repouso', 
		min_value = 94, 
		max_value = 200, 
		value = 130, 
		step = 1)	
		
	st.markdown("---")	
		
	heart = st.number_input(label = 'Frequência cardíaca máxima alcançada', 
		min_value = 71, 
		max_value = 202, 
		value = 153, 
		step = 1)	
		
	st.markdown("---")	
		
	serum = st.number_input(label = 'Colesterol sérico em mg/dl', 
		min_value = 126, 
		max_value = 564, 
		value = 245, 
		step = 1)
		
	st.markdown("---")	
	
	oldpeak	= st.number_input(label = 'Pico antigo', 
		min_value = 0., 
		max_value = 6.2, 
		value = 0.8, 
		step = 0.1)
		
st.divider()
				
#Criar um DataFrame com os inputs exatamente igual ao dataframe em que foi treinado o modelo
aux = {'age': [age],
	   'sex': [sex],
	   'chest pain type': [chest],
	   'resting blood pressure': [resting],
	   'serum cholestoral in mg/dl': [serum],
	   'fasting blood sugar > 120 mg/dl': [fasting],
	   'resting electrocardiographic results': [electrocardiographic],
	   'maximum heart rate achieved': [heart],
	   'exercise induced angina': [exercise],
	   'oldpeak': [oldpeak],
	   'slope of peak': [slope],
	   'number of major vessels': [number],
	   'thal': [thal]}
	   
prever = pd.DataFrame(aux)

st.write(prever)

st.divider()

#Usar o modelo salvo para fazer previsao nesse Dataframe

_, c1, _ = st.columns([2,3,1])

with c1:
	botao = st.button('Previsão de ter doença coração',
		type = 'primary',
		use_container_width = True)

if botao:
	previsao = predict_model(modelo, data = prever)
	valor = previsao.loc[0,'prediction_label']
	
	if valor > 0:
		st.write('Cuidado! É necessário procurar um cardiologista.')
	else:
		st.write('Parabéns! Suas taxas estão dentro da normalidade.')
		st.balloons()
