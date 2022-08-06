/*
 * VenoBox - jQuery Plugin
 * version: 1.8.9
 * @requires jQuery >= 1.7.0
 *
 * Examples at http://veno.es/venobox/
 * License: MIT License
 * License URI: https://github.com/nicolafranchini/VenoBox/blob/master/LICENSE
 * Copyright 2013-2020 Nicola Franchini - @nicolafranchini
 *
 */

/* global jQuery */

(function($){
    "use strict";
    var autoplay, bgcolor, blockleft, blocknum, blockshare, blocktitle, border, core, container, content, dest, extraCss,
        framewidth, frameheight, gallItems, infinigall, items, keyNavigationDisabled, margine, numeratio,
        overlayColor, overlay, title, thisgall, thenext, theprev, nextok, prevok, preloader, $preloader, navigation,
        obj, gallIndex, startouch, vbheader, images, startY, startX, endY, endX, diff, diffX, diffY, threshold,
        share, sharelinks, vbfooter, sharepos;

    var pinIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.372-12 12 0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146 1.124.347 2.317.535 3.554.535 6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z" fill-rule="evenodd" clip-rule="evenodd"/></svg>';
    var fbIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm3 8h-1.35c-.538 0-.65.221-.65.778v1.222h2l-.209 2h-1.791v7h-3v-7h-2v-2h2v-2.308c0-1.769.931-2.692 3.029-2.692h1.971v3z"/></svg>';
    var twitterIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm6.066 9.645c.183 4.04-2.83 8.544-8.164 8.544-1.622 0-3.131-.476-4.402-1.291 1.524.18 3.045-.244 4.252-1.189-1.256-.023-2.317-.854-2.684-1.995.451.086.895.061 1.298-.049-1.381-.278-2.335-1.522-2.304-2.853.388.215.83.344 1.301.359-1.279-.855-1.641-2.544-.889-3.835 1.416 1.738 3.533 2.881 5.92 3.001-.419-1.796.944-3.527 2.799-3.527.825 0 1.572.349 2.096.907.654-.128 1.27-.368 1.824-.697-.215.671-.67 1.233-1.263 1.589.581-.07 1.135-.224 1.649-.453-.384.578-.87 1.084-1.433 1.489z"/></svg>';
    var linkedinIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2 16h-2v-6h2v6zm-1-6.891c-.607 0-1.1-.496-1.1-1.109 0-.612.492-1.109 1.1-1.109s1.1.497 1.1 1.109c0 .613-.493 1.109-1.1 1.109zm8 6.891h-1.998v-2.861c0-1.881-2.002-1.722-2.002 0v2.861h-2v-6h2v1.093c.872-1.616 4-1.736 4 1.548v3.359z"/></svg>';
    var downloadIcon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm2 9h-4v-1h4v1zm0-3v1h-4v-1h4zm-2 13l-6-6h4v-3h4v3h4l-6 6z"/></svg>';
   
    $.fn.extend({
        //plugin name - venobox
        venobox: function(options) {
            var plugin = this;
            // default options
            var defaults = {
                arrowsColor : '#B6B6B6',
                autoplay : false, // same as data-autoplay - thanks @codibit
                bgcolor: '#fff',
                border: '0',
                closeBackground : 'transparent',
                closeColor : "#d2d2d2",
                framewidth: '',
                frameheight: '',
                gallItems: false,
                infinigall: false,
                htmlClose : '&times;',
                htmlNext : '<span>Next</span>',
                htmlPrev : '<span>Prev</span>',
                numeratio: false,
                numerationBackground : '#161617',
                numerationColor : '#d2d2d2',
                numerationPosition : 'top', // 'top' || 'bottom'
                overlayClose: true, // disable overlay click-close - thanx @martybalandis
                overlayColor : 'rgba(23,23,23,0.85)',
                spinner : 'double-bounce', // available: 'rotating-plane' | 'double-bounce' | 'wave' | 'wandering-cubes' | 'spinner-pulse' | 'chasing-dots' | 'three-bounce' | 'circle' | 'cube-grid' | 'fading-circle' | 'folding-cube'
                spinColor : '#d2d2d2',
                titleattr: 'title', // specific attribute to get a title (e.g. [data-title]) - thanx @mendezcode
                titleBackground: '#161617',
                titleColor: '#d2d2d2',
                titlePosition : 'top', // 'top' || 'bottom'
                share: [ 'facebook', 'twitter', 'linkedin', 'pinterest', 'download' ], 
                cb_pre_open: function(){ return true; }, // Callbacks - thanx @garyee
                cb_post_open: function(){},
                cb_pre_close: function(){ return true; },
                cb_post_close: function(){},
                cb_post_resize: function(){},
                cb_after_nav: function(){},
                cb_content_loaded: function(){},
                cb_init: function(){}
            };

            var option = $.extend(defaults, options);

            // callback plugin initialization
            option.cb_init(plugin);

            return this.each(function() {

                obj = $(this);

                // Prevent double initialization - thanx @matthistuff
                if (obj.data('venobox')) {
                  return true;
                }

                // method to be used outside the plugin
                plugin.VBclose = function() {
                    closeVbox();
                };
                obj.addClass('vbox-item');
                obj.data('framewidth', option.framewidth);
                obj.data('frameheight', option.frameheight);
                obj.data('border', option.border);
                obj.data('bgcolor', option.bgcolor);
                obj.data('numeratio', option.numeratio);
                obj.data('gallItems', option.gallItems);
                obj.data('infinigall', option.infinigall);
                obj.data('overlaycolor', option.overlayColor);
                obj.data('titleattr', option.titleattr);
                obj.data('share', option.share);

                obj.data('venobox', true);

                obj.on('click', function(e){

                    e.preventDefault();
                    obj = $(this);

                    // callback plugin initialization
                    var cb_pre_open = option.cb_pre_open(obj);

                    if (cb_pre_open === false) {
                      return false;
                    }

                    // methods to be used outside the plugin
                    plugin.VBnext = function() {
                        navigateGall(thenext);
                    };
                    plugin.VBprev = function() {
                        navigateGall(theprev);
                    };

                    overlayColor = obj.data('overlay') || obj.data('overlaycolor');

                    framewidth = obj.data('framewidth');
                    frameheight = obj.data('frameheight');
                    // set data-autoplay="true" for vimeo and youtube videos - thanx @zehfernandes
                    autoplay = obj.data('autoplay') || option.autoplay;
                    border = obj.data('border');
                    bgcolor = obj.data('bgcolor');
                    nextok = false;
                    prevok = false;
                    keyNavigationDisabled = false;

                    // set a different url to be loaded using data-href="" - thanx @pixeline
                    dest = obj.data('href') || obj.attr('href');
                    extraCss = obj.data( 'css' ) || '';
                    title = obj.attr(obj.data('titleattr')) || '';
                    share = obj.data('share');
                    
                    preloader = '<div class="vbox-preloader">';

                    switch (option.spinner) {

                        case 'rotating-plane':
                            preloader += '<div class="sk-rotating-plane"></div>';
                            break;
                        case 'double-bounce':
                            preloader += '<div class="sk-double-bounce">'+
                            '<div class="sk-child sk-double-bounce1"></div>'+
                            '<div class="sk-child sk-double-bounce2"></div>'+
                            '</div>';
                            break;
                        case 'wave':
                            preloader += '<div class="sk-wave">'+
                            '<div class="sk-rect sk-rect1"></div>'+
                            '<div class="sk-rect sk-rect2"></div>'+
                            '<div class="sk-rect sk-rect3"></div>'+
                            '<div class="sk-rect sk-rect4"></div>'+
                            '<div class="sk-rect sk-rect5"></div>'+
                            '</div>';
                            break;
                        case 'wandering-cubes':
                            preloader += '<div class="sk-wandering-cubes">'+
                            '<div class="sk-cube sk-cube1"></div>'+
                            '<div class="sk-cube sk-cube2"></div>'+
                            '</div>';
                            break;
                          case 'spinner-pulse':
                            preloader += '<div class="sk-spinner sk-spinner-pulse"></div>';
                            break;
                        case 'chasing-dots':
                            preloader += '<div class="sk-chasing-dots">'+
                            '<div class="sk-child sk-dot1"></div>'+
                            '<div class="sk-child sk-dot2"></div>'+
                            '</div>';
                            break;
                        case 'three-bounce':
                            preloader += '<div class="sk-three-bounce">'+
                            '<div class="sk-child sk-bounce1"></div>'+
                            '<div class="sk-child sk-bounce2"></div>'+
                            '<div class="sk-child sk-bounce3"></div>'+
                            '</div>';
                            break;
                        case 'circle':
                            preloader += '<div class="sk-circle">'+
                            '<div class="sk-circle1 sk-child"></div>'+
                            '<div class="sk-circle2 sk-child"></div>'+
                            '<div class="sk-circle3 sk-child"></div>'+
                            '<div class="sk-circle4 sk-child"></div>'+
                            '<div class="sk-circle5 sk-child"></div>'+
                            '<div class="sk-circle6 sk-child"></div>'+
                            '<div class="sk-circle7 sk-child"></div>'+
                            '<div class="sk-circle8 sk-child"></div>'+
                            '<div class="sk-circle9 sk-child"></div>'+
                            '<div class="sk-circle10 sk-child"></div>'+
                            '<div class="sk-circle11 sk-child"></div>'+
                            '<div class="sk-circle12 sk-child"></div>'+
                            '</div>';
                            break;
                        case 'cube-grid':
                            preloader += '<div class="sk-cube-grid">'+
                            '<div class="sk-cube sk-cube1"></div>'+
                            '<div class="sk-cube sk-cube2"></div>'+
                            '<div class="sk-cube sk-cube3"></div>'+
                            '<div class="sk-cube sk-cube4"></div>'+
                            '<div class="sk-cube sk-cube5"></div>'+
                            '<div class="sk-cube sk-cube6"></div>'+
                            '<div class="sk-cube sk-cube7"></div>'+
                            '<div class="sk-cube sk-cube8"></div>'+
                            '<div class="sk-cube sk-cube9"></div>'+
                            '</div>';
                            break;
                        case 'fading-circle':
                            preloader += '<div class="sk-fading-circle">'+
                            '<div class="sk-circle1 sk-circle"></div>'+
                            '<div class="sk-circle2 sk-circle"></div>'+
                            '<div class="sk-circle3 sk-circle"></div>'+
                            '<div class="sk-circle4 sk-circle"></div>'+
                            '<div class="sk-circle5 sk-circle"></div>'+
                            '<div class="sk-circle6 sk-circle"></div>'+
                            '<div class="sk-circle7 sk-circle"></div>'+
                            '<div class="sk-circle8 sk-circle"></div>'+
                            '<div class="sk-circle9 sk-circle"></div>'+
                            '<div class="sk-circle10 sk-circle"></div>'+
                            '<div class="sk-circle11 sk-circle"></div>'+
                            '<div class="sk-circle12 sk-circle"></div>'+
                            '</div>';
                            break;
                        case 'folding-cube':
                            preloader += '<div class="sk-folding-cube">'+
                            '<div class="sk-cube1 sk-cube"></div>'+
                            '<div class="sk-cube2 sk-cube"></div>'+
                            '<div class="sk-cube4 sk-cube"></div>'+
                            '<div class="sk-cube3 sk-cube"></div>'+
                            '</div>';
                            break;
                    }
                    preloader += '</div>';

                    navigation = '<a class="vbox-next">' + option.htmlNext + '</a><a class="vbox-prev">' + option.htmlPrev + '</a>';
                    vbheader = '<div class="vbox-title"></div><div class="vbox-left"><div class="vbox-num">0/0</div></div><div class="vbox-close">' + option.htmlClose + '</div>';
                    vbfooter = '<div class="vbox-share"></div>';

                    core = '<div class="vbox-overlay ' + extraCss + '" style="background:'+ overlayColor +'">'+
                    preloader + '<div class="vbox-container"><div class="vbox-content"></div></div>' + vbheader + navigation + vbfooter + '</div>';

                    $('body').append(core).addClass('vbox-open');

                    $('.vbox-preloader div:not(.sk-circle) .sk-child, .vbox-preloader .sk-rotating-plane, .vbox-preloader .sk-rect, .vbox-preloader div:not(.sk-folding-cube) .sk-cube, .vbox-preloader .sk-spinner-pulse').css('background-color', option.spinColor);

                    overlay = $('.vbox-overlay');
                    container = $('.vbox-container');
                    content = $('.vbox-content');
                    blockleft = $('.vbox-left');
                    blocknum = $('.vbox-num');
                    blockshare = $('.vbox-share');
                    blocktitle = $('.vbox-title');
                    $preloader = $('.vbox-preloader');

                    $preloader.show();

                    if (option.titlePosition == 'top') {
                        sharepos = 'bottom';
                    } else {
                        sharepos = 'top';
                    }
                    blockshare.css(sharepos, '-1px');
                    blockshare.css({
                      'color' : option.titleColor,
                      'fill' : option.titleColor,
                      'background-color' : option.titleBackground
                    });

                    blocktitle.css(option.titlePosition, '-1px',);

                    blocktitle.css({
                      'color' : option.titleColor,
                      'background-color' : option.titleBackground
                    });

                    $('.vbox-close').css({
                      'color' : option.closeColor,
                      'background-color' : option.closeBackground
                    });

                    blockleft.css(option.numerationPosition, '-1px');
                    blockleft.css({
                      'color' : option.numerationColor,
                      'background-color' : option.numerationBackground
                    });

                    $('.vbox-next span, .vbox-prev span').css({
                      'border-top-color' : option.arrowsColor,
                      'border-right-color' : option.arrowsColor
                    });

                    content.html('');
                    content.css('opacity', '0');
                    overlay.css('opacity', '0');

                    checknav();

                    // fade in overlay
                    overlay.animate({opacity:1}, 250, function(){

                        if (obj.data('vbtype') == 'iframe') {
                          loadIframe();
                        } else if (obj.data('vbtype') == 'inline') {
                          loadInline();
                        } else if (obj.data('vbtype') == 'ajax') {
                          loadAjax();
                        } else if (obj.data('vbtype') == 'video') {
                          loadVid(autoplay);
                        } else {
                          content.html('<img src="'+dest+'">');
                          preloadFirst();
                        }
                        option.cb_post_open(obj, gallIndex, thenext, theprev);
                    });

                    /* -------- KEYBOARD ACTIONS -------- */
                    $('body').keydown(keyboardHandler);

                    /* -------- PREVGALL -------- */
                    $('.vbox-prev').on('click', function(){
                        navigateGall(theprev);
                    });
                    /* -------- NEXTGALL -------- */
                    $('.vbox-next').on('click', function(){
                        navigateGall(thenext);
                    });

                    return false;

                }); // click

                /* -------- CHECK NEXT / PREV -------- */
                function checknav(){

                    thisgall = obj.data('gall');
                    numeratio = obj.data('numeratio');
                    gallItems = obj.data('gallItems');
                    infinigall = obj.data('infinigall');
                    share = obj.data('share');
                    blockshare.html('');
                    if ( obj.data('vbtype') !== 'iframe' && obj.data('vbtype') !== 'inline' && obj.data('vbtype') !== 'ajax' ) {
                        sharelinks = { 
                            pinterest : '<a target="_blank" href="https://pinterest.com/pin/create/button/?url='+obj.prop('href')+'&media='+obj.prop('href')+'&description='+title+'">'+pinIcon+'</a>', 
                            facebook  : '<a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u='+obj.prop('href')+'">'+fbIcon+'</a>', 
                            twitter   : '<a target="_blank" href="https://twitter.com/intent/tweet?text='+title+'&url='+obj.prop('href')+'">'+twitterIcon+'</a>', 
                            linkedin  : '<a target="_blank" href="https://www.linkedin.com/sharing/share-offsite/?url='+obj.prop('href')+'">'+linkedinIcon+'</a>',
                            download  : '<a target="_blank" href="'+obj.prop('href')+'">'+downloadIcon+'</a>'
                        };
                        $.each( share, function( key, value ) {
                            blockshare.append(sharelinks[value]);
                        });
                    }

                    if (gallItems) {
                        items = gallItems;
                    } else {
                        items = $('.vbox-item[data-gall="' + thisgall + '"]');
                    }

                    if (items.length < 2) {
                        infinigall = false;
                        numeratio = false;
                    }

                    thenext = items.eq( items.index(obj) + 1 );
                    theprev = items.eq( items.index(obj) - 1 );

                    if (!thenext.length && infinigall === true) {
                      thenext = items.eq(0);
                    }

                    // update gall numeration
                    if (items.length >= 1) {
                      gallIndex = items.index(obj)+1;
                      blocknum.html(gallIndex + ' / ' + items.length);
                    } else {
                      gallIndex = 1;
                    }
                    if (numeratio === true) {
                      blocknum.show();
                    } else {
                      blocknum.hide();
                    }

                    // update title
                    if (title !== '') {
                      blocktitle.show();
                    } else {
                      blocktitle.hide();
                    }

                    // update navigation arrows
                    if (!thenext.length && infinigall !== true) {
                      $('.vbox-next').css('display', 'none');
                      nextok = false;
                    } else {
                      $('.vbox-next').css('display', 'block');
                      nextok = true;
                    }

                    if (items.index(obj) > 0 || infinigall === true) {
                      $('.vbox-prev').css('display', 'block');
                      prevok = true;
                    } else {
                      $('.vbox-prev').css('display', 'none');
                      prevok = false;
                    }
                    // activate swipe
                    if (prevok === true || nextok === true) {
                      content.on(TouchMouseEvent.DOWN, onDownEvent);
                      content.on(TouchMouseEvent.MOVE, onMoveEvent);
                      content.on(TouchMouseEvent.UP, onUpEvent);
                    }
                }

                /* -------- gallery navigation -------- */
                function navigateGall(destination) {

                    if (destination.length < 1) {
                      return false;
                    }
                    if (keyNavigationDisabled) {
                      return false;
                    }
                    keyNavigationDisabled = true;

                    overlayColor = destination.data('overlay') || destination.data('overlaycolor');

                    framewidth = destination.data('framewidth');
                    frameheight = destination.data('frameheight');
                    border = destination.data('border');
                    bgcolor = destination.data('bgcolor');
                    dest = destination.data('href') || destination.attr('href');

                    autoplay = destination.data('autoplay');

                    title = (destination.data('titleattr') && destination.attr(destination.data('titleattr'))) || '';

                    // swipe out item
                    if (destination === theprev) {
                      content.addClass('vbox-animated').addClass('swipe-right');
                    }
                    if (destination === thenext) {
                      content.addClass('vbox-animated').addClass('swipe-left');
                    }

                    $preloader.show();

                    content.animate({
                      opacity : 0,
                    }, 500, function(){

                        overlay.css('background',overlayColor);

                        content
                        .removeClass('vbox-animated')
                        .removeClass('swipe-left')
                        .removeClass('swipe-right')
                        .css({'margin-left': 0,'margin-right': 0});

                        if (destination.data('vbtype') == 'iframe') {
                            loadIframe();
                        } else if (destination.data('vbtype') == 'inline') {
                            loadInline();
                        } else if (destination.data('vbtype') == 'ajax') {
                            loadAjax();
                        } else if (destination.data('vbtype') == 'video') {
                            loadVid(autoplay);
                        } else {
                            content.html('<img src="'+dest+'">');
                            preloadFirst();
                        }
                        obj = destination;
                        checknav();
                        keyNavigationDisabled = false;
                        option.cb_after_nav(obj, gallIndex, thenext, theprev);
                    });
                }

                /* -------- KEYBOARD HANDLER -------- */
                function keyboardHandler(e) {
                    if (e.keyCode === 27) { // esc
                      closeVbox();
                    }

                    if (e.keyCode == 37 && prevok === true) { // left
                      navigateGall(theprev);
                    }

                    if (e.keyCode == 39 && nextok === true) { // right
                      navigateGall(thenext);
                    }
                }

                /* -------- CLOSE VBOX -------- */
                function closeVbox(){

                    var cb_pre_close = option.cb_pre_close(obj, gallIndex, thenext, theprev);

                    if (cb_pre_close === false) {
                      return false;
                    }

                    $('body').off('keydown', keyboardHandler).removeClass('vbox-open');

                    obj.focus();

                    overlay.animate({opacity:0}, 500, function(){
                      overlay.remove();
                      keyNavigationDisabled = false;
                      option.cb_post_close();
                    });
                }

                /* -------- CLOSE CLICK -------- */
                var closeclickclass = '.vbox-overlay';
                if(!option.overlayClose){
                    closeclickclass = '.vbox-close'; // close only on X
                }

                $('body').on('click touchstart', closeclickclass, function(e){
                    if ($(e.target).is('.vbox-overlay') ||
						$(e.target).is('.vbox-content') ||
						$(e.target).is('.vbox-close') ||
						$(e.target).is('.vbox-preloader') ||
						$(e.target).is('.vbox-container')
                    ) {
                        closeVbox();
                    }
                });

                startX = 0;
                endX = 0;

                diff = 0;
                threshold = 50;
                startouch = false;

                function onDownEvent(e){
                    content.addClass('vbox-animated');
                    startY = endY = e.pageY;
                    startX = endX = e.pageX;
                    startouch = true;
                }

                function onMoveEvent(e){
                    if (startouch === true) {
                        endX = e.pageX;
                        endY = e.pageY;

                        diffX = endX - startX;
                        diffY = endY - startY;

                        var absdiffX = Math.abs(diffX);
                        var absdiffY = Math.abs(diffY);

                        if ((absdiffX > absdiffY) && (absdiffX <= 100)) {
                            e.preventDefault();
                            content.css('margin-left', diffX);
                        }
                    }
                }

                function onUpEvent(e){
                    if (startouch === true) {
                        startouch = false;
                        var subject = obj;
                        var change = false;
                        diff = endX - startX;

                        if (diff < 0 && nextok === true) {
                            subject = thenext;
                            change = true;
                        }
                        if (diff > 0 && prevok === true) {
                            subject = theprev;
                            change = true;
                        }

                        if (Math.abs(diff) >= threshold && change === true) {
                            navigateGall(subject);
                        } else {
                            content.css({'margin-left': 0,'margin-right': 0});
                        }
                    }
                }

                /* == GLOBAL DECLERATIONS == */
                var TouchMouseEvent = {
                    DOWN: "touchmousedown",
                    UP: "touchmouseup",
                    MOVE: "touchmousemove"
                };

                /* == EVENT LISTENERS == */
                var onMouseEvent = function(event) {
                    var type;
                    switch (event.type) {
                        case "mousedown": type = TouchMouseEvent.DOWN; break;
                        case "mouseup":   type = TouchMouseEvent.UP;   break;
                        case "mouseout":   type = TouchMouseEvent.UP;   break;
                        case "mousemove": type = TouchMouseEvent.MOVE; break;
                        default:
                            return;
                    }
                    var touchMouseEvent = normalizeEvent(type, event, event.pageX, event.pageY);
                    $(event.target).trigger(touchMouseEvent);
                };

                var onTouchEvent = function(event) {
                    var type;
                    switch (event.type) {
                        case "touchstart": type = TouchMouseEvent.DOWN; break;
                        case "touchend":   type = TouchMouseEvent.UP;   break;
                        case "touchmove":  type = TouchMouseEvent.MOVE; break;
                        default:
                            return;
                    }

                    var touch = event.originalEvent.touches[0];
                    var touchMouseEvent;

                    if (type == TouchMouseEvent.UP) {
                         touchMouseEvent = normalizeEvent(type, event, null, null);
                    } else {
                        touchMouseEvent = normalizeEvent(type, event, touch.pageX, touch.pageY);
                    }
                    $(event.target).trigger(touchMouseEvent);
                };

                /* == NORMALIZE == */
                var normalizeEvent = function(type, original, x, y) {
                    return $.Event(type, {
                        pageX: x,
                        pageY: y,
                        originalEvent: original
                    });
                };

                /* == LISTEN TO ORIGINAL EVENT == */
                if ("ontouchstart" in window) {
                    $(document).on("touchstart", onTouchEvent);
                    $(document).on("touchmove", onTouchEvent);
                    $(document).on("touchend", onTouchEvent);
                } else {
                    $(document).on("mousedown", onMouseEvent);
                    $(document).on("mouseup", onMouseEvent);
                    $(document).on("mouseout", onMouseEvent);
                    $(document).on("mousemove", onMouseEvent);
                }

                /* -------- LOAD AJAX -------- */
                function loadAjax(){
                  $.ajax({
                  url: dest,
                  cache: false
                  }).done(function( msg ) {
                      content.html('<div class="vbox-inline">'+ msg +'</div>');
                      preloadFirst();

                  }).fail(function() {
                      content.html('<div class="vbox-inline"><p>Error retrieving contents, please retry</div>');
                      updateoverlay();
                  });
                }

                /* -------- LOAD IFRAME -------- */
                function loadIframe(){
                    content.html('<iframe class="venoframe" src="'+dest+'"></iframe>');
                  //  $('.venoframe').load(function(){ // valid only for iFrames in same domain
                    updateoverlay();
                  //  });
                }

                /* -------- LOAD VIDEOs -------- */
                function loadVid(autoplay){

                    var player;
                    var videoObj = parseVideo(dest);

                    // set rel=0 to hide related videos at the end of YT + optional autoplay
                    var stringAutoplay = autoplay ? "?rel=0&autoplay=1" : "?rel=0";
                    var queryvars = stringAutoplay + getUrlParameter(dest);

                    if (videoObj.type == 'vimeo') {
                      player = 'https://player.vimeo.com/video/';
                    } else if (videoObj.type == 'youtube') {
                      player = 'https://www.youtube.com/embed/';
                    }
                    content.html('<iframe class="venoframe vbvid" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="autoplay" frameborder="0" src="'+player+videoObj.id+queryvars+'"></iframe>');
                    updateoverlay();
                }

                /**
                * Parse Youtube or Vimeo videos and get host & ID
                */
                function parseVideo (url) {
                    url.match(/(http:|https:|)\/\/(player.|www.)?(vimeo\.com|youtu(be\.com|\.be|be\.googleapis\.com))\/(video\/|embed\/|watch\?v=|v\/)?([A-Za-z0-9._%-]*)(\&\S+)?/);
                    var type;
                    if (RegExp.$3.indexOf('youtu') > -1) {
                        type = 'youtube';
                    } else if (RegExp.$3.indexOf('vimeo') > -1) {
                        type = 'vimeo';
                    }
                    return {
                        type: type,
                        id: RegExp.$6
                    };
                }

                /**
                * get additional video url parameters
                */
                function getUrlParameter(name) {
                  var result = '';
                  var sPageURL = decodeURIComponent(name);
                  var firstsplit = sPageURL.split('?');

                  if (firstsplit[1] !== undefined) {
                      var sURLVariables = firstsplit[1].split('&');
                      var sParameterName;
                      var i;
                      for (i = 0; i < sURLVariables.length; i++) {
                          sParameterName = sURLVariables[i].split('=');
                          result = result + '&'+ sParameterName[0]+'='+ sParameterName[1];
                      }
                  }
                  return encodeURI(result);
                }

                /* -------- LOAD INLINE -------- */
                function loadInline(){
                    content.html('<div class="vbox-inline">'+$(dest).html()+'</div>');
                    updateoverlay();
                }

                /* -------- PRELOAD IMAGE -------- */
                function preloadFirst(){
                    images = content.find('img');

                    if (images.length) {
                        images.each(function(){
                            $(this).one('load', function() {
                                updateoverlay();
                            });
                        });
                    } else {
                        updateoverlay();
                    }
                }

                /* -------- FADE-IN THE NEW CONTENT -------- */
                function updateoverlay(){

                    blocktitle.html(title);
                    content.find(">:first-child").addClass('vbox-figlio').css({
                        'width': framewidth,
                        'height': frameheight,
                        'padding': border,
                        'background': bgcolor
                    });

                    $('img.vbox-figlio').on('dragstart', function(event) {
                        event.preventDefault();
                    });

                    updateOL();

                    content.animate({
                        'opacity': '1'
                    },'slow', function(){
                        $preloader.hide();
                    });

                    option.cb_content_loaded(obj, gallIndex, thenext, theprev);
                }

                /* -------- CENTER FRAME -------- */
                function updateOL(){

                    var sonH = content.outerHeight();
                    var finH = $(window).height();

                    if (sonH + 60 < finH) {
                        margine = (finH - sonH)/2;
                    } else {
                        margine = '30px';
                    }
                    content.css('margin-top', margine);
                    content.css('margin-bottom', margine);
                    option.cb_post_resize();
                }

                $(window).resize(function(){
                    if($('.vbox-content').length){
                        setTimeout(updateOL(), 800);
                    }
                });
            }); // each
        } // venobox
    }); // extend
})(jQuery);
