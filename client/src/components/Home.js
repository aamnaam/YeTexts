import { Button, Container, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import { Link } from "react-router-dom";
import "./index.css";

const useStyles = makeStyles({
	btn: {
		backgroundColor: "blue",
		"&:hover": {
			backgroundColor: "black",
		},
	},
});

const Home = () => {
	const classes = useStyles();

	return (
		<div id="main">
			<Typography
				variant="h3"
				color="secondary"
				align="center"
				gutterBottom
			>
				YeTexts!
			</Typography>
			<h2>Register below to get started with our WhatsApp chatbot!</h2>
			<br />
			<Link to="/register">
				<Button
					className={classes.btn}
					variant="outlined"
					color="primary"
					href="/register"
				>
					Register
				</Button>
			</Link>
			<Link to="/about">
				<Button color="secondary" variant="outlined">
					About
				</Button>
			</Link>
		</div>
	);
};

export default Home;
