function validateForm() {
    var x = document.forms["userForm"]["s1_name"].value;
    if (x == null || x == "") {
        alert("Please enter in a name");
        return false;
    }
}