'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
sass.compiler = require('node-sass');
var browserSync = require('browser-sync').create();

gulp.task('styles', function () {
  return gulp.src('lib/sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('assets/static/css'))
    .pipe(browserSync.reload({
      stream: true
      }))
});

gulp.task('browserSync', function() {
  browserSync.init({
    proxy: 'localhost:5000',
  })
})

gulp.task('watch', ['browserSync', 'styles'], function () {
  gulp.watch('lib/sass/**/*.scss', ['styles']);
});