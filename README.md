# 🤖 Anotações e Comparações de Análises de APIs DeepSeek & OpenAI.
---

## 📁 Projeto:

### 🔍 `analyzer_code_exemple.py`

**O que ele faz:**  
O código a ser analisado é carregado de um arquivo `.csv`.

Este script envia um código para o modelo `deepseek-reasoner` com o objetivo de **melhorar sua qualidade**. Ele realiza:

- Correções de legibilidade e nomes de variáveis
- Identificação de vulnerabilidades
- Ajustes na formatação
- Sugestões para tornar o código mais modular e reutilizável


---

## 🚀 Como rodar os scripts

Siga os passos abaixo para executar qualquer um dos projetos deste repositório:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
```
### 2. Instale as 📚 Bibliotecas:
```bash
pip install -r requirements.txt
```
### 3. 📦 Crie o Arquivo `.env`:

- Arquivo `.env` com suas chaves de API:
  ```env
  OPENAI_API_KEY=your_openai_key_here
  DEEPSEEK_API_KEY=your_deepseek_key_here
---