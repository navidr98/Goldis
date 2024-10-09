let inputs = document.querySelectorAll('.inputs')

inputs.forEach(function(input) {
    input.addEventListener('input', function() {
        if (input.value) {
            input.style.textAlign = 'left'
            input.style.direction = 'ltr'
        } else {
            input.style.textAlign = 'right'
        } 
    })
    input.addEventListener('keydown', function (event) {
        console.log(event.keycode);
    })
})