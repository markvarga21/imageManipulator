// Update the contrast slider value
var cont_slider = document.getElementById("contrast-slider");
var cont_output = document.getElementById("contrast-value");
cont_output.innerHTML = cont_slider.value;

cont_slider.oninput = function() {
  cont_output.innerHTML = this.value;
}

// Update the brightness slider value
var bright_slider = document.getElementById("brightness-slider");
var bright_output = document.getElementById("brightness-value");
bright_output.innerHTML = bright_slider.value;

bright_slider.oninput = function() {
  bright_output.innerHTML = this.value;
}

// Update the sharpness slider value
var sharp_slider = document.getElementById("sharpness-slider");
var sharp_output = document.getElementById("sharpness-value");
sharp_output.innerHTML = sharp_slider.value;

sharp_slider.oninput = function() {
  sharp_output.innerHTML = this.value;
}

// Update the color slider value
var col_slider = document.getElementById("color-slider");
var col_output = document.getElementById("color-value");
col_output.innerHTML = col_slider.value;

col_slider.oninput = function() {
  col_output.innerHTML = this.value;
}

// Update the blur slider value
var bl_slider = document.getElementById("blur-slider");
var bl_output = document.getElementById("blur-value");
bl_output.innerHTML = bl_slider.value;

bl_slider.oninput = function() {
  bl_output.innerHTML = this.value;
}