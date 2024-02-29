// Función para abrir/cerrar el menú desplegable
        function toggleDropdown() {
            let dropdown = document.getElementsByClassName("dropdown")[0];
            dropdown.classList.toggle("open");
        }

        // Agregar un controlador de eventos de clic en el documento
        document.addEventListener("click", function (event) {
            let dropdown = document.getElementsByClassName("dropdown")[0];
            // Verificar si el clic ocurrió fuera del menú desplegable
            if (!event.target.closest('.dropdown') && dropdown.classList.contains('open')) {
                dropdown.classList.remove('open');
            }
        });