function validateForm() {
    var x = document.forms["myForm"]["s1_name"].value;
    if (x == null || x == "") {
        alert("Name must be filled out");
        return false;
    }
}