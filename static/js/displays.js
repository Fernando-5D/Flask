const radiosGenero = document.querySelectorAll('input[name="genero"]');
const selectPronombres = document.getElementById("pronombres");
radiosGenero.forEach(radio => {
    radio.addEventListener('change', () => {
        if (radio.value === "personalizado") {
            selectPronombres.style.display = 'block';
            
        } else {
            selectPronombres.style.display = 'none';
        }
    });
});

const radiosNumOrEmail = document.querySelectorAll('input[name="numOrEmail"]');
const inputTelefono = document.getElementById("telefono");
const inputEmail = document.getElementById("email");
radiosNumOrEmail.forEach(radio => {
    radio.addEventListener('change', () => {
        if (radio.value === "numero") {
            inputTelefono.style.display = 'block';
            inputEmail.style.display = 'none';
            inputTelefono.required = true;
            inputEmail.required = false;
            inputEmail.value = "";
            
        } else {
            inputTelefono.style.display = 'none';
            inputEmail.style.display = 'block';
            inputTelefono.required = false;
            inputEmail.required = true;
            inputTelefono.value = "";
        }
    });
});