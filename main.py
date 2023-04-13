import socket
from fastapi import FastAPI, File, UploadFile


IP = socket.gethostbyname(socket.gethostname())
HOST = "localhost"
PORT = 4456
# ADDR = (IP, PORT)
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024


app = FastAPI()


def send_message(cmd,data):
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
                client.send(f"{cmd}@{data}".encode(FORMAT))
            elif cmd == "mkdir":
                client.send(f"{cmd}@{data}".encode(FORMAT))
            elif cmd == "rmdir":
                client.send(f"{cmd}@{data}".encode(FORMAT))
            elif cmd == "rm":
                client.send(f"{cmd}@{data}".encode(FORMAT))
            elif cmd == "upload":
                path = data[1]
                with open(f"client_data/{path}", "r") as f:
                    text = f.read()
                filename = path
                print(filename)
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
    
@app.get("/")
def read_root():
  return {"message": "Hello World"}

@app.get("/help")
def read_help():
  return send_message("help",None)

@app.get("/logout")
def read_logout():
  return send_message("logout",None)

@app.get("/ls")
def read_ls():
  return send_message("ls",None)

@app.get("/cd/{path}")
def read_cd(path : str):
  return send_message("cd",path)

@app.get("/mkdir/{path}")
def read_mkdir(path : str):
  return send_message("mkdir",path)

@app.get("/rmdir/{path}")
def read_rmdir(path : str):
  return send_message("rmdir",path)

@app.get("/rm/{path}")
def read_rm(path : str):
  return send_message("rm",path)

@app.post("/upload/{path}")
def read_upload(path : str):
  return send_message("upload",path)