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

@app.post('/produtos')
def criar_produtos(novos_produtos: list[dict]):
    lista_de_produtos.extend(novos_produtos)

    return {
        "Mensagem": "Produtos novos adicionados com sucesso!",
        "AVISO": "Caso queira confirmar reinicie a pagina"
    }

@app.get('/')
def inicio():
    return {
        "Mensagem": "Seja muito Bem-Vindo",
        "AVISO": "Para ir para sua lista, Coloque uma (/) logo na frente do seu URL e escreva produtos"
    }
@app.get('/produtos')
def produtos():
    return {
        "Mensagem": "Listando seus Produtos",
        "Lista": lista_de_produtos,
        "AVISO": "Para filtrar produtos por indice, Coloque mais um (/) Logo a frente de produtos e coloque um numero de 0 a 8"
    }
@app.get('/produtos/{id}')
def listar_produtos(id: int):
    return {
        "Mensagem": f"Aqui esta o do ID:{id}",
        "Lista": lista_de_produtos[id]
    }

@app.put('/produtos/{id}')
def atualizar_itens(id: int, item_atualizado: dict):
    lista_de_produtos[id] = item_atualizado
    return {
        "Mensagem": "Item Atualizado com Sucesso",
        "AVISO": item_atualizado
    }
@app.delete('/produtos/{id}')
def deletar_item(id: int):
    item_deletado = lista_de_produtos.pop(id)
    return {
        "AVISO": f"O Seguinte ITEM: {item_deletado}, referente ao ID: {id} Esta sendo excluido da lista permanentemente"
    }