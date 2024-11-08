# Exercício Integrado de Orientação a Objetos, Programação Funcional, RPA com BotCity, Arquivos Binários e Tratamento de Exceções

Este projeto simula a gestão de pedidos de uma loja virtual fictícia utilizando Python. Ele aplica conceitos de programação orientada a objetos, programação funcional, automação com BotCity e manipulação de arquivos em formatos JSON e binário. 

### Estrutura do Projeto

```bash
Automacao-de-Pedidos-com-Python-e-BotCity/
│
├── app.py                    # Arquivo principal da API (Flask) para cadastro e listagem de pedidos.
├── bot.py                    # Arquivo responsável pela automação do preenchimento de formulários com BotCity.
├── main.py                   # Arquivo com o código de execução do programa.
├── core/
│   ├── produto.py            # Define a classe Produto.
│   ├── pedido.py             # Define a classe Pedido.
│   ├── Gestao_pedidos.py     # Define a classe GestorDePedidos
│   ├── manipulacaoArquivo.py # Responsável pela manipulação de arquivos JSON e binários.
│   └── excecao.py            # Define exceções personalizadas.
├── data/
│   ├── pedidos.json          # Arquivo JSON para persistência de dados de pedidos.
│   ├── pedidos.pkl           # Arquivo pkl gerado.
│   ├── pedidos.csv           # Arquivo CSV de exemplo para importar pedidos.
│   └── pedidos.xlsx          # Arquivo XLSX de exemplo para importar pedidos.
├── templates/
│   ├── formulario.html       # Formulário para cadastro de pedidos.
│   ├── listagem.html         # Listagem dos pedidos cadastrados.
├   └── resultado.html        # Exibe o resultado do pedido cadastrado.
├── requirements.txt          # Arquivo com as dependências do projeto.
└── README.md                 # Este arquivo com instruções do projeto.

```

## Instalação

### Instalação do Ambiente

1. **Crie um ambiente Conda** (se ainda não existir):

   ```bash
   conda create --name botPedidos python=3.10.14
   ```

2. **Ative o ambiente Conda**:

   ```bash
   conda activate botPedidos
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Se precisar refazer o ambiente Conda**, você pode excluir o ambiente e repetir os passos acima:

   ```bash
   conda remove --name botPedidos --all
   ```

### Como Usar a API (`app.py`)

1. **Instalação das Dependências**:
   Instale todas as dependências necessárias com o comando:
   ```bash
   pip install -r requirements.txt
   ```

3. **Atualização do `pip`**:
   Se necessário, atualize o `pip` para garantir que você tenha a versão mais recente:
   ```bash
   pip install --upgrade pip
   ```

4. **Rodando a API**:
   Após configurar o ambiente, execute o arquivo `app.py` para iniciar o servidor Flask:
   ```bash
   python app.py
   ```

   O servidor estará rodando em `http://127.0.0.1:5000/`. Você pode acessar o formulário para registrar novos pedidos e visualizar a lista de pedidos cadastrados.

   **Endpoints**:
   - `GET /`: Exibe o formulário para cadastro de pedidos.
   - `POST /`: Processa o envio do formulário e exibe o resumo do pedido.
   - `/listagem`: Exibe todos os pedidos cadastrados a partir do arquivo JSON.

### Como Usar o Bot (`bot.py`)

1. **Rodando o Bot**:
   Após instalar as dependências, execute o `bot.py` para iniciar a automação:
   ```bash
   python bot.py
   ```

   O Bot irá:
   - Preencher automaticamente o formulário da API com os pedidos definidos no código.
   - Navegar pela interface web para inserir dados de pedidos, como cliente, produtos, quantidades e status.
   - Exibir a lista de pedidos após a inserção.

### Dependências

O arquivo `requirements.txt` inclui as bibliotecas necessárias para rodar tanto a API quanto o bot. Para instalar as dependências:

```bash
pip install -r requirements.txt
```

### Considerações Finais

Este projeto foi desenvolvido como um exercício integrado de Orientação a Objetos, Programação Funcional, RPA (Automação Robótica de Processos) com o BotCity, e manipulação de arquivos binários e JSON. Durante o desenvolvimento, foi implementado tratamento de exceções, decoradores de log para os métodos e diversas funcionalidades para gerenciar os pedidos de uma loja virtual.
