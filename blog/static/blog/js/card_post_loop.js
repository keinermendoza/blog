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