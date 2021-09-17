const url_data = "https://raw.githubusercontent.com/danblanc/pag_webinar/main/data.json"
const url_data_2 = "https://raw.githubusercontent.com/danblanc/pag_webinar/main/data_2.json"

window.addEventListener('DOMContentLoaded', (event) => {
    fetch(url_data_2)
    .then(response => response.json())
    .then(data => {
        let contenido = ""

        for (let index = 0; index < data.length; index++) {
            let estrellas = ""
            for (let estrella = 1; estrella <= 5; estrella++) {
                if (estrella <= data[index].rate) {
                    estrellas += `<span alt="${data[index].rate}" class="fa fa-star checked"></span>`
                } else {
                    estrellas += `<span alt="${data[index].rate}" class="fa fa-star"></span>`
                }
            
            }

            contenido += `
            <div class="card">
              <div class="card-body">
              <b>${data[index].user}</b>
                ${estrellas}
                <p>${data[index].coment}</p>
                <span style = "font-family: cursive;">${data[index].date}</span>
                </div>
            </div>
            `
            
        }
        console.log(data)
        document.getElementById("comentarios").innerHTML = contenido;
    })    
});