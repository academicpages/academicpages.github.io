// --------------------------------------------------
// [Gulpfile]
// --------------------------------------------------

'use strict';
 
var gulp 		= require('gulp'),
	sass 		= require('gulp-sass'),
	changed 	= require('gulp-changed'),
	cleanCSS 	= require('gulp-clean-css'),
	rtlcss 		= require('gulp-rtlcss'),
	rename 		= require('gulp-rename'),
	uglify 		= require('gulp-uglify'),
	pump 		= require('pump'),
	htmlhint  	= require('gulp-htmlhint');


// Gulp plumber error handler
function errorLog(error) {
	console.error.bind(error);
	this.emit('end');
}


// --------------------------------------------------
// [Libraries]
// --------------------------------------------------

// Sass - Compile Sass files into CSS
gulp.task('sass', function () {
	gulp.src('../HTML/sass/**/*.scss')
		.pipe(changed('../HTML/css/'))
		.pipe(sass({ outputStyle: 'expanded' }))
		.on('error', sass.logError)
		.pipe(gulp.dest('../HTML/css/'));
});


// Minify CSS
gulp.task('minify-css', function() {
	// Theme
    gulp.src(['../HTML/css/layout.css', '!../HTML/css/layout.min.css'])
        .pipe(cleanCSS({debug: true}, function(details) {
            console.log(details.name + ': ' + details.stats.originalSize);
            console.log(details.name + ': ' + details.stats.minifiedSize);
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('../HTML/css/'));

    // RTL
    gulp.src(['../HTML/css/layout-rtl.css', '!../HTML/css/layout-rtl.min.css'])
        .pipe(cleanCSS({debug: true}, function(details) {
            console.log(details.name + ': ' + details.stats.originalSize);
            console.log(details.name + ': ' + details.stats.minifiedSize);
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('../HTML/css/'));
});


// RTL CSS - Convert LTR CSS to RTL.
gulp.task('rtlcss', function () {
	gulp.src(['../HTML/css/layout.css', '!../HTML/css/layout.min.css', '!../HTML/css/layout-rtl.css', '!../HTML/css/layout-rtl.min.css'])
	.pipe(changed('../HTML/css/'))
		.pipe(rtlcss())
		.pipe(rename({ suffix: '-rtl' }))
		.pipe(gulp.dest('../HTML/css/'));
});


// Minify JS - Minifies JS
gulp.task('uglify', function (cb) {
  	pump([
	        gulp.src(['../HTML/js/**/*.js', '!../HTML/js/**/*.min.js']),
	        uglify(),
			rename({ suffix: '.min' }),
	        gulp.dest('../HTML/js/')
		],
		cb
	);
});


// Htmlhint - Validate HTML
gulp.task('htmlhint', function() {
	gulp.src('../HTML/*.html')
		.pipe(htmlhint())
		.pipe(htmlhint.reporter())
	  	.pipe(htmlhint.failReporter({ suppress: true }))
});


// --------------------------------------------------
// [Gulp Task - Watch]
// --------------------------------------------------

// Lets us type "gulp" on the command line and run all of our tasks
gulp.task('default', ['sass', 'minify-css', 'rtlcss', 'uglify', 'htmlhint', 'watch']);

// This handles watching and running tasks
gulp.task('watch', function () {
    gulp.watch('../HTML/sass/**/*.scss', ['sass']);
    gulp.watch('../HTML/css/layout.css', ['minify-css']);
    gulp.watch('../HTML/css/layout.css', ['rtlcss']);
    gulp.watch('../HTML/js/**/*.js', ['uglify']);
    gulp.watch('../HTML/*.html', ['htmlhint']);
});