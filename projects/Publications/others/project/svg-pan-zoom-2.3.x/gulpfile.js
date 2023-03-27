/**
 *  Modules
 */
var gulp   = require('gulp')
  , watch      = require('gulp-watch')
  , uglify     = require('gulp-uglify')
  , browserify = require('browserify')
  , source     = require('vinyl-source-stream')
  , streamify  = require('gulp-streamify')
  , rename     = require('gulp-rename')
  ;

/**
 *  Build script
 */
gulp.task('build', function() {
  return browserify({entries:'./src/stand-alone.js'})
    .bundle()
    .on('error', function (err) {
      console.log(err.toString())
      this.emit("end")
    })
    .pipe(source('svg-pan-zoom.js'))
    .pipe(gulp.dest('./dist/'))
    .pipe(streamify(rename('svg-pan-zoom.min.js')))
    .pipe(streamify(uglify()))
    .pipe(gulp.dest('./dist/'))
});

/**
 * Watch script
 */
gulp.task('watch', function () {
  gulp.watch('./src/**/*.js', ['build']);
});

/**
 * Default task
 */
gulp.task('default', [
  'build',
  'watch'
]);

