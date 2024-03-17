document.addEventListener("DOMContentLoaded", function () {
    let text = document.querySelector('.text-enter-create');
    text.style.display = 'none'
    let inputOrigin = document.getElementById('id_original_url');

    inputOrigin.addEventListener('input', function (event) {
        if (event.target.value !== '') {
            text.style.display = 'block';
        } else {
            text.style.display = 'none';
        }
    });
});