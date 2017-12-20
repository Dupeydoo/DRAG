var slider = document.getElementById("fitnessrange");
var rating = document.getElementById("rating");

rating.innerHTML = slider.value;


slider.oninput = function() {
    rating.innerHTML = this.value;
};