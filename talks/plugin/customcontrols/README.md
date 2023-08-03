# Custom controls

This plugin allows to add responsive custom controls to reveal.js which allow arbitrary positioning, layout, and behaviour of the controls.

[Check out the live demo](https://rajgoel.github.io/reveal.js-demos/customcontrols-demo.html)


## Installation

Copy the files `plugin.js` and `style.css` into the plugin folder of your reveal.js presentation, i.e. ```plugin/customcontrols``` and load the plugin as shown below.

```html
<link rel="stylesheet" href="plugin/customcontrols/style.css">
<script src="plugin/customcontrols/plugin.js"></script>

<script>
    Reveal.initialize({
        // ...
        plugins: [ RevealCustomControls ],
        // ...
    });
</script>
```

Note, without configuration you need to add

```javascript
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
```

between ```<head>``` and ```</head>``` of your HTML file because the defaults use [Font Awesome](http://fontawesome.io/).



## Configuration

The plugin can be configured by adding custom controls and changing the layout of the slide number, e.g., by:


```javascript
Reveal.initialize({
	// ...
  customcontrols: {
		controls: [
      {
			  id: 'toggle-overview',
			  title: 'Toggle overview (O)',
			  icon: '<i class="fa fa-th"></i>',
			  action: 'Reveal.toggleOverview();'
			},
			{ icon: '<i class="fa fa-pen-square"></i>',
			  title: 'Toggle chalkboard (B)',
			  action: 'RevealChalkboard.toggleChalkboard();'
			},
			{ icon: '<i class="fa fa-pen"></i>',
			  title: 'Toggle notes canvas (C)',
			  action: 'RevealChalkboard.toggleNotesCanvas();'
			}
		]
	},
	// ...

});
```

The `id` and `title` are optional. The configuration should be self explaining and any number of controls can be added. The style file can be altered to control the layout and responsiveness of the custom controls.

## License

MIT licensed

Copyright (C) 2020 Asvin Goel
