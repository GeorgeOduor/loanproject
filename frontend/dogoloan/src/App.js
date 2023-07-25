// import './App.css'
import Hello from './components/Hello'; 
import Message from './components/Message';
import Profile from './components/Profile';
function App() {
  return (
    <div className="App">
      <Hello />
      <Message />
      <Profile name = "George" lastname = "Oduor"/>
    </div>
  );
}

export default App;
