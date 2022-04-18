import { Button, Container, Typography } from "@material-ui/core";
import ArrowBackIosSharpIcon from "@material-ui/icons/ArrowBackIosSharp";
import { Link } from "react-router-dom";

const About = () => {
	return (
		<Container>
			<Typography variant="h4" component="h2" gutterBottom>
				About Page woohoo!
			</Typography>
			<Link to="/">
				<Button
					color="secondary"
					variant="outlined"
					startIcon={<ArrowBackIosSharpIcon />}
				>
					Back
				</Button>
			</Link>
		</Container>
	);
};

export default About;
