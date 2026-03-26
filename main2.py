from fastapi import FastAPI

app = FastAPI()

lista_de_produtos = [
    {"Nome": "Teclado Gamer", "Preço": 1569.99},
    {"Nome": "Cadeira", "Preço": 340.74},
    {"Nome": "Setup Gamer", "Preço": 3598.76},
    {"Nome": "Tenis Nike", "Preço": 299.99},
    {"Nome": "Caderno Inteligente", "Preço": 98.99},
    {"Nome": "MousePad", "Preço": 30.97},
    {"Nome": "Ventilador", "Preço": 75.15},
    {"Nome": "Mouse", "Preço": 35.45},
    {"Nome": "Notebook", "Preço": 1200.52}
]
@app.get('/')

def inicio():
    return {
        "Mensagem": "Seja muito bem-vindo",
        "AVISO": "Para ir para sua lista, Coloque uma (/) logo na frente do seu URL e escreva produtos"
    }
@app.get('/produtos')
def produtos():
    return {
        "Mensagem": "Listando seus produtos",
        "Listagem": lista_de_produtos,
        "AVISO": "Para filtrar prdotuso por indice, Coloque mais um (/) Logo a frente de produtos e coloque um numero de 0 a 8"
    }

@app.get('/produtos/{id}')
def listar_produtos(id: int):
    return {
        "Mensagem": f"Aqui está o produto do id:{id}",
        "Produto": lista_de_produtos[id]
    }
@app.post('/produtos')
def criar_produto(novos_produtos: list[dict]):
    lista_de_produtos.append(novos_produtos)

    return {
        "mensagem": "Produto adicionado com sucesso!!",
        "AVISO": "Caso queira confirmar reinicie a pagina"
    }
