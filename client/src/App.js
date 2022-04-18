import { BrowserRouter as Router, Route } from "react-router-dom";
import TelInput from "./components/TelInput";
import About from "./components/About";
import Home from "./components/Home";

function App() {
	return (
		<Router>
			<Route>
				<Route exact path="/">
					<Home />
				</Route>
			</Route>
			<Route>
				<Route exact path="/about">
					<About />
				</Route>
			</Route>
			<Route>
				<Route exact path="/register">
					<TelInput />
				</Route>
			</Route>
		</Router>
	);
}

export default App;
