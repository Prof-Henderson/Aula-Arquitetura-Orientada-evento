# consumer.py
import pika  # Biblioteca para conexão com o RabbitMQ
import json  # Para converter a mensagem recebida de volta para dicionário

# Função que será chamada automaticamente sempre que uma nova mensagem chegar
def callback(ch, method, properties, body):
    # body chega como string JSON; aqui transformamos em dicionário Python
    dados = json.loads(body)

    # Ação 1: Enviar um e-mail (simulado)
    print(f"[EMAIL] Enviando e-mail para {dados['email']} com assunto: {dados['assunto']}")

    # Ação 2: Registrar no log (simulado)
    print(f"[LOG] Evento salvo: {dados}")

# Cria a conexão com o RabbitMQ (localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Cria um canal dentro da conexão
channel = connection.channel()

# Garante que a fila "usuario_cadastrado" exista (mesmo nome usado no produtor)
channel.queue_declare(queue="usuario_cadastrado")

# Define qual função será chamada ao receber mensagens dessa fila
channel.basic_consume(
    queue="usuario_cadastrado",  # Nome da fila a ser escutada
    on_message_callback=callback,  # Função a ser executada quando chegar mensagem
    auto_ack=True  # Confirma automaticamente que a mensagem foi recebida com sucesso
)

# Exibe uma mensagem enquanto espera por eventos
print(" [*] Aguardando eventos. Pressione CTRL+C para sair.")

# Inicia o processo de escuta. Fica rodando até ser interrompido.
channel.start_consuming()
