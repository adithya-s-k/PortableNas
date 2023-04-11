import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:4456');

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  useEffect(() => {
    socket.on('message', (data) => {
      const [cmd, msg] = data.split('@');
      if (cmd === 'DISCONNECTED') {
        setResponse(msg);
      } else if (cmd === 'OK') {
        setResponse(msg);
      }
    });
  }, []);

  const handleClick = (cmd, arg) => {
    let data;
    if (cmd === 'HELP' || cmd === 'LOGOUT' || cmd === 'LIST') {
      data = cmd;
    } else if (cmd === 'DELETE') {
      data = `${cmd}@${arg}`;
    } else if (cmd === 'UPLOAD') {
      const file = document.getElementById('file').files[0];
      const reader = new FileReader();
      reader.onload = () => {
        const text = reader.result;
        const filename = file.name;
        const send_data = `${cmd}@${filename}@${text}`;
        socket.emit('message', send_data);
      };
      reader.readAsText(file);
      return;
    }
    socket.emit('message', data);
  };

  return (
    <div>
      <p>{response}</p>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={() => handleClick(message)}>Send</button>
      <button onClick={() => handleClick('HELP')}>Help</button>
      <button onClick={() => handleClick('LOGOUT')}>Logout</button>
      <button onClick={() => handleClick('LIST')}>List</button>
      <input type="file" id="file" />
      <button onClick={() => handleClick('UPLOAD')}>Upload</button>
    </div>
  );
}

export default App;
