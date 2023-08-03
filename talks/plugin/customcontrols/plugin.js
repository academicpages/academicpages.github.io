/*****************************************************************
** Author: Asvin Goel, goel@telematique.eu
**
** A plugin replacing the default controls by custom controls.
**
** Version: 2.0.0
** 
** License: MIT license (see LICENSE.md)
**
******************************************************************/
window.RevealCustomControls = window.RevealCustomControls || {
    id: 'RevealCustomControls',
    init: function(deck) {
        initCustomControls(deck);
    }
};

const initCustomControls = function(Reveal){
	var config = Reveal.getConfig().customcontrols || {};

	var collapseIcon = config.collapseIcon || '<i class="fa fa-chevron-down"></i>';
	var expandIcon = config.expandIcon || '<i class="fa fa-chevron-up"></i>';
	var tooltip = config.tooltip || 'Show/hide controls';

	var div = document.createElement( 'div' );
	div.id = 'customcontrols';

	var toggleButton = document.createElement( 'button' );
	toggleButton.title = tooltip;
	toggleButton.innerHTML = '<span id="collapse-customcontrols">' + collapseIcon + '</span>' + '<span id="expand-customcontrols">' + expandIcon + '</span>';

	toggleButton.addEventListener('click', function( event ) {
		var div = document.querySelector("div#customcontrols");
		if ( div.classList.contains('collapsed') ) {
			div.classList.remove('collapsed');
		}
		else {
			div.classList.add('collapsed');
		}
		toggleButton.blur(); // unfocus button
	});

	div.appendChild(toggleButton);

	var controls = document.createElement( 'ul' );
	for (var i = 0; i < config.controls.length; i++ ) {
		var control = document.createElement( 'li' );
		if ( config.controls[i].id ) {
			control.id = config.controls[i].id;
		}
		control.innerHTML = '<button ' + ( config.controls[i].title ? 'title="' + config.controls[i].title + '" ': '' ) + 'onclick="' + config.controls[i].action + '">' + config.controls[i].icon + '</button>';
		controls.appendChild( control );
	}
	div.appendChild( controls );


	document.querySelector(".reveal").appendChild( div );

	document.addEventListener( 'resize', function( event ) {
		// expand controls to make sure they are visible
		var div = document.querySelector("div#customcontrols.collapsed");
		if ( div ) {
			div.classList.remove('collapsed');
		}
	} );

	return this;

};

