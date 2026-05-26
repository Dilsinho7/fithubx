from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS para o Frontend conseguir conversar com o Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# O "Banco de Dados" temporário
products_db = [
    {"id": 1, "name": "Cinto de Musculação", "description": "Proteção lombar para agachamentos.", "price": 120.00},
    {"id": 2, "name": "Faixa de Joelho", "description": "Estabilidade para cargas altas.", "price": 85.50},
    {"id": 3, "name": "Straps", "description": "Melhora a pegada no levantamento terra.", "price": 45.00},
]

@app.get("/")
def read_root():
    return {"status": "FitHub API rodando com sucesso!"}

# Rota 1: Lista todos os produtos
@app.get("/api/products")
def get_products():
    return products_db

# Rota 2: Busca um produto específico pelo ID
@app.get("/api/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    # Se o loop terminar e não achar o ID, dispara erro 404
    raise HTTPException(status_code=404, detail="Produto não encontrado no FitHub")