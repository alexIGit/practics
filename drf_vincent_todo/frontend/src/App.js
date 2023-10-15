import logo from './logo.svg';
import './App.css';

import React, { Component } from 'react';
import axios from 'axios';

const list = [
  {
      "id": 1,
      "title": "qwetitle #1",
      "body": "body #1"
  },
  {
      "id": 2,
      "title": "123task #2",
      "body": "somethin to do"
  },
  {
      "id": 3,
      "title": "123warming #3",
      "body": "Very spetionaml task"
  }
]

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

class App extends Component {
  // constructor(props) {
  //   super(props);
  //   this.state = { list };
  // }
  state = {
    todos: []
  };

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
    .get('http://127.0.0.1:8000/api/')
    .then(res => {
      this.setState({ todos: res.data });
    })
    .catch(err => {
      console.log(err);
    });
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <p>{item.body}</p>
          </div>
        ))}
      </div>
    );
  }
}
export default App;
