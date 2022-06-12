# Dics: Definitive Image Comparison Slider

<a target="_blank" href="http://codictados.com"><img
src="http://codictados.com/wp-content/uploads/2015/07/logo263x781.png"
alt="Codictados"></a>

Made by <a href="http://abelcabezaroman.com/" target="_blank">Abel Cabeza Román</a>, a
<a href="http://codictados.com">Codictados</a> developer.

## DEMO

<a target="_blank"
href="http://codictados.com/portfolio/definitive-image-comparison-slider-demo/">See
examples</a>

## Description

Light Vanilla Javascript library (8kb minified) to compare multiples images with
sliders. Also, you can add text and filters to your images.

## Installation

Download the library.

```bash
npm i dics
```

And import it to your project.

```html
<link rel="stylesheet" href="dics.css">
<script src="dics.js"></script>
```

## Usage

You only have to create a container and add your images. You can add all
images you want!! If you add the `alt` attribute, you will view the text
in the image comparison.

```html
<div class="b-dics">
    <img src="01.jpg">
    <img src="02.jpg" alt="Japan Yellow">
    <img src="03.jpg" alt="Japan Orange">
    <img src="04.jpg" alt="Japan Black & White">
</div>
```

Finally, you need to initialize the component like this.

```javascript
new Dics({
    container: document.querySelector('.b-dics')
});
```

Or this.

```javascript
new Dics({
    container: document.querySelectorAll('.b-dics'),
    linesOrientation: 'vertical',
    textPosition: 'left',
    arrayBackgroundColorText: ['#000000', '#FFFFFF'],
    arrayColorText: ['#FFFFFF', '#000000'],
    linesColor: 'rgb(0,0,0)'
});
```

## Options

If you want you can include different options.

| Option | Description | Example |
| --- | --- | --- |
| container | **REQUIRED**: HTML container | `document.querySelector('.b-dics')` |
| filters | Array of CSS string filters  |`['blur(3px)', 'grayscale(1)', 'sepia(1)', 'saturate(3)']` |
| hideTexts | Show text only when you hover the image container |`true`,`false`|
| textPosition | Set the prefer text position  |`'center'`,`'top'`, `'right'`, `'bottom'`, `'left'` |
| linesOrientation | Change the orientation of lines  |`'horizontal'`,`'vertical'` |
| rotate | Rotate the image container (not too useful but it's a beatiful effect. String of rotate CSS rule)  |`'45deg'`|
| arrayBackgroundColorText | Change the bacground-color of sections texts with an array |`['#000000', '#FFFFFF']`|
| arrayColorText | Change the color of texts with an array  |`['#FFFFFF', '#000000']`|
| linesColor | Change the lines and arrows color  |`'rgb(0,0,0)'`|


## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.