document.addEventListener("DOMContentLoaded", function() {
    const tipoSelect = document.getElementById("category"); // Obtiene el ID que el usuario usara para elegir la conversion
    const form = document.getElementById("conversion-form"); // Obtiene el ID del formulaio que enviara la solicitud

    // Cambiar la acción del formulario según la selección del usuario
    categorySelect.addEventListener("change", function() {
        let category = tipoSelect.value;
        if (category === "longitud") {
            form.action = "/convert_long/";
        } else if (category === "peso") {
            form.action = "/convert_weight/";
        } else if (category === "temperatura") {
            form.action = "/convert_temperature/";
        }
    });

    // Ejecutar el evento al cargar para establecer el valor inicial
    tipoSelect.dispatchEvent(new Event("change"));
});
