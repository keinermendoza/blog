document.addEventListener("DOMContentLoaded", () => {
    const totalObj = parseInt(document.getElementById("lenght").value);
    const PaginateBy = 10;

    if (totalObj > PaginateBy) {
        
        const container = document.getElementById("post-list-container");
        const paginator = new Paginator(PaginateBy, CopyCardPostPattern, container)
        
        // fetching data
        const endpoint = document.getElementById("published-endpoint").value;
        fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            paginator.data = data.published;
            paginator.init()
        });

    }
})

function CopyCardPostPattern(elem) {
    return `
    <a class="nav-link" href="${elem.url}">
    <article class="card p-2 my-1">
            <h3>${elem.title}</h3>
            <h6>By ${elem.author}</h6>
            <p class="small">Publish on ${elem.publish}</p>
            <p class="m-0">${elem.body}</p> 
    </article>
    </a>
    `
}