function validateInfo() {
    let obj = document.getElementById("PhoneNumber");
    let phoneOkay = obj.checkValidity();

    if (phoneOkay) {
        alert('Phone Number is valid')
    } else {
        alert('Invalid Phone Number')
    }
}
