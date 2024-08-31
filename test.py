import varint
import socket as S

socket = S.socket(S.AF_INET, S.SOCK_STREAM)
socket.bind(('0.0.0.0', 25565))
socket.listen(1)
socket.settimeout(5)

while True:
    print("Wait...")

    try:
        connection, address = socket.accept()

        print(address)

        while True:
            print(connection.recv(1))
    except Exception:
        print("Exception")