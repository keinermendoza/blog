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
    if (data.length == 0){ 
        container.innerHTML = "";
        return;
    }
    container.innerHTML = data.map(elem => {
        return  `
        <a class="nav-link" href="${elem.url}">
        <article class="card p-2 my-1">
            <h3>${elem.title}</h3>
            <h6>By ${elem.author}</h6>
            <p class="small">Publish on ${new Date(elem.publish)}</p>
            <p class="m-0">${elem.body}</p>
        </article>
        </a>

        `
	}).join("");

}
