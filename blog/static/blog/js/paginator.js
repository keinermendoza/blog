// for use this object you need to
// 1. make an new instance providing the intial parameters
// 2. pass the data required by your specific builder
// 3. call the init method
class Paginator {
    constructor(paginateBy, builder, container) {
        this.paginateBy = paginateBy;
        this.builder = builder;
		this.containerElement = container;  
        this.btnCurrent = null;
        this.btnPrev = null;
		this.btnNext = null;

		this.data = [];
        this.currentPage = 1;
        this.totalPages = null;
        
        this.createBtns();      
        this.putBtns;
        this.numPages;
        this.render;

		this.btnPrev.onclick = () => this.goPrev();
		this.btnNext.onclick = () => this.goNext();
        
        this.init = () => {
            this.putBtns()
            this.numPages();
            this.render();
        }
    }

    createBtns() {
        const btnPrev = document.createElement("button");
        btnPrev.className = "btn btn-primary";
        btnPrev.innerHTML = "Previous";
        this.btnPrev = btnPrev;

        const btnNext = btnPrev.cloneNode();
        btnNext.innerHTML = "Next";
        this.btnNext = btnNext;

        const btnCurrent = btnPrev.cloneNode();
        btnCurrent.className = "btn btn-secondary";
        this.btnCurrent = btnCurrent;
    }

    putBtns() {
        const div = document.createElement("div");
        div.className = "d-flex aling-items-center justify-content-center gap-2";

        div.append(this.btnPrev, this.btnCurrent, this.btnNext);
        this.containerElement.after(div);

        // to delete
        // create element
        const js = document.createElement("div")
        js.innerHTML = `<h4 class="text-center">JavaScript Pagination</h4>`;
        div.before(js);
        
    }

	goNext() {
		if(this.currentPage < this.totalPages) {
			this.currentPage++;
			this.render();
		}
    }

    goPrev() {
		if (this.currentPage > 1) {
			this.currentPage--;
			this.render();
		}
    }
    numPages() {
        this.totalPages = Math.ceil(this.data.length / this.paginateBy);
    }
    
    render() {
		
		// update the counter
		this.btnCurrent.innerHTML = `Showing <b>${this.currentPage}</b> of ${this.totalPages}`
	
		if (this.currentPage == 1) {
			this.btnPrev.style.visibility = "hidden";
		} else {
			this.btnPrev.style.visibility = "visible";
		}

		if (this.currentPage == this.totalPages) {
			this.btnNext.style.visibility = "hidden";
		} else {
			this.btnNext.style.visibility = "visible";
		}
		const start = (this.currentPage - 1) * this.paginateBy;
		const end = start + this.paginateBy;
		const dataCurrentPage = this.data.slice(start,end);

		this.containerElement.innerHTML = dataCurrentPage.map(elem => this.builder(elem)).join("");
	}    
}
