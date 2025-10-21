const radios = document.querySelectorAll('input[name="genero"]');
const select = document.getElementById("pronombres");

radios.forEach(radio => {
    radio.addEventListener('change', () => {
        if (radio.value === "personalizado") {
            select.style.display = 'block';
            
        } else {
            select.style.display = 'none';
        }
    });
});