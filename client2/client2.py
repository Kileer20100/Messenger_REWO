import zmq

# Инициализируем контекст и создаем DEALER-сокет для клиента
context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.identity = b"2"  # Присваиваем ID клиенту (например, "1")
socket.connect("tcp://localhost:5050")

while True:
    # Ввод ID получателя и сообщения
    print("Введите ID получателя:")
    id_send = input().strip().encode("utf-8")
    
    print("Введите сообщение:")
    message = input().encode("utf-8")

    # Отправляем ID получателя и сообщение серверу
    socket.send_multipart([socket.identity, id_send, message])

    # Получаем ответ от сервера
    response = socket.recv_multipart()
    print("Received from server:", response[1].decode())
