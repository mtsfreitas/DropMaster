from flask import Flask, request, render_template, send_file
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Carregando o modelo e o LabelEncoder
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    le = pickle.load(f)

# Inicializando um DataFrame para armazenar as previsões
predictions = pd.DataFrame(columns=['Ano', 'Mês', 'ID do Produto', 'ID da Categoria do Produto', 'Quantidade recomendada', 'Preço Recomendado'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = int(request.form['year'])
    month = int(request.form['month'])
    item_id = int(request.form['item_id'])
    item_category_id = le.transform([int(request.form['item_category_id'])])[0]

    product_input = pd.DataFrame({
        'year': [year],
        'month': [month],
        'item_id': [item_id],
        'item_category_id': [item_category_id]
    })

    predicted_output = model.predict(product_input)

    quantity_recommended = predicted_output[0][0]
    price_recommended = predicted_output[0][1]
    revenue_estimated = quantity_recommended * price_recommended

    # Adicionando a previsão ao DataFrame
    global predictions
    new_row = pd.DataFrame({
        'Ano': [year],
        'Mês': [month],
        'ID do Produto': [item_id],
        'ID da Categoria do Produto': [item_category_id],
        'Quantidade recomendada': [quantity_recommended],
        'Preço Recomendado': [price_recommended],
        'Receita Estimada': [revenue_estimated]
    })
    predictions = pd.concat([predictions, new_row], ignore_index=True)

    # Calculando a receita estimada considerando todos os valores na tabela
    total_revenue_estimated = predictions['Receita Estimada'].sum()

     # Verificando se o diretório static existe, se não, cria um
    if not os.path.exists('static'):
        os.makedirs('static')

    # Gerando o gráfico e salvando como imagem
    plt.figure(figsize=(10,6))
    plt.plot(predictions['Quantidade recomendada'], predictions['Preço Recomendado'] + 0.5, 'o-')
    for i in range(len(predictions['Preço Recomendado'])):
        plt.text(predictions['Quantidade recomendada'].iat[i], predictions['Preço Recomendado'].iat[i] + 0.5, "{:.2f}".format(predictions['Preço Recomendado'].iat[i]), verticalalignment='bottom')
    plt.title('Previsões de Quantidade recomendada vs Preço Recomendado')
    plt.xlabel('Quantidade recomendada')
    plt.ylabel('Preço Recomendado')
    plt.grid(True)
    plt.savefig('static/plot.png')
    
    return render_template('index.html',
                           prediction_quantity='Quantidade recomendada: {:.2f}'.format(quantity_recommended),
                           prediction_price='Preço recomendado: {:.2f}'.format(price_recommended),
                           total_revenue='Receita total estimada: {:.2f}'.format(total_revenue_estimated),
                           predictions=predictions.to_html())




@app.route('/plot')
def plot():
    return render_template('plot.html')

@app.route('/pie_plot')
def pie_plot():
    # Verificando se o diretório static existe, se não, cria um
    if not os.path.exists('static'):
        os.makedirs('static')

    # Gerando o gráfico de pizza e salvando como imagem
    plt.figure(figsize=(10,6))
    plt.pie(predictions['Receita Estimada'], labels = predictions['ID do Produto'], autopct='%1.1f%%')
    plt.title('Receita Estimada por Produto')
    plt.savefig('static/pie_plot.png')

    return render_template('pie_plot.html')

@app.route('/download')
def download():
    # Escrevendo o DataFrame para um arquivo .csv
    predictions.to_csv('predictions.csv', index=False)
    return send_file('predictions.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
