import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {
render() {
    return (
    <div>
    <button type="button" onClick={this.onClick}>Send GET /products </button>
    </div>
    );
}

onClick(ev) {
  console.log("Sending a GET API Call !!!");
  axios.get('/users/')
  .then(res => {
          console.log(res.data)
  }).then(response => {
      console.log(JSON.stringify(response));
  })    
} 

}

export default App;