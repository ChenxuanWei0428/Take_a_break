function validate_form() {
    // please refer to views.py for changes
    let form = document.getElementById("re_form").elements;
    let username = form["username"].value;
    let email = form["email"].value;
    let password =form["password"].value;
    let confirm_password = form["confirm_password"].value;
    let error_message = ""
    if (password != confirm_password) {
        error_message = "Please double check your password";
    } else if (username.length > 100) {
        error_message = "Username is too long";
    } else if (email.length > 100) {
        error_message = "Email is too long";
    } else if (password.length > 100) {
        error_message = "Password is too long";
    }  else if (!valid_email(email)) {
        error_message = "Incorrect email format";
    }
    console.log("error_message")
    if (error_message == "") {
        return true;
    } else {
        ReactDOM.render(
            error_message,
            document.getElementById('error_message')
        );
        return false;
    }
};

function valid_email(email) {
    let pattern = /^\S+@\S+\.\S+$/i;
    return email.search(pattern) != -1;
};
