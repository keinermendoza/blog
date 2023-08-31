document.addEventListener("DOMContentLoaded", () => {
    const url =  document.getElementById("search-form").action;
    const container = document.getElementById("search-container");
    document.getElementById("query").oninput = (e) => {
        if (e.target.value.trim() != "") {
            const query = e.target.value;
            fetch(`${url}?query=${query}`)
		    .then(response => {
		        if (!response.ok) { 
			        throw new Error("some error")
        	    }
		        return response.json();
		    })
	        .then(data => {
                builder(container, data)
            }
                )
	        .catch(err => console.error(err))
        }
    }
});


function builder(container, data) {
    if (data.length == 0){ return;}
    container.innerHTML = data.map(elem => {
        return  `
        <h3>${elem.title}</h3>
        <p>${elem.body}</p>
		`
	}).join("");
    console.log(data);

}
