import zmq


context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.identity = b"1"
socket.connect("tcp://localhost:5050")

while True:

    print("Введите ID получателя:")
    id_send = input().strip().encode("utf-8")
    
    print("Введите сообщение:")
    message = input().encode("utf-8")


    socket.send_multipart([socket.identity, id_send, message])

    response = socket.recv_multipart()
    print("Received from server:", response[1].decode())
