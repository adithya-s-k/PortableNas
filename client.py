import socket

IP = socket.gethostbyname(socket.gethostname())
HOST = "localhost"
PORT = 4456
# ADDR = (IP, PORT)
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    # client.connect(("raspberrypi", 5000))

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")
        # currentWorkingDirectory = ""

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        try :
            if cmd == "help":
                client.send(cmd.encode(FORMAT))
            elif cmd == "logout":
                client.send(cmd.encode(FORMAT))
                break
            elif cmd == "ls":
                client.send(cmd.encode(FORMAT))
            elif cmd == "cd":
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            elif cmd == "mkdir":
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            elif cmd == "rmdir":
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            elif cmd == "rm":
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            elif cmd == "up":
                path = data[1]
                with open(f"{path}", "r") as f:
                    text = f.read()
                filename = path.split("/")[-1]
                send_data = f"{cmd}@{filename}@{text}"
                client.send(send_data.encode(FORMAT))
            else:
                cmd = "invalid"
                client.send(cmd.encode(FORMAT))
        except IndexError:
            cmd = "invalid"
            client.send(cmd.encode(FORMAT))
        continue

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
