// Update the contrast slider value
let cont_slider = document.getElementById("contrast-slider");
let cont_output = document.getElementById("contrast-value");
cont_output.innerHTML = cont_slider.value;

cont_slider.oninput = function() {
  cont_output.innerHTML = this.value;
}

// Update the brightness slider value
let bright_slider = document.getElementById("brightness-slider");
let bright_output = document.getElementById("brightness-value");
bright_output.innerHTML = bright_slider.value;

bright_slider.oninput = function() {
  bright_output.innerHTML = this.value;
}

// Update the sharpness slider value
let sharp_slider = document.getElementById("sharpness-slider");
let sharp_output = document.getElementById("sharpness-value");
sharp_output.innerHTML = sharp_slider.value;

sharp_slider.oninput = function() {
  sharp_output.innerHTML = this.value;
}

// Update the color slider value
let col_slider = document.getElementById("color-slider");
let col_output = document.getElementById("color-value");
col_output.innerHTML = col_slider.value;

col_slider.oninput = function() {
  col_output.innerHTML = this.value;
}

// Update the blur slider value
let bl_slider = document.getElementById("blur-slider");
let bl_output = document.getElementById("blur-value");
bl_output.innerHTML = bl_slider.value;

bl_slider.oninput = function() {
  bl_output.innerHTML = this.value;
}