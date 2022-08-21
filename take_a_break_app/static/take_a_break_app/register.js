function validateForm() {
    // please refer to views.py for changes
    let username = forms["register"]["username"].value;
    let email = forms["register"]["email"].value;
    let password = forms["register"]["password"].value;
    let confirm_password = forms["register"]["confirm_password"].value;
    let error_message = ""
    if (password != confirm_password) {
        error_message = "Please double check your password";
    } else if (username.length > 100) {
        error_message = "Username is too long";
    } else if (email.length > 100) {
        error_message = "Email is too long";
    } else {

    }
    /*
    if (password != confirmed_password):
            return 2
        if len(username)> 100:
            return 4
        if len(email)> 100:
            return 5
        pattern = "^\S+@\S+\.\S+$"
        if len(password)> 100:
            return 6
        if not check_user_exist(username):
            return 3 
        if not valid_email(email):
            return 7
        return 0
    else:
        return 1
    */
   /*
   elif response_id == 1:
            error_message = "Please enter valid character"
        elif response_id == 2:
            error_message = "Please double check your password"
        elif response_id == 3:
            error_message =  "User already exist"
        elif response_id == 4:
            error_message = "Username is too long"
        elif response_id == 5:
            error_message = "Email is too long"
        elif response_id == 6:
            error_message = "Password is too long"
        elif response_id == 7:
            error_message = "Incorrect email format"
   */
}