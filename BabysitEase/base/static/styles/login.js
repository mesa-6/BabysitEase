document.getElementById('sendButton').addEventListener('click', function () {
    var email = document.getElementById('emailInput').value;
    if (email) {
        // Exibir popup
        document.getElementById('popup').style.display = 'block';
        // Ocultar popup após 3.5 segundos
        setTimeout(function () {
            document.getElementById('popup').style.display = 'none';
        }, 3500);
    }
});