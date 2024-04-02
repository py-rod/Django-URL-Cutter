let check = document.getElementById('more_options');

let options_hiddent = document.getElementById('hiddent_qr_options');

check.addEventListener('change', function () {
    if (check.checked) {
        options_hiddent.style.display = 'block';
    }
    else {
        options_hiddent.style.display = 'none';
    }
});