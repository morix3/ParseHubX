function disableButton() {
    let button = document.getElementById("parse-button");

    button.disabled = true;

    button.innerText = "Парсинг...";
}