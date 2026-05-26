from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="FitHub API", description="Backend do catálogo de acessórios fitness")

# permite que o Frontend React acesse a API tranquilamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# simulação de banco de dados de produtos fitness
PRODUCTS = [
    {"id": 1, "name": "Cinto Lombar de Couro", "price": 149.90, "category": "Musculação"},
    {"id": 2, "name": "Faixa Elástica (Theraband)", "price": 45.00, "category": "Funcional"},
    {"id": 3, "name": "Strap de Pegada Profissional", "price": 39.90, "category": "Musculação"},
    {"id": 4, "name": "Corda de Pular de Alta Velocidade", "price": 59.90, "category": "Cardio"}
]

@app.get("/")
def read_root():
    return {"status": "FitHub API rodando com sucesso!"}

@app.get("/api/products")
def get_products():
    return PRODUCTS
@app.get("/api/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return product
    # Retorna erro 404 se o produto não existir
    raise HTTPException(status_code=404, detail="Produto não encontrado no FitHub")