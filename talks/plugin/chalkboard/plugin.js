/*****************************************************************
 ** Author: Asvin Goel, goel@telematique.eu
 **
 ** A plugin for reveal.js adding a chalkboard.
 **
 ** Version: 2.1.0
 **
 ** License: MIT license (see LICENSE.md)
 **
 ** Credits:
 ** Chalkboard effect by Mohamed Moustafa https://github.com/mmoustafa/Chalkboard
 ** Multi color support initially added by Kurt Rinnert https://github.com/rinnert
 ** Compatibility with reveal.js v4 by Hakim El Hattab https://github.com/hakimel
 ******************************************************************/

window.RevealChalkboard = window.RevealChalkboard || {
	id: 'RevealChalkboard',
	init: function ( deck ) {
		initChalkboard( deck );
	},
	configure: function ( config ) {
		configure( config );
	},
	toggleNotesCanvas: function () {
		toggleNotesCanvas();
	},
	toggleChalkboard: function () {
		toggleChalkboard();
	},
	colorIndex: function () {
		colorIndex();
	},
	colorNext: function () {
		colorNext();
	},
	colorPrev: function () {
		colorPrev();
	},
	clear: function () {
		clear();
	},
	reset: function () {
		reset();
	},
	resetAll: function () {
		resetAll();
	},
	updateStorage: function () {
		updateStorage();
	},
	getData: function () {
		return getData();
	},
	download: function () {
		download();
	},
};

function scriptPath() {
	// obtain plugin path from the script element
	var src;
	if ( document.currentScript ) {
		src = document.currentScript.src;
	} else {
		var sel = document.querySelector( 'script[src$="/chalkboard/plugin.js"]' )
		if ( sel ) {
			src = sel.src;
		}
	}
	var path = ( src === undefined ) ? "" : src.slice( 0, src.lastIndexOf( "/" ) + 1 );
//console.log("Path: " + path);
	return path;
}
var path = scriptPath();

const initChalkboard = function ( Reveal ) {
//console.warn(path);
	/* Feature detection for passive event handling*/
	var passiveSupported = false;

	try {
		window.addEventListener( 'test', null, Object.defineProperty( {}, 'passive', {
			get: function () {
				passiveSupported = true;
			}
		} ) );
	} catch ( err ) {}


/*****************************************************************
 ** Configuration
 ******************************************************************/
	var background, pen, draw, color;
	var grid = false;
	var boardmarkerWidth = 3;
	var chalkWidth = 7;
	var chalkEffect = 1.0;
	var rememberColor = [ true, false ];
	var eraser = {
		src: path + 'img/sponge.png',
		radius: 20
	};
	var boardmarkers = [ {
			color: 'rgba(100,100,100,1)',
			cursor: 'url(' + path + 'img/boardmarker-black.png), auto'
		},
		{
			color: 'rgba(30,144,255, 1)',
			cursor: 'url(' + path + 'img/boardmarker-blue.png), auto'
		},
		{
			color: 'rgba(220,20,60,1)',
			cursor: 'url(' + path + 'img/boardmarker-red.png), auto'
		},
		{
			color: 'rgba(50,205,50,1)',
			cursor: 'url(' + path + 'img/boardmarker-green.png), auto'
		},
		{
			color: 'rgba(255,140,0,1)',
			cursor: 'url(' + path + 'img/boardmarker-orange.png), auto'
		},
		{
			color: 'rgba(150,0,20150,1)',
			cursor: 'url(' + path + 'img/boardmarker-purple.png), auto'
		},
		{
			color: 'rgba(255,220,0,1)',
			cursor: 'url(' + path + 'img/boardmarker-yellow.png), auto'
		}
	];
	var chalks = [ {
			color: 'rgba(255,255,255,0.5)',
			cursor: 'url(' + path + 'img/chalk-white.png), auto'
		},
		{
			color: 'rgba(96, 154, 244, 0.5)',
			cursor: 'url(' + path + 'img/chalk-blue.png), auto'
		},
		{
			color: 'rgba(237, 20, 28, 0.5)',
			cursor: 'url(' + path + 'img/chalk-red.png), auto'
		},
		{
			color: 'rgba(20, 237, 28, 0.5)',
			cursor: 'url(' + path + 'img/chalk-green.png), auto'
		},
		{
			color: 'rgba(220, 133, 41, 0.5)',
			cursor: 'url(' + path + 'img/chalk-orange.png), auto'
		},
		{
			color: 'rgba(220,0,220,0.5)',
			cursor: 'url(' + path + 'img/chalk-purple.png), auto'
		},
		{
			color: 'rgba(255,220,0,0.5)',
			cursor: 'url(' + path + 'img/chalk-yellow.png), auto'
		}
	];
	var keyBindings = {
		toggleNotesCanvas: {
			keyCode: 67,
			key: 'C',
			description: 'Toggle notes canvas'
		},
		toggleChalkboard: {
			keyCode: 66,
			key: 'B',
			description: 'Toggle chalkboard'
		},
		clear: {
			keyCode: 46,
			key: 'DEL',
			description: 'Clear drawings on slide'
		},
/*
		reset: {
			keyCode: 173,
			key: '-',
			description: 'Reset drawings on slide'
		},
*/
		resetAll: {
			keyCode: 8,
			key: 'BACKSPACE',
			description: 'Reset all drawings'
		},
		colorNext: {
			keyCode: 88,
			key: 'X',
			description: 'Next color'
		},
		colorPrev: {
			keyCode: 89,
			key: 'Y',
			description: 'Previous color'
		},
		download: {
			keyCode: 68,
			key: 'D',
			description: 'Download drawings'
		}
	};


	var theme = 'chalkboard';
	var color = [ 0, 0 ];
	var toggleChalkboardButton = false;
	var toggleNotesButton = false;
	var colorButtons = true;
	var boardHandle = true;
	var transition = 800;

	var readOnly = false;
	var messageType = 'broadcast';

	var config = configure( Reveal.getConfig().chalkboard || {} );
	if ( config.keyBindings ) {
		for ( var key in config.keyBindings ) {
			keyBindings[ key ] = config.keyBindings[ key ];
		};
	}

	function configure( config ) {

		if ( config.boardmarkerWidth || config.penWidth ) boardmarkerWidth = config.boardmarkerWidth || config.penWidth;
		if ( config.chalkWidth ) chalkWidth = config.chalkWidth;
		if ( config.chalkEffect ) chalkEffect = config.chalkEffect;
		if ( config.rememberColor ) rememberColor = config.rememberColor;
		if ( config.eraser ) eraser = config.eraser;
		if ( config.boardmarkers ) boardmarkers = config.boardmarkers;
		if ( config.chalks ) chalks = config.chalks;

		if ( config.theme ) theme = config.theme;
		switch ( theme ) {
		case 'whiteboard':
			background = [ 'rgba(127,127,127,.1)', path + 'img/whiteboard.png' ];
			draw = [ drawWithBoardmarker, drawWithBoardmarker ];
			pens = [ boardmarkers, boardmarkers ];
			grid = {
				color: 'rgb(127,127,255,0.1)',
				distance: 40,
				width: 2
			};
			break;
		case 'chalkboard':
		default:
			background = [ 'rgba(127,127,127,.1)', path + 'img/blackboard.png' ];
			draw = [ drawWithBoardmarker, drawWithChalk ];
			pens = [ boardmarkers, chalks ];
			grid = {
				color: 'rgb(50,50,10,0.5)',
				distance: 80,
				width: 2
			};
		}

		if ( config.background ) background = config.background;
		if ( config.grid != undefined ) grid = config.grid;

		if ( config.toggleChalkboardButton != undefined ) toggleChalkboardButton = config.toggleChalkboardButton;
		if ( config.toggleNotesButton != undefined ) toggleNotesButton = config.toggleNotesButton;
		if ( config.colorButtons != undefined ) colorButtons = config.colorButtons;
		if ( config.boardHandle != undefined ) boardHandle = config.boardHandle;
		if ( config.transition ) transition = config.transition;

		if ( config.readOnly != undefined ) readOnly = config.readOnly;
		if ( config.messageType ) messageType = config.messageType;

		if ( drawingCanvas && ( config.theme || config.background || config.grid ) ) {
			var canvas = document.getElementById( drawingCanvas[ 1 ].id );
			canvas.style.background = 'url("' + background[ 1 ] + '") repeat';
			clearCanvas( 1 );
			drawGrid();
		}

		return config;
	}
/*****************************************************************
 ** Setup
 ******************************************************************/

	function whenReady( callback ) {
		// wait for markdown to be parsed and code to be highlighted
		if ( !document.querySelector( 'section[data-markdown]:not([data-markdown-parsed])' ) 
		     && !document.querySelector( 'code[data-line-numbers*="|"]') 	
		) {
			callback();
		} else {
			console.log( "Wait for markdown to be parsed and code to be highlighted" );
			setTimeout( whenReady, 500, callback )
		}
	}

	function whenLoaded( callback ) {
		// wait for drawings to be loaded and markdown to be parsed
		if ( loaded !== null ) {
			callback();
		} else {
			console.log( "Wait for drawings to be loaded" );
			setTimeout( whenLoaded, 500, callback )
		}
	}

	if ( toggleChalkboardButton ) {
console.warn( "toggleChalkboardButton is deprecated, use customcontrols plugin instead!" );
//console.log("toggleChalkboardButton")
		var button = document.createElement( 'div' );
		button.className = "chalkboard-button";
		button.id = "toggle-chalkboard";
		button.style.visibility = "visible";
		button.style.position = "absolute";
		button.style.zIndex = 30;
		button.style.fontSize = "24px";

		button.style.left = toggleChalkboardButton.left || "30px";
		button.style.bottom = toggleChalkboardButton.bottom || "30px";
		button.style.top = toggleChalkboardButton.top || "auto";
		button.style.right = toggleChalkboardButton.right || "auto";

		button.innerHTML = '<a href="#" title="Toggle chalkboard (' + keyBindings.toggleChalkboard.key + ')" onclick="RevealChalkboard.toggleChalkboard(); return false;"><i class="fa fa-pen-square"></i></a>'
		document.querySelector( ".reveal" ).appendChild( button );
	}
	if ( toggleNotesButton ) {
console.warn( "toggleNotesButton is deprecated, use customcontrols plugin instead!" );
//console.log("toggleNotesButton")
		var button = document.createElement( 'div' );
		button.className = "chalkboard-button";
		button.id = "toggle-notes";
		button.style.position = "absolute";
		button.style.zIndex = 30;
		button.style.fontSize = "24px";

		button.style.left = toggleNotesButton.left || "70px";
		button.style.bottom = toggleNotesButton.bottom || "30px";
		button.style.top = toggleNotesButton.top || "auto";
		button.style.right = toggleNotesButton.right || "auto";

		button.innerHTML = '<a href="#" title="Toggle slide annotation (' + keyBindings.toggleNotesCanvas.key + ')" onclick="RevealChalkboard.toggleNotesCanvas(); return false;"><i class="fa fa-pen"></i></a>'
		document.querySelector( ".reveal" ).appendChild( button );
	}

	var drawingCanvas = [ {
		id: 'notescanvas'
	}, {
		id: 'chalkboard'
	} ];
	setupDrawingCanvas( 0 );
	setupDrawingCanvas( 1 );

	var mode = 0; // 0: notes canvas, 1: chalkboard
	var board = 0; // board index (only for chalkboard)

	var mouseX = 0;
	var mouseY = 0;
	var lastX = null;
	var lastY = null;

	var drawing = false;
	var erasing = false;

	var slideStart = Date.now();
	var slideIndices = {
		h: 0,
		v: 0
	};

	var timeouts = [
		[],
		[]
	];
	var touchTimeout = null;
	var slidechangeTimeout = null;
	var updateStorageTimeout = null;
	var playback = false;

	function createPalette( colors, length ) {
		if ( length === true || length > colors.length ) {
			length = colors.length;
		}
		var palette = document.createElement( 'div' );
		palette.classList.add( 'palette' );
		var list = document.createElement( 'ul' );
		// color pickers
		for ( var i = 0; i < length; i++ ) {
			var colorButton = document.createElement( 'li' );
			colorButton.setAttribute( 'data-color', i );
			colorButton.innerHTML = '<i class="fa fa-square"></i>';
			colorButton.style.color = colors[ i ].color;
			colorButton.addEventListener( 'click', function ( e ) {
				var element = e.target;
				while ( !element.hasAttribute( 'data-color' ) ) {
					element = element.parentElement;
				}
				colorIndex( parseInt( element.getAttribute( 'data-color' ) ) );
			} );
			colorButton.addEventListener( 'touchstart', function ( e ) {
				var element = e.target;
				while ( !element.hasAttribute( 'data-color' ) ) {
					element = element.parentElement;
				}
				colorIndex( parseInt( element.getAttribute( 'data-color' ) ) );
			} );
			list.appendChild( colorButton );
		}
		palette.appendChild( list );
		return palette;
	};

	function switchBoard( boardIdx ) {
		selectBoard( boardIdx, true );
		// broadcast
		var message = new CustomEvent( messageType );
			message.content = {
			sender: 'chalkboard-plugin',
			type: 'selectboard',
			timestamp: Date.now() - slideStart,
			mode,
			board
		};
		document.dispatchEvent( message );	
	}

	function setupDrawingCanvas( id ) {
		var container = document.createElement( 'div' );
		container.id = drawingCanvas[ id ].id;
		container.classList.add( 'overlay' );
		container.setAttribute( 'data-prevent-swipe', 'true' );
		container.oncontextmenu = function () {
			return false;
		}
		container.style.cursor = pens[ id ][ color[ id ] ].cursor;

		drawingCanvas[ id ].width = window.innerWidth;
		drawingCanvas[ id ].height = window.innerHeight;
		drawingCanvas[ id ].scale = 1;
		drawingCanvas[ id ].xOffset = 0;
		drawingCanvas[ id ].yOffset = 0;

		if ( id == "0" ) {
			container.style.background = 'rgba(0,0,0,0)';
			container.style.zIndex = 24;
			container.style.opacity = 1;
			container.style.visibility = 'visible';
			container.style.pointerEvents = 'none';

			var slides = document.querySelector( '.slides' );
			var aspectRatio = Reveal.getConfig().width / Reveal.getConfig().height;
			if ( drawingCanvas[ id ].width > drawingCanvas[ id ].height * aspectRatio ) {
				drawingCanvas[ id ].xOffset = ( drawingCanvas[ id ].width - drawingCanvas[ id ].height * aspectRatio ) / 2;
			} else if ( drawingCanvas[ id ].height > drawingCanvas[ id ].width / aspectRatio ) {
				drawingCanvas[ id ].yOffset = ( drawingCanvas[ id ].height - drawingCanvas[ id ].width / aspectRatio ) / 2;
			}

			if ( colorButtons ) {
				var palette = createPalette( boardmarkers, colorButtons );
				palette.style.visibility = 'hidden'; // only show palette in drawing mode
				container.appendChild( palette );
			}
		} else {
			container.style.background = 'url("' + background[ id ] + '") repeat';
			container.style.zIndex = 26;
			container.style.opacity = 0;
			container.style.visibility = 'hidden';

			if ( colorButtons ) {
				var palette = createPalette( chalks, colorButtons );
				container.appendChild( palette );
			}
			if ( boardHandle ) {
				var handle = document.createElement( 'div' );
				handle.classList.add( 'boardhandle' );
				handle.innerHTML = '<ul><li><a id="previousboard" href="#" title="Previous board"><i class="fas fa-chevron-up"></i></a></li><li><a id="nextboard" href="#" title="Next board"><i class="fas fa-chevron-down"></i></a></li></ul>';
				handle.querySelector( '#previousboard' ).addEventListener( 'click', function ( e ) {
					e.preventDefault();
					switchBoard( board - 1 );
				} );
				handle.querySelector( '#nextboard' ).addEventListener( 'click', function ( e ) {
					e.preventDefault();
					switchBoard( board + 1 );
				} );
				handle.querySelector( '#previousboard' ).addEventListener( 'touchstart', function ( e ) {
					e.preventDefault();
					switchBoard( board - 1 );
				} );
				handle.querySelector( '#nextboard' ).addEventListener( 'touchstart', function ( e ) {
					e.preventDefault();
					switchBoard( board + 1 );
				} );

				container.appendChild( handle );
			}
		}


		var sponge = document.createElement( 'img' );
		sponge.src = eraser.src;
		sponge.id = 'sponge';
		sponge.style.visibility = 'hidden';
		sponge.style.position = 'absolute';
		container.appendChild( sponge );
		drawingCanvas[ id ].sponge = sponge;

		var canvas = document.createElement( 'canvas' );
		canvas.width = drawingCanvas[ id ].width;
		canvas.height = drawingCanvas[ id ].height;
		canvas.setAttribute( 'data-chalkboard', id );
		canvas.style.cursor = pens[ id ][ color[ id ] ].cursor;
		container.appendChild( canvas );
		drawingCanvas[ id ].canvas = canvas;

		drawingCanvas[ id ].context = canvas.getContext( '2d' );

		setupCanvasEvents( container );

		document.querySelector( '.reveal' ).appendChild( container );
		drawingCanvas[ id ].container = container;
	}


/*****************************************************************
 ** Storage
 ******************************************************************/

	var storage = [ {
			width: Reveal.getConfig().width,
			height: Reveal.getConfig().height,
			data: []
		},
		{
			width: Reveal.getConfig().width,
			height: Reveal.getConfig().height,
			data: []
		}
	];

	var loaded = null;

	if ( config.storage ) {
		// Get chalkboard drawings from session storage
		loaded = initStorage( sessionStorage.getItem( config.storage ) );
	}

	if ( !loaded && config.src != null ) {
		// Get chalkboard drawings from the given file
		loadData( config.src );
	}

	/**
	 * Initialize storage.
	 */
	function initStorage( json ) {
		var success = false;
		try {
			var data = JSON.parse( json );
			for ( var id = 0; id < data.length; id++ ) {
				if ( drawingCanvas[ id ].width != data[ id ].width || drawingCanvas[ id ].height != data[ id ].height ) {
					drawingCanvas[ id ].scale = Math.min( drawingCanvas[ id ].width / data[ id ].width, drawingCanvas[ id ].height / data[ id ].height );
					drawingCanvas[ id ].xOffset = ( drawingCanvas[ id ].width - data[ id ].width * drawingCanvas[ id ].scale ) / 2;
					drawingCanvas[ id ].yOffset = ( drawingCanvas[ id ].height - data[ id ].height * drawingCanvas[ id ].scale ) / 2;
				}
				if ( config.readOnly ) {
					drawingCanvas[ id ].container.style.cursor = 'default';
					drawingCanvas[ id ].canvas.style.cursor = 'default';
				}
			}
			success = true;
			storage = data;
		} catch ( err ) {
			console.warn( "Cannot initialise storage!" );
		}
		return success;
	}


	/**
	 * Load data.
	 */
	function loadData( filename ) {
		var xhr = new XMLHttpRequest();
		xhr.onload = function () {
			if ( xhr.readyState === 4 && xhr.status != 404 ) {
				loaded = initStorage( xhr.responseText );
				updateStorage();
				console.log( "Drawings loaded from file" );
			} else {
				config.readOnly = undefined;
				readOnly = undefined;
				console.warn( 'Failed to get file ' + filename + '. ReadyState: ' + xhr.readyState + ', Status: ' + xhr.status );
				loaded = false;
			}
		};

		xhr.open( 'GET', filename, true );
		try {
			xhr.send();
		} catch ( error ) {
			config.readOnly = undefined;
			readOnly = undefined;
			console.warn( 'Failed to get file ' + filename + '. Make sure that the presentation and the file are served by a HTTP server and the file can be found there. ' + error );
			loaded = false;
		}
	}


	function storageChanged( now ) {
		if ( !now ) {
			// create or update timer
			if ( updateStorageTimeout ) {
				clearTimeout( updateStorageTimeout );
			}
			updateStorageTimeout = setTimeout( storageChanged, 1000, true);
		}
		else {
// console.log("Update storage", updateStorageTimeout,  Date.now());
			updateStorage();
			updateStorageTimeout = null;
		}
	}

	function updateStorage() {
		var json = JSON.stringify( storage )
		if ( config.storage ) {
			sessionStorage.setItem( config.storage, json )
		}
		return json;
	}

	function recordEvent( event ) {
//console.log(event);
		event.time = Date.now() - slideStart;
		if ( mode == 1 ) event.board = board;
		var slideData = getSlideData();
		var i = slideData.events.length;
		while ( i > 0 && event.time < slideData.events[ i - 1 ].time ) {
			i--;
		}
		slideData.events.splice( i, 0, event );
		slideData.duration = Math.max( slideData.duration, Date.now() - slideStart ) + 1;

		storageChanged();
	}

	/**
	 * Get data as json string.
	 */
	function getData() {
		// cleanup slide data without events
		for ( var id = 0; id < 2; id++ ) {
			for ( var i = storage[ id ].data.length - 1; i >= 0; i-- ) {
				if ( storage[ id ].data[ i ].events.length == 0 ) {
					storage[ id ].data.splice( i, 1 );
				}
			}
		}

		return updateStorage();
	}

	/**
	 * Download data.
	 */
	function downloadData() {
		var a = document.createElement( 'a' );
		document.body.appendChild( a );
		try {
			a.download = 'chalkboard.json';
			var blob = new Blob( [ getData() ], {
				type: 'application/json'
			} );
			a.href = window.URL.createObjectURL( blob );
		} catch ( error ) {
			a.innerHTML += ' (' + error + ')';
		}
		a.click();
		document.body.removeChild( a );
	}

	/**
	 * Returns data object for the slide with the given indices.
	 */
	function getSlideData( indices, id ) {
		if ( id == undefined ) id = mode;
		if ( !indices ) indices = slideIndices;
		var data;
		for ( var i = 0; i < storage[ id ].data.length; i++ ) {
			if ( storage[ id ].data[ i ].slide.h === indices.h && storage[ id ].data[ i ].slide.v === indices.v && storage[ id ].data[ i ].slide.f === indices.f ) {
				data = storage[ id ].data[ i ];
				return data;
			}
		}
		var page = Number( Reveal.getCurrentSlide().getAttribute('data-pdf-page-number') ); 
//console.log( indices, Reveal.getCurrentSlide() );
		storage[ id ].data.push( {
			slide: indices,
			page,
			events: [],
			duration: 0
		} );
		data = storage[ id ].data[ storage[ id ].data.length - 1 ];
		return data;
	}

	/**
	 * Returns maximum duration of slide playback for both modes
	 */
	function getSlideDuration( indices ) {
		if ( !indices ) indices = slideIndices;
		var duration = 0;
		for ( var id = 0; id < 2; id++ ) {
			for ( var i = 0; i < storage[ id ].data.length; i++ ) {
				if ( storage[ id ].data[ i ].slide.h === indices.h && storage[ id ].data[ i ].slide.v === indices.v && storage[ id ].data[ i ].slide.f === indices.f ) {
					duration = Math.max( duration, storage[ id ].data[ i ].duration );
					break;
				}
			}
		}
//console.log( duration );
		return duration;
	}

/*****************************************************************
 ** Print
 ******************************************************************/
	var printMode = ( /print-pdf/gi ).test( window.location.search );
//console.log("createPrintout" + printMode)

	function addPageNumbers() {
		// determine page number for printouts with fragments serialised
		var slides = Reveal.getSlides();
		var page = 0;
		for ( var i=0; i < slides.length; i++) {
			slides[i].setAttribute('data-pdf-page-number',page.toString());
			// add number of fragments without fragment indices
			var count = slides[i].querySelectorAll('.fragment:not([data-fragment-index])').length;
			var fragments = slides[i].querySelectorAll('.fragment[data-fragment-index]');
			for ( var j=0; j < fragments.length; j++) {
				// increasenumber of fragments by highest fragment index (which start at 0)
				if ( Number(fragments[j].getAttribute('data-fragment-index')) + 1 > count ) {
					count = Number(fragments[j].getAttribute('data-fragment-index')) + 1;
				}
			}
//console.log(count,fragments.length,( slides[i].querySelector('h1,h2,h3,h4')||{}).innerHTML, page); 
			page += count + 1;
		}
	}

	function createPrintout() {
		//console.warn(Reveal.getTotalSlides(),Reveal.getSlidesElement());
		if ( storage[ 1 ].data.length == 0 ) return;
		console.log( 'Create printout(s) for ' + storage[ 1 ].data.length + " slides" );
		drawingCanvas[ 0 ].container.style.opacity = 0; // do not print notes canvas
		drawingCanvas[ 0 ].container.style.visibility = 'hidden';

		var patImg = new Image();
		patImg.onload = function () {
			var slides = Reveal.getSlides();
//console.log(slides);
			for ( var i = storage[ 1 ].data.length - 1; i >= 0; i-- ) {
				console.log( 'Create printout for slide ' + storage[ 1 ].data[ i ].slide.h + '.' + storage[ 1 ].data[ i ].slide.v );
				var slideData = getSlideData( storage[ 1 ].data[ i ].slide, 1 );
				var drawings = createDrawings( slideData, patImg );
//console.log("Page:", storage[ 1 ].data[ i ].page );
//console.log("Slide:", slides[storage[ 1 ].data[ i ].page] );
				addDrawings( slides[storage[ 1 ].data[ i ].page], drawings );

			}
//			Reveal.sync();
		};
		patImg.src = background[ 1 ];
	}


	function cloneCanvas( oldCanvas ) {
		//create a new canvas
		var newCanvas = document.createElement( 'canvas' );
		var context = newCanvas.getContext( '2d' );
		//set dimensions
		newCanvas.width = oldCanvas.width;
		newCanvas.height = oldCanvas.height;
		//apply the old canvas to the new one
		context.drawImage( oldCanvas, 0, 0 );
		//return the new canvas
		return newCanvas;
	}

	function getCanvas( template, container, board ) {
		var idx = container.findIndex( element => element.board === board );
		if ( idx === -1 ) {
			var canvas = cloneCanvas( template );
			if ( !container.length ) {
				idx = 0;
				container.push( {
					board,
					canvas
				} );
			} else if ( board < container[ 0 ].board ) {
				idx = 0;
				container.unshift( {
					board,
					canvas
				} );
			} else if ( board > container[ container.length - 1 ].board ) {
				idx = container.length;
				container.push( {
					board,
					canvas
				} );
			}
		}

		return container[ idx ].canvas;
	}

	function createDrawings( slideData, patImg ) {
		var width = Reveal.getConfig().width;
		var height = Reveal.getConfig().height;
		var scale = 1;
		var xOffset = 0;
		var yOffset = 0;
		if ( width != storage[ 1 ].width || height != storage[ 1 ].height ) {
			scale = Math.min( width / storage[ 1 ].width, height / storage[ 1 ].height );
			xOffset = ( width - storage[ 1 ].width * scale ) / 2;
			yOffset = ( height - storage[ 1 ].height * scale ) / 2;
		}
		mode = 1;
		board = 0;
//		console.log( 'Create printout(s) for slide ', slideData );

		var drawings = [];
		var template = document.createElement( 'canvas' );
		template.width = width;
		template.height = height;

		var imgCtx = template.getContext( '2d' );
		imgCtx.fillStyle = imgCtx.createPattern( patImg, 'repeat' );
		imgCtx.rect( 0, 0, width, height );
		imgCtx.fill();

		for ( var j = 0; j < slideData.events.length; j++ ) {
			switch ( slideData.events[ j ].type ) {
			case 'draw':
				draw[ 1 ]( getCanvas( template, drawings, board ).getContext( '2d' ),
					xOffset + slideData.events[ j ].x1 * scale,
					yOffset + slideData.events[ j ].y1 * scale,
					xOffset + slideData.events[ j ].x2 * scale,
					yOffset + slideData.events[ j ].y2 * scale,
					yOffset + slideData.events[ j ].color
				);
				break;
			case 'erase':
				eraseWithSponge( getCanvas( template, drawings, board ).getContext( '2d' ),
					xOffset + slideData.events[ j ].x * scale,
					yOffset + slideData.events[ j ].y * scale
				);
				break;
			case 'selectboard':
				selectBoard( slideData.events[ j ].board );
				break;
			case 'clear':
				getCanvas( template, drawings, board ).getContext( '2d' ).clearRect( 0, 0, width, height );
				getCanvas( template, drawings, board ).getContext( '2d' ).fill();
				break;
			default:
				break;
			}
		}

		drawings = drawings.sort( ( a, b ) => a.board > b.board && 1 || -1 );

		mode = 0;

		return drawings;
	}

	function addDrawings( slide, drawings ) {
		var parent = slide.parentElement.parentElement;
		var nextSlide = slide.parentElement.nextElementSibling;

		for ( var i = 0; i < drawings.length; i++ ) {
			var newPDFPage = document.createElement( 'div' );
			newPDFPage.classList.add( 'pdf-page' );
			newPDFPage.style.height = Reveal.getConfig().height;
			newPDFPage.append( drawings[ i ].canvas );
//console.log("Add drawing", newPDFPage);
			if ( nextSlide != null ) {
				parent.insertBefore( newPDFPage, nextSlide );
			} else {
				parent.append( newPDFPage );
			}
		}
	}

	/*****************************************************************
	 ** Drawings
	 ******************************************************************/

	function drawWithBoardmarker( context, fromX, fromY, toX, toY, colorIdx ) {
		if ( colorIdx == undefined ) colorIdx = color[ mode ];
		context.lineWidth = boardmarkerWidth;
		context.lineCap = 'round';
		context.strokeStyle = boardmarkers[ colorIdx ].color;
		context.beginPath();
		context.moveTo( fromX, fromY );
		context.lineTo( toX, toY );
		context.stroke();
	}

	function drawWithChalk( context, fromX, fromY, toX, toY, colorIdx ) {
		if ( colorIdx == undefined ) colorIdx = color[ mode ];
		var brushDiameter = chalkWidth;
		context.lineWidth = brushDiameter;
		context.lineCap = 'round';
		context.fillStyle = chalks[ colorIdx ].color; // 'rgba(255,255,255,0.5)';
		context.strokeStyle = chalks[ colorIdx ].color;
		/*var opacity = Math.min(0.8, Math.max(0,color[1].replace(/^.*,(.+)\)/,'$1') - 0.1)) + Math.random()*0.2;*/
		var opacity = 1.0;
		context.strokeStyle = context.strokeStyle.replace( /[\d\.]+\)$/g, opacity + ')' );
		context.beginPath();
		context.moveTo( fromX, fromY );
		context.lineTo( toX, toY );
		context.stroke();
		// Chalk Effect
		var length = Math.round( Math.sqrt( Math.pow( toX - fromX, 2 ) + Math.pow( toY - fromY, 2 ) ) / ( 5 / brushDiameter ) );
		var xUnit = ( toX - fromX ) / length;
		var yUnit = ( toY - fromY ) / length;
		for ( var i = 0; i < length; i++ ) {
			if ( chalkEffect > ( Math.random() * 0.9 ) ) {
				var xCurrent = fromX + ( i * xUnit );
				var yCurrent = fromY + ( i * yUnit );
				var xRandom = xCurrent + ( Math.random() - 0.5 ) * brushDiameter * 1.2;
				var yRandom = yCurrent + ( Math.random() - 0.5 ) * brushDiameter * 1.2;
				context.clearRect( xRandom, yRandom, Math.random() * 2 + 2, Math.random() + 1 );
			}
		}
	}
 
	function eraseWithSponge( context, x, y ) {
		context.save();
		context.beginPath();
		context.arc( x, y, eraser.radius, 0, 2 * Math.PI, false );
		context.clip();
		context.clearRect( x - eraser.radius - 1, y - eraser.radius - 1, eraser.radius * 2 + 2, eraser.radius * 2 + 2 );
		context.restore();
		if ( mode == 1 && grid ) {
			redrawGrid( x, y, eraser.radius );
		}
	}


	/**
	 * Show an overlay for the chalkboard.
	 */
	function showChalkboard() {
//console.log("showChalkboard");
		clearTimeout( touchTimeout );
		touchTimeout = null;
		drawingCanvas[ 0 ].sponge.style.visibility = 'hidden'; // make sure that the sponge from touch events is hidden
		drawingCanvas[ 1 ].sponge.style.visibility = 'hidden'; // make sure that the sponge from touch events is hidden
		drawingCanvas[ 1 ].container.style.opacity = 1;
		drawingCanvas[ 1 ].container.style.visibility = 'visible';
		mode = 1;
	}


	/**
	 * Closes open chalkboard.
	 */
	function closeChalkboard() {
		clearTimeout( touchTimeout );
		touchTimeout = null;
		drawingCanvas[ 0 ].sponge.style.visibility = 'hidden'; // make sure that the sponge from touch events is hidden
		drawingCanvas[ 1 ].sponge.style.visibility = 'hidden'; // make sure that the sponge from touch events is hidden
		drawingCanvas[ 1 ].container.style.opacity = 0;
		drawingCanvas[ 1 ].container.style.visibility = 'hidden';
		lastX = null;
		lastY = null;
		mode = 0;
	}

	/**
	 * Clear current canvas.
	 */
	function clearCanvas( id ) {
		if ( id == 0 ) clearTimeout( slidechangeTimeout );
		drawingCanvas[ id ].context.clearRect( 0, 0, drawingCanvas[ id ].width, drawingCanvas[ id ].height );
		if ( id == 1 && grid ) drawGrid();
	}

	/**
	 * Draw grid on background
	 */
	function drawGrid() {
		var context = drawingCanvas[ 1 ].context;

		drawingCanvas[ 1 ].scale = Math.min( drawingCanvas[ 1 ].width / storage[ 1 ].width, drawingCanvas[ 1 ].height / storage[ 1 ].height );
		drawingCanvas[ 1 ].xOffset = ( drawingCanvas[ 1 ].width - storage[ 1 ].width * drawingCanvas[ 1 ].scale ) / 2;
		drawingCanvas[ 1 ].yOffset = ( drawingCanvas[ 1 ].height - storage[ 1 ].height * drawingCanvas[ 1 ].scale ) / 2;

		var scale = drawingCanvas[ 1 ].scale;
		var xOffset = drawingCanvas[ 1 ].xOffset;
		var yOffset = drawingCanvas[ 1 ].yOffset;

		var distance = grid.distance * scale;

		var fromX = drawingCanvas[ 1 ].width / 2 - distance / 2 - Math.floor( ( drawingCanvas[ 1 ].width - distance ) / 2 / distance ) * distance;
		for ( var x = fromX; x < drawingCanvas[ 1 ].width; x += distance ) {
			context.beginPath();
			context.lineWidth = grid.width * scale;
			context.lineCap = 'round';
			context.fillStyle = grid.color;
			context.strokeStyle = grid.color;
			context.moveTo( x, 0 );
			context.lineTo( x, drawingCanvas[ 1 ].height );
			context.stroke();
		}
		var fromY = drawingCanvas[ 1 ].height / 2 - distance / 2 - Math.floor( ( drawingCanvas[ 1 ].height - distance ) / 2 / distance ) * distance;

		for ( var y = fromY; y < drawingCanvas[ 1 ].height; y += distance ) {
			context.beginPath();
			context.lineWidth = grid.width * scale;
			context.lineCap = 'round';
			context.fillStyle = grid.color;
			context.strokeStyle = grid.color;
			context.moveTo( 0, y );
			context.lineTo( drawingCanvas[ 1 ].width, y );
			context.stroke();
		}
	}

	function redrawGrid( centerX, centerY, diameter ) {
		var context = drawingCanvas[ 1 ].context;

		drawingCanvas[ 1 ].scale = Math.min( drawingCanvas[ 1 ].width / storage[ 1 ].width, drawingCanvas[ 1 ].height / storage[ 1 ].height );
		drawingCanvas[ 1 ].xOffset = ( drawingCanvas[ 1 ].width - storage[ 1 ].width * drawingCanvas[ 1 ].scale ) / 2;
		drawingCanvas[ 1 ].yOffset = ( drawingCanvas[ 1 ].height - storage[ 1 ].height * drawingCanvas[ 1 ].scale ) / 2;

		var scale = drawingCanvas[ 1 ].scale;
		var xOffset = drawingCanvas[ 1 ].xOffset;
		var yOffset = drawingCanvas[ 1 ].yOffset;

		var distance = grid.distance * scale;

		var fromX = drawingCanvas[ 1 ].width / 2 - distance / 2 - Math.floor( ( drawingCanvas[ 1 ].width - distance ) / 2 / distance ) * distance;

		for ( var x = fromX + distance * Math.ceil( ( centerX - diameter - fromX ) / distance ); x <= fromX + distance * Math.floor( ( centerX + diameter - fromX ) / distance ); x += distance ) {
			context.beginPath();
			context.lineWidth = grid.width * scale;
			context.lineCap = 'round';
			context.fillStyle = grid.color;
			context.strokeStyle = grid.color;
			context.moveTo( x, centerY - Math.sqrt( diameter * diameter - ( centerX - x ) * ( centerX - x ) ) );
			context.lineTo( x, centerY + Math.sqrt( diameter * diameter - ( centerX - x ) * ( centerX - x ) ) );
			context.stroke();
		}
		var fromY = drawingCanvas[ 1 ].height / 2 - distance / 2 - Math.floor( ( drawingCanvas[ 1 ].height - distance ) / 2 / distance ) * distance;
		for ( var y = fromY + distance * Math.ceil( ( centerY - diameter - fromY ) / distance ); y <= fromY + distance * Math.floor( ( centerY + diameter - fromY ) / distance ); y += distance ) {
			context.beginPath();
			context.lineWidth = grid.width * scale;
			context.lineCap = 'round';
			context.fillStyle = grid.color;
			context.strokeStyle = grid.color;
			context.moveTo( centerX - Math.sqrt( diameter * diameter - ( centerY - y ) * ( centerY - y ) ), y );
			context.lineTo( centerX + Math.sqrt( diameter * diameter - ( centerY - y ) * ( centerY - y ) ), y );
			context.stroke();
		}
	}

	/**
	 * Set the  color
	 */
	function setColor( index, record ) {
		// protect against out of bounds (this could happen when
		// replaying events recorded with different color settings).
		if ( index >= pens[ mode ].length ) index = 0;
		color[ mode ] = index;
		drawingCanvas[ mode ].canvas.style.cursor = pens[ mode ][ color[ mode ] ].cursor;
	}

	/**
	 * Set the  board
	 */
	function selectBoard( boardIdx, record ) {
//console.log("Set board",boardIdx);
		if ( board == boardIdx ) return;

		board = boardIdx;
		redrawChalkboard( boardIdx );
		if ( record ) {
			recordEvent( { type: 'selectboard' } );
		}
	}

	function redrawChalkboard( boardIdx ) {
		clearCanvas( 1 );
		var slideData = getSlideData( slideIndices, 1 );
		var index = 0;
		var play = ( boardIdx == 0 );
		while ( index < slideData.events.length && slideData.events[ index ].time < Date.now() - slideStart ) {
			if ( boardIdx == slideData.events[ index ].board ) {
				playEvent( 1, slideData.events[ index ], Date.now() - slideStart );
			}

			index++;
		}
	}


	/**
	 * Forward cycle color
	 */
	function cycleColorNext() {
		color[ mode ] = ( color[ mode ] + 1 ) % pens[ mode ].length;
		return color[ mode ];
	}

	/**
	 * Backward cycle color
	 */
	function cycleColorPrev() {
		color[ mode ] = ( color[ mode ] + ( pens[ mode ].length - 1 ) ) % pens[ mode ].length;
		return color[ mode ];
	}

/*****************************************************************
 ** Broadcast
 ******************************************************************/

	var eventQueue = [];

	document.addEventListener( 'received', function ( message ) {
		if ( message.content && message.content.sender == 'chalkboard-plugin' ) {
			// add message to queue
			eventQueue.push( message );
			console.log( JSON.stringify( message ) );
		}
		if ( eventQueue.length == 1 ) processQueue();
	} );

	function processQueue() {
		// take first message from queue
		var message = eventQueue.shift();

		// synchronize time with seminar host
		slideStart = Date.now() - message.content.timestamp;
		// set status
		if ( mode < message.content.mode ) {
			// open chalkboard
			showChalkboard();
		} else if ( mode > message.content.mode ) {
			// close chalkboard
			closeChalkboard();
		}
		if ( board != message.content.board ) {
			board = message.content.board;
			redrawChalkboard( board );
		};

		switch ( message.content.type ) {
		case 'showChalkboard':
			showChalkboard();
			break;
		case 'closeChalkboard':
			closeChalkboard();
			break;
		case 'erase':
			erasePoint( message.content.x, message.content.y );
			break;
		case 'draw':
			drawSegment( message.content.fromX, message.content.fromY, message.content.toX, message.content.toY, message.content.color );
			break;
		case 'clear':
			clearSlide();
			break;
		case 'selectboard':
			selectBoard( message.content.board, true );
			break;
		case 'resetSlide':
			resetSlideDrawings();
			break;
		case 'init':
			storage = message.content.storage;
			for ( var id = 0; id < 2; id++ ) {
				drawingCanvas[ id ].scale = Math.min( drawingCanvas[ id ].width / storage[ id ].width, drawingCanvas[ id ].height / storage[ id ].height );
				drawingCanvas[ id ].xOffset = ( drawingCanvas[ id ].width - storage[ id ].width * drawingCanvas[ id ].scale ) / 2;
				drawingCanvas[ id ].yOffset = ( drawingCanvas[ id ].height - storage[ id ].height * drawingCanvas[ id ].scale ) / 2;
			}
			clearCanvas( 0 );
			clearCanvas( 1 );
			if ( !playback ) {
				slidechangeTimeout = setTimeout( startPlayback, transition, getSlideDuration(), 0 );
			}
			if ( mode == 1 && message.content.mode == 0 ) {
				setTimeout( closeChalkboard, transition + 50 );
			}
			if ( mode == 0 && message.content.mode == 1 ) {
				setTimeout( showChalkboard, transition + 50 );
			}
			mode = message.content.mode;
			board = message.content.board;
			break;
		default:
			break;
		}

		// continue with next message if queued
		if ( eventQueue.length > 0 ) {
			processQueue();
		} else {
			storageChanged();
		}
	}

	document.addEventListener( 'welcome', function ( user ) {
		// broadcast storage
		var message = new CustomEvent( messageType );
		message.content = {
			sender: 'chalkboard-plugin',
			recipient: user.id,
			type: 'init',
			timestamp: Date.now() - slideStart,
			storage: storage,
			mode,
			board
		};
		document.dispatchEvent( message );
	} );

	/*****************************************************************
	 ** Playback
	 ******************************************************************/

	document.addEventListener( 'seekplayback', function ( event ) {
//console.log('event seekplayback ' + event.timestamp);
		stopPlayback();
		if ( !playback || event.timestamp == 0 ) {
			// in other cases startplayback fires after seeked
			startPlayback( event.timestamp );
		}
		//console.log('seeked');
	} );


	document.addEventListener( 'startplayback', function ( event ) {
//console.log('event startplayback ' + event.timestamp);
		stopPlayback();
		playback = true;
		startPlayback( event.timestamp );
	} );

	document.addEventListener( 'stopplayback', function ( event ) {
//console.log('event stopplayback ' + (Date.now() - slideStart) );
		playback = false;
		stopPlayback();
	} );

	document.addEventListener( 'startrecording', function ( event ) {
//console.log('event startrecording ' + event.timestamp);
		startRecording();
	} );


	function startRecording() {
		resetSlide( true );
		slideStart = Date.now();
	}

	function startPlayback( timestamp, finalMode ) {
//console.log("playback " + timestamp );
		slideStart = Date.now() - timestamp;
		closeChalkboard();
		mode = 0;
		board = 0;
		for ( var id = 0; id < 2; id++ ) {
			clearCanvas( id );
			var slideData = getSlideData( slideIndices, id );
//console.log( timestamp +" / " + JSON.stringify(slideData));
			var index = 0;
			while ( index < slideData.events.length && slideData.events[ index ].time < ( Date.now() - slideStart ) ) {
				playEvent( id, slideData.events[ index ], timestamp );
				index++;
			}

			while ( playback && index < slideData.events.length ) {
				timeouts[ id ].push( setTimeout( playEvent, slideData.events[ index ].time - ( Date.now() - slideStart ), id, slideData.events[ index ], timestamp ) );
				index++;
			}
		}
//console.log("Mode: " + finalMode + "/" + mode );
		if ( finalMode != undefined ) {
			mode = finalMode;
		}
		if ( mode == 1 ) showChalkboard();
//console.log("playback (ok)");

	};

	function stopPlayback() {
//console.log("stopPlayback");
//console.log("Timeouts: " + timeouts[0].length + "/"+ timeouts[1].length);
		for ( var id = 0; id < 2; id++ ) {
			for ( var i = 0; i < timeouts[ id ].length; i++ ) {
				clearTimeout( timeouts[ id ][ i ] );
			}
			timeouts[ id ] = [];
		}
	};

	function playEvent( id, event, timestamp ) {
//console.log( timestamp +" / " + JSON.stringify(event));
//console.log( id + ": " + timestamp +" / " +  event.time +" / " + event.type +" / " + mode );
		switch ( event.type ) {
		case 'open':
			if ( timestamp <= event.time ) {
				showChalkboard();
			} else {
				mode = 1;
			}

			break;
		case 'close':
			if ( timestamp < event.time ) {
				closeChalkboard();
			} else {
				mode = 0;
			}
			break;
		case 'clear':
			clearCanvas( id );
			break;
		case 'selectboard':
			selectBoard( event.board );
			break;
		case 'draw':
			drawLine( id, event, timestamp );
			break;
		case 'erase':
			eraseCircle( id, event, timestamp );
			break;
		}
	};

	function drawLine( id, event, timestamp ) {
		var ctx = drawingCanvas[ id ].context;
		var scale = drawingCanvas[ id ].scale;
		var xOffset = drawingCanvas[ id ].xOffset;
		var yOffset = drawingCanvas[ id ].yOffset;
		draw[ id ]( ctx, xOffset + event.x1 * scale, yOffset + event.y1 * scale, xOffset + event.x2 * scale, yOffset + event.y2 * scale, event.color );
	};

	function eraseCircle( id, event, timestamp ) {
		var ctx = drawingCanvas[ id ].context;
		var scale = drawingCanvas[ id ].scale;
		var xOffset = drawingCanvas[ id ].xOffset;
		var yOffset = drawingCanvas[ id ].yOffset;

		eraseWithSponge( ctx, xOffset + event.x * scale, yOffset + event.y * scale );
	};

	function startErasing( x, y ) {
		drawing = false;
		erasing = true;
		drawingCanvas[ mode ].sponge.style.visibility = 'visible';
		erasePoint( x, y );
	}

	function erasePoint( x, y ) {
		var ctx = drawingCanvas[ mode ].context;
		var scale = drawingCanvas[ mode ].scale;
		var xOffset = drawingCanvas[ mode ].xOffset;
		var yOffset = drawingCanvas[ mode ].yOffset;

		// move sponge image
		drawingCanvas[ mode ].sponge.style.left = ( x * scale + xOffset - eraser.radius ) + 'px';
		drawingCanvas[ mode ].sponge.style.top = ( y * scale + yOffset - 2 * eraser.radius ) + 'px';

		recordEvent( {
			type: 'erase',
			x,
			y
		} );

		if (
			x * scale + xOffset > 0 &&
			y * scale + yOffset > 0 &&
			x * scale + xOffset < drawingCanvas[ mode ].width &&
			y * scale + yOffset < drawingCanvas[ mode ].height
		) {
			eraseWithSponge( ctx, x * scale + xOffset, y * scale + yOffset );
		}
	}

	function stopErasing() {
		erasing = false;
		// hide sponge
		drawingCanvas[ mode ].sponge.style.visibility = 'hidden';
	}

	function startDrawing( x, y ) {
		drawing = true;

		var ctx = drawingCanvas[ mode ].context;
		var scale = drawingCanvas[ mode ].scale;
		var xOffset = drawingCanvas[ mode ].xOffset;
		var yOffset = drawingCanvas[ mode ].yOffset;
		lastX = x * scale + xOffset;
		lastY = y * scale + yOffset;
	}

	function drawSegment( fromX, fromY, toX, toY, colorIdx ) {
		var ctx = drawingCanvas[ mode ].context;
		var scale = drawingCanvas[ mode ].scale;
		var xOffset = drawingCanvas[ mode ].xOffset;
		var yOffset = drawingCanvas[ mode ].yOffset;

		recordEvent( {
			type: 'draw',
			color: colorIdx,
			x1: fromX,
			y1: fromY,
			x2: toX,
			y2: toY
		} );

		if (
			fromX * scale + xOffset > 0 &&
			fromY * scale + yOffset > 0 &&
			fromX * scale + xOffset < drawingCanvas[ mode ].width &&
			fromY * scale + yOffset < drawingCanvas[ mode ].height &&
			toX * scale + xOffset > 0 &&
			toY * scale + yOffset > 0 &&
			toX * scale + xOffset < drawingCanvas[ mode ].width &&
			toY * scale + yOffset < drawingCanvas[ mode ].height
		) {
			draw[ mode ]( ctx, fromX * scale + xOffset, fromY * scale + yOffset, toX * scale + xOffset, toY * scale + yOffset, colorIdx );
		}
	}

	function stopDrawing() {
		drawing = false;
	}


/*****************************************************************
 ** User interface
 ******************************************************************/

	function setupCanvasEvents( canvas ) {
// TODO: check all touchevents
		canvas.addEventListener( 'touchstart', function ( evt ) {
			evt.preventDefault();
//console.log("Touch start");
			if ( !readOnly && evt.target.getAttribute( 'data-chalkboard' ) == mode ) {
				var scale = drawingCanvas[ mode ].scale;
				var xOffset = drawingCanvas[ mode ].xOffset;
				var yOffset = drawingCanvas[ mode ].yOffset;

				var touch = evt.touches[ 0 ];
				mouseX = touch.pageX;
				mouseY = touch.pageY;
				startDrawing( ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale );
				touchTimeout = setTimeout( startErasing, 500,  ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale );
			}
		}, passiveSupported ? {
			passive: false
		} : false );

		canvas.addEventListener( 'touchmove', function ( evt ) {
			evt.preventDefault();
//console.log("Touch move");
			clearTimeout( touchTimeout );
			touchTimeout = null;
			if ( drawing || erasing ) {
				var scale = drawingCanvas[ mode ].scale;
				var xOffset = drawingCanvas[ mode ].xOffset;
				var yOffset = drawingCanvas[ mode ].yOffset;

				var touch = evt.touches[ 0 ];
				mouseX = touch.pageX;
				mouseY = touch.pageY;
				if ( mouseY < drawingCanvas[ mode ].height && mouseX < drawingCanvas[ mode ].width ) {
					// move sponge
					if ( event.type == 'erase' ) {
						drawingCanvas[ mode ].sponge.style.left = ( mouseX - eraser.radius ) + 'px';
						drawingCanvas[ mode ].sponge.style.top = ( mouseY - eraser.radius ) + 'px';
					}
				}

				if ( drawing ) {
					drawSegment( ( lastX - xOffset ) / scale, ( lastY - yOffset ) / scale, ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale, color[ mode ] );
					// broadcast
					var message = new CustomEvent( messageType );
					message.content = {
						sender: 'chalkboard-plugin',
						type: 'draw',
						timestamp: Date.now() - slideStart,
						mode,
						board,
						fromX: ( lastX - xOffset ) / scale,
						fromY: ( lastY - yOffset ) / scale,
						toX: ( mouseX - xOffset ) / scale,
						toY: ( mouseY - yOffset ) / scale,
						color: color[ mode ]
					};
					document.dispatchEvent( message );

					lastX = mouseX;
					lastY = mouseY;
				} else {
					erasePoint( ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale );
					// broadcast
					var message = new CustomEvent( messageType );
					message.content = {
						sender: 'chalkboard-plugin',
						type: 'erase',
						timestamp: Date.now() - slideStart,
						mode,
						board,
						x: ( mouseX - xOffset ) / scale,
						y: ( mouseY - yOffset ) / scale
					};
					document.dispatchEvent( message );
				}

			}
		}, false );


		canvas.addEventListener( 'touchend', function ( evt ) {
			evt.preventDefault();
			clearTimeout( touchTimeout );
			touchTimeout = null;
			// hide sponge image
			drawingCanvas[ mode ].sponge.style.visibility = 'hidden';
			stopDrawing();
		}, false );

		canvas.addEventListener( 'mousedown', function ( evt ) {
			evt.preventDefault();
			if ( !readOnly && evt.target.getAttribute( 'data-chalkboard' ) == mode ) {
//console.log( "mousedown: " + evt.button );
				var scale = drawingCanvas[ mode ].scale;
				var xOffset = drawingCanvas[ mode ].xOffset;
				var yOffset = drawingCanvas[ mode ].yOffset;

				mouseX = evt.pageX;
				mouseY = evt.pageY;

				if ( evt.button == 2 || evt.button == 1 ) {
					startErasing( ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale );
					// broadcast
					var message = new CustomEvent( messageType );
					message.content = {
						sender: 'chalkboard-plugin',
						type: 'erase',
						timestamp: Date.now() - slideStart,
						mode,
						board,
						x: ( mouseX - xOffset ) / scale,
						y: ( mouseY - yOffset ) / scale
					};
					document.dispatchEvent( message );
				} else {
					startDrawing( ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale );
				}
			}
		} );

		canvas.addEventListener( 'mousemove', function ( evt ) {
			evt.preventDefault();
//console.log("Mouse move");
			if ( drawing || erasing ) {
				var scale = drawingCanvas[ mode ].scale;
				var xOffset = drawingCanvas[ mode ].xOffset;
				var yOffset = drawingCanvas[ mode ].yOffset;

				mouseX = evt.pageX;
				mouseY = evt.pageY;

				if ( drawing ) {
					drawSegment( ( lastX - xOffset ) / scale, ( lastY - yOffset ) / scale, ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale, color[ mode ] );
					// broadcast
					var message = new CustomEvent( messageType );
					message.content = {
						sender: 'chalkboard-plugin',
						type: 'draw',
						timestamp: Date.now() - slideStart,
						mode,
						board,
						fromX: ( lastX - xOffset ) / scale,
						fromY: ( lastY - yOffset ) / scale,
						toX: ( mouseX - xOffset ) / scale,
						toY: ( mouseY - yOffset ) / scale,
						color: color[ mode ]
					};
					document.dispatchEvent( message );

					lastX = mouseX;
					lastY = mouseY;
				} else {
					erasePoint( ( mouseX - xOffset ) / scale, ( mouseY - yOffset ) / scale );
					// broadcast
					var message = new CustomEvent( messageType );
					message.content = {
						sender: 'chalkboard-plugin',
						type: 'erase',
						timestamp: Date.now() - slideStart,
						mode,
						board,
						x: ( mouseX - xOffset ) / scale,
						y: ( mouseY - yOffset ) / scale
					};
					document.dispatchEvent( message );
				}

			}
		} );


		canvas.addEventListener( 'mouseup', function ( evt ) {
			evt.preventDefault();
			drawingCanvas[ mode ].canvas.style.cursor = pens[ mode ][ color[ mode ] ].cursor;
			if ( drawing || erasing ) {
				stopDrawing();
				stopErasing();
			}
		} );
	}

	function resize() {
//console.log("resize");
		// Resize the canvas and draw everything again
		var timestamp = Date.now() - slideStart;
		if ( !playback ) {
			timestamp = getSlideDuration();
		}

//console.log( drawingCanvas[0].scale + "/" + drawingCanvas[0].xOffset + "/" +drawingCanvas[0].yOffset );
		for ( var id = 0; id < 2; id++ ) {
			drawingCanvas[ id ].width = window.innerWidth;
			drawingCanvas[ id ].height = window.innerHeight;
			drawingCanvas[ id ].canvas.width = drawingCanvas[ id ].width;
			drawingCanvas[ id ].canvas.height = drawingCanvas[ id ].height;
			drawingCanvas[ id ].context.canvas.width = drawingCanvas[ id ].width;
			drawingCanvas[ id ].context.canvas.height = drawingCanvas[ id ].height;

			drawingCanvas[ id ].scale = Math.min( drawingCanvas[ id ].width / storage[ id ].width, drawingCanvas[ id ].height / storage[ id ].height );
			drawingCanvas[ id ].xOffset = ( drawingCanvas[ id ].width - storage[ id ].width * drawingCanvas[ id ].scale ) / 2;
			drawingCanvas[ id ].yOffset = ( drawingCanvas[ id ].height - storage[ id ].height * drawingCanvas[ id ].scale ) / 2;
//console.log( drawingCanvas[id].scale + "/" + drawingCanvas[id].xOffset + "/" +drawingCanvas[id].yOffset );
		}
//console.log( window.innerWidth + "/" + window.innerHeight);
		startPlayback( timestamp, mode, true );
	}

	Reveal.addEventListener( 'pdf-ready', function ( evt ) {
//		console.log( "Create printouts when ready" );
		whenLoaded( createPrintout );
	});

	Reveal.addEventListener( 'ready', function ( evt ) {
//console.log('ready');
		if ( !printMode ) {
			window.addEventListener( 'resize', resize );

			slideStart = Date.now() - getSlideDuration();
			slideIndices = Reveal.getIndices();
			if ( !playback ) {
				startPlayback( getSlideDuration(), 0 );
			}
			if ( Reveal.isAutoSliding() ) {
				var event = new CustomEvent( 'startplayback' );
				event.timestamp = 0;
				document.dispatchEvent( event );
			}
			updateStorage();
			whenReady( addPageNumbers );
		}
	} );
	Reveal.addEventListener( 'slidechanged', function ( evt ) {
//		clearTimeout( slidechangeTimeout );
//console.log('slidechanged');
		if ( !printMode ) {
			slideStart = Date.now() - getSlideDuration();
			slideIndices = Reveal.getIndices();
			closeChalkboard();
			board = 0;
			clearCanvas( 0 );
			clearCanvas( 1 );
			if ( !playback ) {
				slidechangeTimeout = setTimeout( startPlayback, transition, getSlideDuration(), 0 );
			}
			if ( Reveal.isAutoSliding() ) {
				var event = new CustomEvent( 'startplayback' );
				event.timestamp = 0;
				document.dispatchEvent( event );
			}
		}
	} );
	Reveal.addEventListener( 'fragmentshown', function ( evt ) {
//		clearTimeout( slidechangeTimeout );
//console.log('fragmentshown');
		if ( !printMode ) {
			slideStart = Date.now() - getSlideDuration();
			slideIndices = Reveal.getIndices();
			closeChalkboard();
			board = 0;
			clearCanvas( 0 );
			clearCanvas( 1 );
			if ( Reveal.isAutoSliding() ) {
				var event = new CustomEvent( 'startplayback' );
				event.timestamp = 0;
				document.dispatchEvent( event );
			} else if ( !playback ) {
				startPlayback( getSlideDuration(), 0 );
//				closeChalkboard();
			}
		}
	} );
	Reveal.addEventListener( 'fragmenthidden', function ( evt ) {
//		clearTimeout( slidechangeTimeout );
//console.log('fragmenthidden');
		if ( !printMode ) {
			slideStart = Date.now() - getSlideDuration();
			slideIndices = Reveal.getIndices();
			closeChalkboard();
			board = 0;
			clearCanvas( 0 );
			clearCanvas( 1 );
			if ( Reveal.isAutoSliding() ) {
				document.dispatchEvent( new CustomEvent( 'stopplayback' ) );
			} else if ( !playback ) {
				startPlayback( getSlideDuration() );
				closeChalkboard();
			}
		}
	} );

	Reveal.addEventListener( 'autoslideresumed', function ( evt ) {
//console.log('autoslideresumed');
		var event = new CustomEvent( 'startplayback' );
		event.timestamp = 0;
		document.dispatchEvent( event );
	} );
	Reveal.addEventListener( 'autoslidepaused', function ( evt ) {
//console.log('autoslidepaused');
		document.dispatchEvent( new CustomEvent( 'stopplayback' ) );

		// advance to end of slide
//		closeChalkboard();
		startPlayback( getSlideDuration(), 0 );
	} );

	function toggleNotesCanvas() {
		if ( !readOnly ) {
			if ( mode == 1 ) {
				toggleChalkboard();
				notescanvas.style.background = background[ 0 ]; //'rgba(255,0,0,0.5)';
				notescanvas.style.pointerEvents = 'auto';
			}
			else {
				if ( notescanvas.style.pointerEvents != 'none' ) {
					// hide notes canvas
					if ( colorButtons ) {
						notescanvas.querySelector( '.palette' ).style.visibility = 'hidden';
					}
					notescanvas.style.background = 'rgba(0,0,0,0)';
					notescanvas.style.pointerEvents = 'none';
				}
				else {
					// show notes canvas
					if ( colorButtons ) {
						notescanvas.querySelector( '.palette' ).style.visibility = 'visible';
					}
					notescanvas.style.background = background[ 0 ]; //'rgba(255,0,0,0.5)';
					notescanvas.style.pointerEvents = 'auto';

					var idx = 0;
					if ( color[ mode ] ) {
						idx = color[ mode ];
					}

					setColor( idx, true );
				}
			}
		}
	};

	function toggleChalkboard() {
//console.log("toggleChalkboard " + mode);
		if ( mode == 1 ) {
			if ( !readOnly ) {
				recordEvent( { type: 'close' } );
			}
			closeChalkboard();

			// broadcast
			var message = new CustomEvent( messageType );
			message.content = {
				sender: 'chalkboard-plugin',
				type: 'closeChalkboard',
				timestamp: Date.now() - slideStart,
				mode: 0,
				board
			};
			document.dispatchEvent( message );


		} else {
			showChalkboard();
			if ( !readOnly ) {
				recordEvent( { type: 'open' } );
				// broadcast
				var message = new CustomEvent( messageType );
				message.content = {
					sender: 'chalkboard-plugin',
					type: 'showChalkboard',
					timestamp: Date.now() - slideStart,
					mode: 1,
					board
				};
				document.dispatchEvent( message );

				var idx = 0;

				if ( rememberColor[ mode ] ) {
					idx = color[ mode ];
				}

				setColor( idx, true );
			}
		}
	};

	function clearSlide() {
		recordEvent( { type: 'clear' } );
		clearCanvas( mode );
	}

	function clear() {
		if ( !readOnly ) {
			clearSlide();
			// broadcast
			var message = new CustomEvent( messageType );
			message.content = {
				sender: 'chalkboard-plugin',
				type: 'clear',
				timestamp: Date.now() - slideStart,
				mode,
				board
			};
			document.dispatchEvent( message );
		}
	};

	function colorIndex( idx ) {
		if ( !readOnly ) {
			setColor( idx, true );
		}
	}

	function colorNext() {
		if ( !readOnly ) {
			let idx = cycleColorNext();
			setColor( idx, true );
		}
	}

	function colorPrev() {
		if ( !readOnly ) {
			let idx = cycleColorPrev();
			setColor( idx, true );
		}
	}

	function resetSlideDrawings() {
		slideStart = Date.now();
		closeChalkboard();

		clearCanvas( 0 );
		clearCanvas( 1 );

		mode = 1;
		var slideData = getSlideData();
		slideData.duration = 0;
		slideData.events = [];
		mode = 0;
		var slideData = getSlideData();
		slideData.duration = 0;
		slideData.events = [];

		updateStorage();
	}

	function resetSlide( force ) {
		var ok = force || confirm( "Please confirm to delete chalkboard drawings on this slide!" );
		if ( ok ) {
//console.log("resetSlide ");
			stopPlayback();
			resetSlideDrawings();
			// broadcast
			var message = new CustomEvent( messageType );
			message.content = {
				sender: 'chalkboard-plugin',
				type: 'resetSlide',
				timestamp: Date.now() - slideStart,
				mode,
				board
			};
			document.dispatchEvent( message );
		}
	};

	function resetStorage( force ) {
		var ok = force || confirm( "Please confirm to delete all chalkboard drawings!" );
		if ( ok ) {
			stopPlayback();
			slideStart = Date.now();
			clearCanvas( 0 );
			clearCanvas( 1 );
			if ( mode == 1 ) {
				closeChalkboard();
			}

			storage = [ {
					width: Reveal.getConfig().width,
					height: Reveal.getConfig().height,
					data: []
				},
				{
					width: Reveal.getConfig().width,
					height: Reveal.getConfig().height,
					data: []
				}
			];

			if ( config.storage ) {
				sessionStorage.setItem( config.storage, null )
			}
			// broadcast
			var message = new CustomEvent( messageType );
			message.content = {
				sender: 'chalkboard-plugin',
				type: 'init',
				timestamp: Date.now() - slideStart,
				storage,
				mode,
				board
			};
			document.dispatchEvent( message );
		}
	};

	this.toggleNotesCanvas = toggleNotesCanvas;
	this.toggleChalkboard = toggleChalkboard;
	this.colorIndex = colorIndex;
	this.colorNext = colorNext;
	this.colorPrev = colorPrev;
	this.clear = clear;
	this.reset = resetSlide;
	this.resetAll = resetStorage;
	this.download = downloadData;
	this.updateStorage = updateStorage;
	this.getData = getData;
	this.configure = configure;


	for ( var key in keyBindings ) {
		if ( keyBindings[ key ] ) {
			Reveal.addKeyBinding( keyBindings[ key ], RevealChalkboard[ key ] );
		}
	};

	return this;
};
