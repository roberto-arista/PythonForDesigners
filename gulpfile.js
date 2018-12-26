'use strict';

var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var sass = require('gulp-sass');
sass.compiler = require('node-sass');
var browserSync = require('browser-sync').create();

var sassOptions = {
  errLogToConsole: true,
  outputStyle: 'expanded'
};

gulp.task('styles', function () {

  return gulp
      .src('lib/sass/**/*.scss')
      .pipe(sass(sassOptions).on('error', sass.logError))
      .pipe(autoprefixer())
      .pipe(gulp.dest('assets/static/css'))
      .pipe(browserSync.reload({
        stream: true
        }));
  });

gulp.task('browserSync', function() {
  browserSync.init({
    proxy: 'localhost:5000',
  })
})

gulp.task('watch', ['browserSync', 'styles'], function () {
  gulp.watch('lib/sass/**/*.scss', ['styles']);
});