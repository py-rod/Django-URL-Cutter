function setDefaultValue(event) {
    let border_value = event.target.value;

    if (border_value < 0) {
        event.target.value = 0
    }
}
