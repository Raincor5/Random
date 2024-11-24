import React, { useState } from 'react';
import './App.css';

function App() {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  const addTask = () => {
    // Logic to add task will go here
    if (task !== '') {
      setTasks([...tasks, task]);
      setTask('');
    }
  };

  return (
    <div className='App'>
      <header className='App-header'>
        <h1>Todo list</h1>
        <div>
          <input 
            type="text"
            placeholder='Add a new task'
            value={task}
            onChange={(e) => setTask(e.target.value)}
          />
          <button onClick={addTask}>Add task</button>
        </div>
        <div>
          <ul>
            {tasks.map((t, index) => (
              <li key={index}>{t}</li>
            ))}
          </ul>
        </div>
      </header>
    </div>
  );
}

export default App;
