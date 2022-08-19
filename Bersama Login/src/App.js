// import background from "./Bersama Fellowship.png";
// <img className="background" src={background} alt="Bersama Fellowship Background" />
import './App.css';
import Login from "./components/Login";
import Search from "./components/Search";

function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <div className='page'>
          <Login></Login>  
          <Search></Search>
        </div>
      </header>
    </div>
  );
}

export default App;
