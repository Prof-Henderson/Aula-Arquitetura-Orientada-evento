import pika  # Importa a biblioteca pika para comunicação com o RabbitMQ
import json  # Importa json para converter o dicionário em string JSON

# Cria uma conexão com o servidor RabbitMQ que está rodando localmente
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Cria um canal de comunicação dentro da conexão
channel = connection.channel()

# Garante que a fila chamada "usuario_cadastrado" exista
# Se não existir, ela será criada automaticamente
channel.queue_declare(queue="usuario_cadastrado")

# Cria uma mensagem representando um novo usuário cadastrado
mensagem = {
    "email": "joao@example.com",
    "assunto": "Bem-vindo ao sistema!"
}

# Publica a mensagem no RabbitMQ
# - exchange="" significa que usamos o exchange padrão do RabbitMQ
# - routing_key="usuario_cadastrado" indica para qual fila estamos enviando
# - body é o conteúdo da mensagem, que deve ser uma string
channel.basic_publish(
    exchange="",
    routing_key="usuario_cadastrado",
    body=json.dumps(mensagem)  # Converte o dicionário em string JSON
)

# Apenas para visualização no terminal
print("[x] Evento 'usuario_cadastrado' enviado.")

# Fecha a conexão com o RabbitMQ
connection.close()
