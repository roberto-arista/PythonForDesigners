
var settings = {
    styles: true,
    scripts: true,
    reload: true
};


/**
 * Paths to project folders
 */

var paths = {
    input: ['lib/', 'content/', 'templates/'],
    output: 'assets/static/',
    styles: {
        input: ['lib/sass/**/*.{scss,sass}', '!lib/sass/**/*_BAK.{scss,sass}'],
        output: 'assets/static/css/'
    },
    scripts: {
        input: 'lib/js/*.js',
        polyfills: '.polyfill.js',
        output: 'assets/static/js/'
    },
    reload: './assets/static/'
};


/**
 * Gulp Packages
 */

// General
var {gulp, src, dest, watch, series, parallel} = require('gulp');

var flatmap = require('gulp-flatmap');
var lazypipe = require('lazypipe');
var rename = require('gulp-rename');
var package = require('./package.json');

// Scripts
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
var concat = require('gulp-concat');
var uglify = require('gulp-terser');
var optimizejs = require('gulp-optimize-js');

// Styles
var sass = require('gulp-sass')(require('sass'));
var prefix = require('gulp-autoprefixer');
var minify = require('gulp-cssnano');

// BrowserSync
var browserSync = require('browser-sync');


// Repeated JavaScript tasks
var jsTasks = lazypipe()
    .pipe(optimizejs)
    .pipe(dest, paths.scripts.output)
    .pipe(rename, {suffix: '.min'})
    .pipe(uglify)
    .pipe(optimizejs)
    .pipe(dest, paths.scripts.output);

// Lint, minify, and concatenate scripts
var buildScripts = function (done) {

    // Make sure this feature is activated before running
    if (!settings.scripts) return done();

    // Run tasks on script files
    return src(paths.scripts.input)
        .pipe(flatmap(function(stream, file) {

            console.log(paths.scripts.input)
            // If the file is a directory
            if (file.isDirectory()) {

                // Setup a suffix variable
                var suffix = '';

                // If separate polyfill files enabled
                if (settings.polyfills) {

                    // Update the suffix
                    suffix = '.polyfills';

                    // Grab files that aren't polyfills, concatenate them, and process them
                    src([file.path + '/*.js', '!' + file.path + '/*' + paths.scripts.polyfills])
                        .pipe(concat(file.relative + '.js'))
                        .pipe(jsTasks());

                }

                // Grab all files and concatenate them
                // If separate polyfills enabled, this will have .polyfills in the filename
                src(file.path + '/*.js')
                    .pipe(concat(file.relative + suffix + '.js'))
                    .pipe(jsTasks());

                return stream;

            }

            // Otherwise, process the file
            return stream.pipe(jsTasks());

        }));

};

// Lint scripts
var lintScripts = function (done) {

    // Make sure this feature is activated before running
    if (!settings.scripts) return done();

    // Lint scripts
    return src(paths.scripts.input)
        .pipe(jshint())
        .pipe(jshint.reporter('jshint-stylish'));

};


// Process, lint, and minify Sass files
var buildStyles = function (done) {

    // Make sure this feature is activated before running
    if (!settings.styles) return done();

    // Run tasks on all Sass files
    return src(paths.styles.input)
        .pipe(sass({
            outputStyle: 'expanded',
            sourceComments: true
        })).on('error', sass.logError)
        .pipe(prefix({
            overrideBrowserslist: ['last 2 version', '> 0.25%'],
            cascade: true,
            remove: true
        }))
        .pipe(dest(paths.styles.output))
        // .pipe(rename({suffix: '.min'}))
        // .pipe(minify({
        //     discardComments: {
        //         removeAll: true
        //     }
        // }))
        // .pipe(dest(paths.styles.output));

};


// Watch for changes to the src directory
var startServer = function (done) {

    // Make sure this feature is activated before running
    if (!settings.reload) return done();

    // Initialize BrowserSync
    browserSync.init({
        proxy: 'localhost:5000',
        // server: {
        //     baseDir: paths.reload
        // }
    });

    // Signal completion
done();

};

// Reload the browser when files change
var reloadBrowser = function (done) {
    if (!settings.reload) return done();
    browserSync.reload({strem: true});
    done();
};

// Watch for changes
var watchSource = function (done) {
    watch(paths.input, series(exports.default, reloadBrowser));
    done();
};

/**
 * Export Tasks
 */

// Default task
// gulp
exports.default = series(
    parallel(
        buildStyles,
        buildScripts,
        lintScripts
    )
);

// Watch and reload
// gulp watch
exports.watch = series(
    exports.default,
    startServer,
    watchSource
);
