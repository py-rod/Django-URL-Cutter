function toggleDropdownOptions(dropdownId) {
    let dropdown = document.getElementById('myDropdown-link-options' + dropdownId)
    dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block'
}