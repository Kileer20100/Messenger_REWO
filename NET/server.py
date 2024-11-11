import zmq

# Инициализируем контекст и создаем ROUTER-сокет для сервера
context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://*:5050")

print("Server is running...")

while True:
    # Получаем ID отправителя, ID получателя и само сообщение
    sender_id, empty, receiver_id, message = socket.recv_multipart()
    
    # Выводим информацию о сообщении
    print(f"Received from {sender_id.decode()} to {receiver_id.decode()}: {message.decode()}")

    # Отправляем сообщение указанному получателю
    socket.send_multipart([receiver_id, b"", message])
