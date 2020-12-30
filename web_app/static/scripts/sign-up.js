function validate(){
    var name = document.forms["signUpForm"]["name"].value;
    var email = document.forms["signUpForm"]["email"].value;
    var password = document.forms["signUpForm"]["password"].value;
    var retypedPassword = document.forms["signUpForm"]["retypePassword"].value;
    var phoneNumber =  document.forms["signUpForm"]["phoneNumber"].value;

    if (name == "" || name == null ||){
        alert("Error: Name can not be blank!");
        return(false);
    }else if (email == "" || email == null || email.includes(".edu")){
        alert("Error: Email didn't pass check (was null or was not a .edu email)");
        return(false);
    }else if (password !== retypedPassword || password == null || password == "" || retypePassword == null || retypePassword == ""){
        alert("Error: Passwords do not match!");
        return(false);
    }else if (phoneNumber == "" || phoneNumber == null || phoneNumber.includes("-")){
        alert("Error: Phone number is null, empty, or contains dashes!");
        return(false);
    }
}