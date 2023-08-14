// import './App.css'
import Hello from './components/Hello'; 
import Message from './components/Message';
import Profile from './components/Profile';
function App() {
  return (
    <div className="App">
      {/* <Hello /> */}
      <Message messagecode = "10" messagecontent="Displayed Message from props" />
      {/* <Profile name = "George" lastname = "Oduor"/> */}
    </div>
  );
}

export default App;
