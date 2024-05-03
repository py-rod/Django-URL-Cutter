function toggleDropdownOptions(dropdownId) {
    let dropdown = document.getElementById('myDropdown-qr-options' + dropdownId)
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block'
}