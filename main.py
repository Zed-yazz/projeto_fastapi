from fastapi import FastAPI

app = FastAPI()

lista_de_produtos = [
    {"Nome": "Teclado Gamer", "Preço": 1569.99},
    {"Nome": "Cadeira", "Preço": 340.74},
    {"Nome": "Setup Gamer", "Preço": 3598.76},
    {"Nome": "Tenis Nike", "Preço": 299.99},
    {"Nome": "Caderno Inteligente", "Preço": 98.99}
]
@app.get("/produtos")
def lista_produtos():
    return {
        "mensagem": "Seja muito bem vindo!",
        "Estoque": lista_de_produtos,
        "AVISO": "Caso queira procurar um produto especifico, Coloque no seu URL uma (/) an frente de produtos,"
                 "e escolha umd ID, Comaçando a partir do Zero"
    }
@app.get('/produtos/{id}')
def exibir_produto(id: int):
    return {
        "Mensagem": f"Aqui esta o produto do ID:{id}",
        "Produto": lista_de_produtos[id]
    }

