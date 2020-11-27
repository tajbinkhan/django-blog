const usernameField = document.querySelector("#id_username");
const emailField = document.querySelector("#id_email");
const invalidfeedbackArea = document.querySelector('.username-invalid');
const emailinvalidfeedbackArea = document.querySelector('.email-invalid');
const validfeedbackArea = document.querySelector('.username-valid');
const emailvalidfeedbackArea = document.querySelector('.email-valid');

emailField.addEventListener("keyup", (e) => {
	const emailVal = e.target.value;
	emailField.classList.remove("is-invalid");
	emailinvalidfeedbackArea.style.display = "none";
	emailField.classList.remove("is-valid");
	emailvalidfeedbackArea.style.display = "none";
	if (emailVal.length > 0) {
		fetch("/accounts/validate-email/", {
			body: JSON.stringify({email: emailVal}),
			method: "POST",
		}).then((res)=>res.json()).then((data)=> {
			console.log("data", data);
			if (data.email_error) {
				emailField.classList.add("is-invalid");
				emailinvalidfeedbackArea.style.display = "block";
				emailinvalidfeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
			} else {
				emailField.classList.add("is-valid");
				emailvalidfeedbackArea.style.display = "block";
				emailvalidfeedbackArea.innerHTML = `<p>${data.email_valid}</p>`;
			}
		});
	}
});

usernameField.addEventListener("keyup", (e) => {
	const usernameVal = e.target.value;
	usernameField.classList.remove("is-invalid");
	invalidfeedbackArea.style.display = "none";
	usernameField.classList.remove("is-valid");
	validfeedbackArea.style.display = "none";
	if (usernameVal.length > 0) {
		fetch("/accounts/validate-username/", {
			body: JSON.stringify({username: usernameVal}),
			method: "POST",
		}).then((res)=>res.json()).then((data)=> {
			console.log("data", data);
			if (data.username_error) {
				usernameField.classList.add("is-invalid");
				invalidfeedbackArea.style.display = "block";
				invalidfeedbackArea.innerHTML = `<p>${data.username_error}</p>`;
			} else {
				usernameField.classList.add("is-valid");
				validfeedbackArea.style.display = "block";
				validfeedbackArea.innerHTML = `<p>${data.username_valid}</p>`;
			}
		});
	}
});