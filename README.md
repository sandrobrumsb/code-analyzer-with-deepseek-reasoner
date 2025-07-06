# 📁🤖 Projeto: Exemplo simples de ferramenta em IA para compreensão e raciocínio sobre código-fonte.
---

### 🔍 `O que ele faz:`

O Realiza a analise de um código que é carregado de um arquivo `.csv`.

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
git clone https://github.com/sandrobrumsb/code-analyzer-with-deepseek-reasoner.git
```
### 2. Instale as 📚 Bibliotecas:
```bash
pip install -r requirements.txt
```
### 3. 📦 Crie o Arquivo `.env`:

- Arquivo `.env` com suas chaves de API:
  ```env
  DEEPSEEK_API_KEY='sua_chave_deepseek_aqui'
---
