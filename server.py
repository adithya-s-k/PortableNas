
import os
import socket
import threading
import shutil

IP = socket.gethostbyname(socket.gethostname())
HOST = "localhost"
PORT = 4456
ADDR = (HOST, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(FORMAT))
    global SERVER_DATA_PATH

    while True:
        try:
            data = conn.recv(SIZE).decode(FORMAT)
            data = data.split("@")
            cmd = data[0]

            if cmd == "ls":
                files = os.listdir(SERVER_DATA_PATH)
                send_data = "OK@"

                if len(files) == 0:
                    send_data += "The server directory is empty"
                else:
                    send_data += "\n".join(f for f in files)
                conn.send(send_data.encode(FORMAT))

            elif cmd == "cd":
                if data[1] == "..":
                    if SERVER_DATA_PATH == "server_data":
                        conn.send("OK@You are already in the root directory.".encode(FORMAT))
                        continue
                    else:
                        index = SERVER_DATA_PATH.rfind(str('\\'))
                        final_path = SERVER_DATA_PATH[:index]
                        SERVER_DATA_PATH = final_path
                        print(final_path)
                else: 
                    final_path = os.path.join(SERVER_DATA_PATH, data[1])
                    SERVER_DATA_PATH = final_path
                    print(final_path)
                conn.send("OK@Changed directory successfully.".encode(FORMAT))
                
                
            elif cmd == "mkdir":
                path = data[1]
                files = os.listdir(SERVER_DATA_PATH)
                
                if path in files:
                    conn.send("OK@Directory already exists.".encode(FORMAT))
                    continue
                else:
                    final_path = os.path.join(SERVER_DATA_PATH, path)
                    os.mkdir(final_path)
                    conn.send("OK@Created directory successfully.".encode(FORMAT))
                
            elif cmd == "rmdir":
                path = data[1]
                if os.path.exists(os.path.join(SERVER_DATA_PATH, path)):
                    try:
                        os.rmdir(os.path.join(SERVER_DATA_PATH, path))
                        print (os.path.join(SERVER_DATA_PATH, path))
                    except OSError:
                        try:
                            shutil.rmtree(os.path.join(SERVER_DATA_PATH, path))
                        except:
                            conn.send("OK@Directory not empty.".encode(FORMAT))
                    conn.send("OK@Removed directory successfully.".encode(FORMAT))
                else:
                    conn.send("OK@Directory not found.".encode(FORMAT))
                
            elif cmd == "rm":
                send_data = "hello"
                files = os.listdir(SERVER_DATA_PATH)
                send_data = "OK@"
                filename = data[1]
                print(filename)    
                if len(files) == 0:
                    send_data += "The server directory is empty"
                else:
                    if filename in files:
                        os.remove(os.path.join(SERVER_DATA_PATH, filename))
                        send_data += "File deleted successfully."
                    else:
                        send_data += "File not found."
                
                conn.send(send_data.encode(FORMAT))
                
            elif cmd == "upload":
                name, text = data[1], data[2]
                filepath = os.path.join(SERVER_DATA_PATH, name)
                with open(filepath, "w") as f:
                    f.write(text)

                send_data = "OK@File uploaded successfully."
                conn.send(send_data.encode(FORMAT))

            elif cmd == "help":
                data = "OK@"
                data += "ls: List all the files from the server.\n"
                data += "cd <directory>: Change directory.\n"
                data += "mkdir <directory>: Create a directory.\n"
                data += "rmdir <directory>: Remove a directory.\n"
                data += "rm <filename>: Delete a file from the server.\n"
                data += "upload <path>: Upload a file to the server.\n"
                data += "logout: Disconnect from the server.\n"
                data += "help: List all the commands."

                conn.send(data.encode(FORMAT))
                
            elif cmd == "invalid":
                data = "OK@"
                data += "Invalid command. Please type help to see all the commands."

                conn.send(data.encode(FORMAT))
            
            elif cmd == "logout":
                break
        except:
            conn.send("OK@Error occured.".encode(FORMAT))
            
    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

def main():
    # host = "localhost" 
    print("[STARTING] Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    # print(f"[STARTING] server is starting on {host}:{PORT}")
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
