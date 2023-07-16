/**
 * Effective-tabs.js v1.0.0
 * http://www.geekslabs.com
 * Copyright 2015, GeeksLabs
 */
;( function( window ) {

	'use strict';

	function extend( a, b ) {
		for( var key in b ) {
			if( b.hasOwnProperty( key ) ) {
				a[key] = b[key];
			}
		}
		return a;
	}

	function efTabs( el, options ) {
		this.el = el;
		this.options = extend( {}, this.options );
  		extend( this.options, options );
  		this._init();
	}

	efTabs.prototype.options = {
		start : 0
	};

	efTabs.prototype._init = function() {
		// tabs elems
		this.tabs = [].slice.call( this.el.querySelectorAll( 'nav > ul > li' ) );
		// content items
		this.items = [].slice.call( this.el.querySelectorAll( '.content-wrap > section' ) );
		// current index
		this.current = -1;
		// show current content item
		this._show();
		// init events
		this._initEvents();
	};

	efTabs.prototype._initEvents = function() {
		var self = this;
		this.tabs.forEach( function( tab, idx ) {
			tab.addEventListener( 'click', function( ev ) {
				ev.preventDefault();
				self._show( idx );
			} );
		} );
	};

	efTabs.prototype._show = function( idx ) {
		if( this.current >= 0 ) {
			this.tabs[ this.current ].className = this.items[ this.current ].className = '';
		}

		this._transitions( this.current,idx );

		// change current
		this.current = idx != undefined ? idx : this.options.start >= 0 && this.options.start < this.items.length ? this.options.start : 0;
		this.tabs[ this.current ].className = 'tab-current';
		this.items[ this.current ].className = 'content-current';
	};

	efTabs.prototype._transitions = function( last, current){
		var last_sec = this.items[ last ],
		current_sec = this.items[ current ];
		if(last == -1){
			this.items[0].style.display = "block";
		}
		else{
			$(last_sec).transition({
				opacity:0, scale:0.5, speed: 500
			});
			current_sec.style.display = "block";
			$(current_sec)
			.delay(300)
			.css({opacity:0})
			.transition({
				opacity:1, scale:1, speed:300
			});
		}
	};
	// add to global namespace
	window.efTabs = efTabs;

})( window );

$(document).ready(function(){
	[].slice.call( document.querySelectorAll( '.ef-tabs' ) ).forEach( function( el ) {
		new efTabs( el );
	});

	//$('.ef-tabs li a').click(function(){

		// Rotate
		/*$('.content-wrap')
		.css({ transformOrigin: '0 0' })
		.transition({
			opacity:0.1, rotate:90
		})
		.transition({
			opacity:1, rotate:0, speed:600
		});*/

		/*$('.content-wrap')
		.css({ transformOrigin: '0 0' })
		.transition({
			opacity:0.8, rotateX:-90, speed: 400
		})
		.transition({
			opacity:1, rotateX:0, speed:500
		});*/

		// Scale
		/*$('.content-wrap')
		.transition({
			opacity:0.5, scale:0.5, speed: 500
		})
		.transition({
			opacity:1, scale:1, speed:300
		});*/

	//});
});