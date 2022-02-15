import pandas as pd 
from flask import Flask, jsonify 

app = Flask(__name__)   


@app.route('/')  
def homepage():  
    return 'Essa é a homepage do site'


@app.route('/pegarvendas')
def pegar_vendas():
    table = pd.read_csv('Criando-API-no-Python.csv') 
    total_vendas = table['Vendas'].sum()  
    resposta = {'total de vendas': total_vendas}  
    return jsonify(resposta) 


app.run()