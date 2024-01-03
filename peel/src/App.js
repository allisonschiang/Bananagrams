import './App.css';
import Game from './components/Game/Game';


function App() {
  fetch("http://localhost:8000").then(response => response.json()).then(data => console.log(data))
  return (
    <div className="App">
      <Game/>
      
    </div>
  );
}

export default App;
