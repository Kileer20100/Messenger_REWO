import zmq


context = zmq.Context()
socket = context.socket(zmq.DEALER)
socket.connect("tcp://localhost:5050")

while True:


    response = socket.recv_multipart()
    print("Received from server:", response[1].decode())
