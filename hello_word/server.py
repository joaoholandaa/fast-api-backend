from lib2to3.pytree import Base
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
def home():
    return {"mensagem":"Olá FastAPI, backend!"}

@app.get('/profile')
def profile():
    return {"nome":"Holanda"}

@app.get('/saudacao/{nome}') 
def saudacao(nome: str):
    texto = f'Olá {nome}, tudo em paz?'
    return {"mensagem": texto}

@app.get('/area-retangulo')
def area_retangulo(largura: int, altura: int = 2):
    area = largura * altura
    return {'area': area}

class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso!'}