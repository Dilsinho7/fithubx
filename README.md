# FitHub 🏋️‍♂️

O **FitHub** é uma aplicação web funcional projetada para o gerenciamento e exibição de um catálogo de acessórios fitness de alto desempenho. O foco principal deste projeto é demonstrar a aplicação prática de conceitos de DevOps, conteinerização e integração contínua.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python (FastAPI)
- **Frontend:** React.js (Vite)
- **Infraestrutura & DevOps:** Docker, GitHub Actions

## 👥 5. Membros da Squad
Adilson Peddro Ferreira Cavalcanti Filho - 01751877;
Alexsandro Souza do Nascimento - 01750424;
Alex Johny Santos da Silva - 01124089;

## 📦 Como Rodar o Projeto via Docker

Certifique-se de ter o Docker instalado em sua máquina.

### 1. Clonar o Repositório
```bash
git clone https://github.com/Dilsinho7/fithubx

# 1. Navegue até a pasta do backend
cd backend

# 2. Construa a imagem Docker (Atenção ao ponto final!)
docker build -t fithub-backend .

# 3. Inicialize o container mapeando as portas de comunicação
docker run -d -p 8000:8000 --name fithub-api fithub-backend

Subir o frontend:

# 1. Navegue até a pasta do frontend
cd frontend

# 2. Construa a imagem Docker do frontend (Atenção ao ponto final!)
docker build -t fithub-frontend .

# 3. Inicialize o container na porta padrão da web (Porta 80)
docker run -d -p 80:80 --name fithub-web fithub-frontend

Comandos úteis de Gerenciamento Docker:
Ver se os containers estão rodando: docker ps
Parar a aplicação temporariamente: docker stop fithub-api fithub-web
Ligar a aplicação novamente: docker start fithub-api fithub-web
Remover os containers para refazer o build: docker rm -f fithub-api fithub-web
