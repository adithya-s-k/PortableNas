## Portable NAS using Raspberry Pi

This project aims to create a portable Network Attached Storage (NAS) using a Raspberry Pi. It allows users to insert any pendrive or hard disk, and the Raspberry Pi will act as a server and provide a unique key and password. Users can then enter this information on their computer connected to the same network, and a socket connection will be established between the computer and the Raspberry Pi, enabling access to the data on the inserted drive.

In addition, a frontend interface is provided that allows users to delete, list, upload, and change directories.

### Prerequisites

To use this project, you will need:

- A Raspberry Pi (tested with Raspberry Pi 4 Model B)
- A power supply for the Raspberry Pi
- A microSD card (16GB or larger) with Raspberry Pi OS installed
- A USB drive or external hard drive to use as storage

### Installation

To install the project, follow these steps:

- Clone the repository onto your Raspberry Pi.

```
git clone https://github.com/yourusername/portable-nas.git
```

- Install the required dependencies.

```
cd portable-nas
pip install -r requirements.txt
```

- Start the server.

```
python server.py
```

- Open a web browser on your computer and enter the IP address of your Raspberry Pi, followed by the port number (default is 5000).
  arduino

```
http://<Raspberry Pi IP address>:5000
```

- Enter the key and password displayed on the Raspberry Pi into the web interface.

- You should now be able to access the data on the inserted drive through the web interface.

### Usage

The web interface provides the following options:

- List: lists the files and directories in the current directory.
- Upload: allows you to upload a file to the current directory.
- Delete: allows you to delete a file or directory.
- Change Directory: allows you to navigate to a different directory.
