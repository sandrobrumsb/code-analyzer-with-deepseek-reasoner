from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente OpenAI com a chave de API e URL base personalizada
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
)

# Define o modelo a ser utilizado na chamada de API
model = "deepseek-reasoner"


def load(file_name):
    """
    Função para carregar o conteúdo de um arquivo de texto.
    Recebe o nome do arquivo e retorna seu conteúdo como string.
    Trata exceções de leitura, exibindo mensagem de erro caso ocorra.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except IOError as e:
        print(f"error: {e}")


# Prompt de sistema para instruir o assistente sobre a tarefa desejada
prompt_system = """
Você é um assistente especializado em correção de código. Realize as seguintes melhorias:
1. **Legibilidade**: Melhore nomes de variáveis, clareza e adicione comentários úteis.
2. **Vulnerabilidade**: Identifique e corrija potenciais falhas de segurança.
3. **Formatação**: Aplique consistência ao estilo de código (espaçamento, indentação, etc.).
4. **Reutilização**: Sugira modularidade e eliminação de redundâncias.
"""

# Carrega o conteúdo do arquivo CSV que contém o código a ser corrigido
prompt_user = load(r"dados\codigo.csv")

# Estima a quantidade de tokens aproximada do prompt total
number_of_tokens = len((prompt_system + prompt_user).split())
print(f"Estimativa de tokens de entrada: {number_of_tokens}")

# Exibe o modelo escolhido para a chamada de API
print(f"Modelo Escolhido: {model}")

# Monta a lista de mensagens para a API de chat do OpenAI
message_list = [
    {"role": "system", "content": prompt_system},
    {"role": "user", "content": prompt_user},
]

# Faz a chamada para a API de chat, solicitando a correção do código
response = client.chat.completions.create(
    messages=message_list,
    model=model,
    temperature=0.0,  # Temperatura zero para respostas mais determinísticas
)

# Exibe a resposta gerada pela API
print(response.choices[0].message.content)
