/* Adapted from RegExper (http://regexper.com) gulpfile.js */

var gulp = require('gulp');
var COPY_GLOB = './src/**/*.@(html|css|png)';

gulp.task('default', ['server'], function() {
    gulp.watch(COPY_GLOB, ['copy']);
    gulp.watch('./index.js', ['browserify']);
});

gulp.task('server', ['copy', 'browserify'], function() {
  var connect = require('gulp-connect'),
      watch = require('gulp-watch');

  watch('./build/**/*')
    .pipe(connect.reload());

  return connect.server({ 
    root: './build',
    liveReload: true
  });
});

gulp.task('copy', [], function() {
  return gulp.src(COPY_GLOB , { base: './src' })
    .pipe(gulp.dest('./build'));
});

gulp.task('browserify', [], function() {
  var browserify = require('browserify'),
      source = require('vinyl-source-stream');
  return browserify('./index.js')
    .bundle()
    .pipe(source('table-viewer.js'))
    .pipe(gulp.dest('./build/'));
});
