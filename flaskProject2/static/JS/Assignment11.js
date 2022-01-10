function myFunction(e) {
    number = document.getElementById("f_number");
    url = "https://reqres.in/api/users/"+number.value
    // console.log("clicked");
    fetch(url).then(
        response => response.json()
    ).then((response_obj) => {
        console.log(response_obj.data)
        return put_users_inside_html(response_obj.data)
    }
    ).catch(
        error => console.log(error)
    )
}

function put_users_inside_html(response_obj) {
    const current_main = document.querySelector("main");
    // debugger
    current_main.innerHTML = `
        <img src="${response_obj.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj.first_name} ${response_obj.last_name}</span>
            <br>
            <a href="mailto:${response_obj.email}">Send Email</a>
            <br><br>
        </div>
    `;
}