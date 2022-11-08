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

let minimum_slider = document.getElementById("minimum-slider");
let minimum_output = document.getElementById("minimum-value");
minimum_output.innerHTML = minimum_slider.value;

minimum_slider.oninput = function() {
  minimum_output.innerHTML = this.value;
}

let maximum_slider = document.getElementById("maximum-slider");
let maximum_output = document.getElementById("maximum-value");
maximum_output.innerHTML = maximum_slider.value;

maximum_slider.oninput = function() {
  maximum_output.innerHTML = this.value;
}
///////////////////

//buttons control

let retouch = button => {
  let photort = document.getElementById("photo_rt");
  let hidden = photort.getAttribute("hidden");

     photort.removeAttribute("hidden");

  let back_rem = document.getElementById("back_rem");
  hidden = back_rem.getAttribute("hidden");
   
    back_rem.setAttribute("hidden", "hidden");

}
let back_remove = button => {
  let photort = document.getElementById("photo_rt");
  let hidden = photort.getAttribute("hidden");

    photort.setAttribute("hidden", "hidden");

  let back_rem = document.getElementById("back_rem");
  hidden = back_rem.getAttribute("hidden");
     
    back_rem.removeAttribute("hidden", "hidden");
}

let image = document.querySelector('#imagePreview');
let imageSizeLabel = document.querySelector('.imageSizeLabel');
let fullScreenDiv = document.querySelector('.fullScreen');

const defaultSize = '800px';

let imageWidth = image.naturalWidth;
let imageHeight = image.naturalHeight;

fullScreenDiv.onclick = function() {
  image.setAttribute('width', defaultSize);
  imageSizeLabel.innerHTML = '100%';
}

function zoomIn() {
  image.setAttribute('width', String(imageWidth + 50));
  image.setAttribute('height', String(imageWidth + 50));
  const percentIndex = imageSizeLabel.innerHTML.indexOf('%');
  let prevImageSizePercentage = Number(imageSizeLabel.innerHTML.substring(0, percentIndex));
  imageSizeLabel.innerHTML = `${String(prevImageSizePercentage + 20)}%`;
  imageWidth += 50;
}

function zoomOut() {
  image.setAttribute('width', String(imageWidth - 50));
  image.setAttribute('height', String(imageWidth - 50));
  const percentIndex = imageSizeLabel.innerHTML.indexOf('%');
  let prevImageSizePercentage = Number(imageSizeLabel.innerHTML.substring(0, percentIndex));
  imageSizeLabel.innerHTML = `${String(prevImageSizePercentage - 20)}%`;
  imageWidth -= 50;
}

function goToHome() {
  console.log('Clicked on home button!');
}

let imageNameLabel = document.querySelector('.label');

function makeImageNameEditable() {
  const editable = imageNameLabel.getAttribute('contenteditable');
  if (editable === 'true') {
    imageNameLabel.setAttribute('contenteditable', 'false');
  } else {
    imageNameLabel.setAttribute('contenteditable', 'true');
  }
}