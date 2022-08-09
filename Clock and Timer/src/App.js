import logo from './ricevillage.jpeg';

import './App.css';
import Clock from './components/Clock';
import Timer from './components/Timer';

function App() {
  // Date, Day, Countdown
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <img src={logo} alt="logo" className='riceVillage'/>
        </div>

        <div>
          <h1 id='riceClock'>RiceClock</h1>
          <Clock/>
        </div>

        <div>
          <h1 id='riceTimer'>RiceTimer</h1>
          <Timer/>
        </div>
      </header>
    </div>
  );
}

export default App;
