class Sender{
    constructor(form, reload=false) {
        this.form = form;
        this.reload = reload;
        this.csrf = this.form["csrfmiddlewaretoken"].value;
        this.toastContainer = document.getElementById("toast-container");
        this.setSubmition();
    }

    setSubmition() {
        this.form.addEventListener("submit", (e) => {
            this.removeErrorStyle(); // removes red color of each field
            e.preventDefault()

            const newForm = new FormData(this.form);
            fetch(this.form.action, {
                method: "POST",
                body: newForm,
            })
            .then(response => {
                if (!response.ok) {
                    this.handleError(response);
                    throw new Error(response.status); // cut then flow
                } else {
                    return response.json();
                }
            })
            .then(data => {
                this.handleSuccess(data);
            })
            .catch(err => {
                console.error(err);
            }) 
        }); 
    }

    async handleError(response) {
        const data = await response.json() // dict of each field with arrays
        const tupleFieldsErrors = Object.entries(data); // list of tuple field:errors

        tupleFieldsErrors.forEach(field => {
            // setting the css of field as invalid
            const fieldElement = document.getElementById(`id_${field[0]}`);
            fieldElement.classList.add("is-invalid"); 

            // showing pop-up errors
            const errorsMessages = Object.values(field[1]); 
            errorsMessages.forEach(error =>  {
                this.toastContainer.appendChild(this.cretaeToast(error.message)); // append toast
            });
        })      
    }

    handleSuccess(data) {
        if (this.reload) {
            window.location.reload();
        } else {
            this.toastContainer.appendChild(this.cretaeToast(data.message, false))
            this.form.reset();
            this.form["csrfmiddlewaretoken"].value = this.csrf;
        }
    }

    removeErrorStyle() {
        for (let element of this.form) {
            element.classList.remove("is-invalid");
        }
    }

    cretaeToast(str, error=true) {
        const toast = document.createElement("div");
        if (error) {
            toast.className = "alert alert-danger alert-dismissible fade show  z-maximum";
        } else {
            toast.className = "alert alert-success alert-dismissible fade show  z-maximum";
        }
        toast.role = "alert";
        toast.innerHTML = `
            ${str}.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            `;
        return toast;
    }
} // end Sender object

document.addEventListener("DOMContentLoaded", () => {
    const commentForm = document.getElementById("comment-form");
    const recomendForm = document.getElementById("recomend-form");
    new Sender(commentForm, true);
    new Sender(recomendForm);
})

