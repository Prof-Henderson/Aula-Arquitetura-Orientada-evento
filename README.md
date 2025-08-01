# 🧰 Ambiente de Desenvolvimento com RabbitMQ e Python (Windows)

---

## 📦 O que será instalado

- Python 3
- pip (gerenciador de pacotes do Python)
- Erlang
- RabbitMQ
- Plugin de gerenciamento do RabbitMQ
- Biblioteca Python `pika`

---

## ✅ 1. Instalar o Python 3

1. Acesse: https://www.python.org/downloads/windows/
2. Baixe a versão recomendada para Windows.
3. Durante a instalação, marque a opção:

✅ Add Python to PATH

4. Após instalar, verifique no terminal:

```
python --version
```
✅ 2. Instalar o Erlang
Acesse: https://www.erlang.org/downloads

Baixe a versão do instalador para Windows (.exe).

Execute o instalador normalmente.

Verifique se o caminho do Erlang foi adicionado ao PATH. Exemplo:
```
C:\Program Files\erl-XX.X\bin
```

✅ 3. Instalar o RabbitMQ
Acesse: https://www.rabbitmq.com/install-windows.html

Baixe e instale o RabbitMQ Server para Windows.

Após a instalação, o RabbitMQ será adicionado como serviço do Windows.

✅ 4. Iniciar o serviço do RabbitMQ
Abra o Prompt de Comando (cmd) como administrador e execute:

```
net start RabbitMQ
```
Para parar:
```
net stop RabbitMQ
```
Verificar status:
```
sc query RabbitMQ
```

✅ 5. Habilitar o painel de gerenciamento do RabbitMQ (opcional, mas recomendado)
No terminal, execute:

```
rabbitmq-plugins enable rabbitmq_management
```
Reinicie o serviço:
```
net stop RabbitMQ
net start RabbitMQ
```

Acesse o painel no navegador:

http://localhost:15672
Login padrão:

Usuário: guest

Senha: guest

✅ 6. Instalar a biblioteca pika (cliente RabbitMQ para Python)
No terminal, digite:
```
pip install pika
```

✅ 7. Rodar os scripts Python
Certifique-se de que o serviço do RabbitMQ está rodando:
```
net start RabbitMQ
```
Navegue até a pasta onde estão os scripts Python e execute:
```
python produtor.py
```
Em outro terminal:
```
python consumidor.py
```
✅ Ferramentas instaladas
Ferramenta	Função
Python	Interpretar os scripts
pip	Instalar bibliotecas Python
Erlang	Requisito para o RabbitMQ
RabbitMQ	Broker de mensagens
pika	Biblioteca Python para enviar e consumir mensagens

🧪 Teste rápido
Se você rodar produtor.py e consumidor.py com o RabbitMQ ativo,
deve ver mensagens sendo enviadas e processadas no terminal.

