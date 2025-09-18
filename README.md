Sistema de Gerenciamento de Loja de Automóveis
Uma aplicação web completa desenvolvida em Django para gerenciar o catálogo de veículos de uma concessionária. O projeto é integrado com a API da OpenAI para gerar descrições de veículos de forma inteligente.

📸 Demonstração do Projeto
<img width="1637" height="784" alt="image" src="https://github.com/user-attachments/assets/41054d7c-e3af-4f9b-87eb-2496fc33abad" />


✨ Funcionalidades
Gerenciamento Completo de Veículos (CRUD):

Cadastrar: Adicionar novos carros ao catálogo.

Visualizar: Listar todos os carros com seus detalhes.

Atualizar: Editar as informações de veículos existentes.

Deletar: Remover carros do sistema.

🪄 Geração de Descrição com IA: Integrado com a API da OpenAI. Se o usuário não fornecer uma descrição ao cadastrar um novo carro, o sistema gera automaticamente um texto de marketing atraente com base na marca, modelo e ano do veículo.

Busca e Filtro: Mecanismos para encontrar veículos específicos no catálogo.

Páginas Dinâmicas: Interface construída com HTML/CSS e renderizada pelo backend do Django.

Painel Administrativo: Utiliza o Django Admin para um gerenciamento de dados robusto e seguro.

💻 Tecnologias Utilizadas
Backend: Python, Django

Frontend: HTML5, CSS3, Django Template Language

Banco de Dados: SQLite (padrão de desenvolvimento)

Integrações: API da OpenAI

🚀 Instalação e Configuração
Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

Pré-requisitos
Git

Python 3.10+

Passos
1. Clone o repositório:

Bash

git clone https://github.com/pedropauloramosmendes19-debug/projeto_carros.git
cd projeto_carros
2. Crie e ative um ambiente virtual (venv):

Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para Linux/macOS
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências do projeto:
(Se você não tiver um arquivo requirements.txt, pode criá-lo com o comando pip freeze > requirements.txt)

Bash

pip install -r requirements.txt
4. Configure as variáveis de ambiente:
Crie um arquivo chamado .env na raiz do projeto. Este arquivo é crucial e deve conter sua SECRET_KEY do Django e sua chave da API da OpenAI.

Ini, TOML

# Exemplo de arquivo .env

# Configurações do Django
SECRET_KEY='sua-chave-secreta-super-forte-aqui'
DEBUG=True

# Chave da API da OpenAI (Obrigatória para a geração de descrição)
OPENAI_API_KEY='sk-sua-chave-da-api-da-openai-aqui'
5. Aplique as migrações do banco de dados:

Bash

python manage.py migrate
6. Crie um superusuário:
Isso permitirá que você acesse a área administrativa do Django em /admin.

Bash

python manage.py createsuperuser
▶️ Executando o Projeto
Após a instalação, inicie o servidor de desenvolvimento:

Bash

python manage.py runserver
A aplicação estará disponível em http://127.0.0.1:8000/.

📄 Licença
Este projeto está sob a licença MIT.

👨‍💻 Autor
Feito com ❤️ por Pedro Paulo Ramos Mendes
