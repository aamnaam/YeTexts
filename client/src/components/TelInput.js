import { useState } from "react";
import PhoneInput from "react-phone-input-2";
import { Button, Container, TextField, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import ArrowBackIosSharpIcon from "@material-ui/icons/ArrowBackIosSharp";
import ArrowForwardIosSharpIcon from "@material-ui/icons/ArrowForwardIosSharp";
import { Link } from "react-router-dom";
import "react-phone-input-2/lib/material.css";
import "./index.css";

import axios from "axios";

const useStyles = makeStyles({
	field: {
		marginTop: 10,
		marginBottom: 10,
		display: "block",
	},
});

const TelInput = () => {
	const classes = useStyles("");

	const [name, setName] = useState("");
	const [phone, setPhone] = useState("");

	const handleSubmit = (e) => {
		e.preventDefault();
		if (name !== "" && phone !== "") {
			const applyingUser = { name: name, WAid: phone };
			axios
				.post("/api/register", applyingUser)
				.then(function (response) {
					console.log(response);
				})
				.catch(function (err) {
					console.log(err);
				});

			console.log("New user request sent");
		} else {
			alert("Cannot be empty");
		}
	};

	return (
		<Container id="main">
			<Typography variant="h4" component="h2">
				Register!
			</Typography>
			<form noValidate autoComplete="off">
				<TextField
					className={classes.field}
					label="Name"
					variant="outlined"
					required
					value={name}
					onChange={(e) => setName(e.target.value)}
				/>
				<PhoneInput
					style={{ marginBottom: 10 }}
					country={"us"}
					value={phone}
					onChange={(phone) => setPhone(phone)}
				/>
			</form>

			<Link to="/">
				<Button
					color="secondary"
					variant="outlined"
					startIcon={<ArrowBackIosSharpIcon />}
				>
					Back
				</Button>
			</Link>
			<Button
				color="primary"
				variant="outlined"
				type="submit"
				endIcon={<ArrowForwardIosSharpIcon />}
				onClick={(e) => handleSubmit(e)}
			>
				Submit
			</Button>
		</Container>
	);
};

export default TelInput;
