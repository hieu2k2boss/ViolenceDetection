import "./Css/App.css";
import Header from "./components/Header";
import HeaderNext from "./components/HeaderNext";
import Main from "./components/Main";
import TabSwitcher from "./components/TabSwitcher";

function App() {
  return (
    <div className="App">
      <Header/>
      <TabSwitcher/>
    </div>
  );
}

export default App;
