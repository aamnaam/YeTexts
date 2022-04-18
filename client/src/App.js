import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import TelInput from "./components/TelInput";
import About from "./components/About";
import Home from "./components/Home";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
      </Switch>
      <Switch>
        <Route exact path="/about">
          <About />
        </Route>
      </Switch>
      <Switch>
        <Route exact path="/register">
          <TelInput />
        </Route>
      </Switch>
      {/* <TelInput /> */}
    </Router>
  );
}

export default App;
