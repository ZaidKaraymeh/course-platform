/* $(document).ready(
    function() {
    $(':input[type="submit"]').prop('disabled', true)
}) */

$('.submit').click(function(){
    var spinner = document.createElement("div")
    spinner.className = "spinner-border text-light"
    $('.submit').empty();
    $('.submit').addClass('disabled');
    
    $('.submit').append(spinner);
})

