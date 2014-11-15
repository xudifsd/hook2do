gulp = require 'gulp'

stylus = require 'gulp-stylus'
coffee = require 'gulp-coffee'
concat = require 'gulp-concat'

path = require 'path'
source = require 'vinyl-source-stream'
browserify = require 'browserify'

BUILD = path.join(__dirname, '../static/')

gulp.task 'coffee', ->
  browserify extensions: ['.coffee'], basedir: path.join(__dirname, 'coffee/')
    .add './main.coffee'
    .transform 'coffeeify'
    .bundle()
    .pipe source('app.js')
    .pipe gulp.dest("#{BUILD}/js")


gulp.task 'stylus', ->
  gulp.src('./stylus/main.styl')
    .pipe stylus()
    .pipe concat('styles.css')
    .pipe gulp.dest("#{BUILD}/css")

gulp.task 'jsdeps', ->
  gulp.src([
    './bower_components/underscore/underscore-min.js'
    './bower_components/hammerjs/hammer.min.js'
    './bower_components/angular/angular.min.js'
    './bower_components/angular-aria/angular-aria.min.js'
    './bower_components/angular-animate/angular-animate.min.js'
    './bower_components/angular-material/angular-material.min.js'
    './bower_components/angular-resource/angular-resource.min.js'
    './bower_components/angular-loading-bar/build/loading-bar.min.js'
    ])
    .pipe concat('deps.js')
    .pipe gulp.dest("#{BUILD}/js")

gulp.task 'cssdeps', ->
  gulp.src([
    './bower_components/angular-material/angular-material.min.css'
    './bower_components/angular-loading-bar/build/loading-bar.min.css'
    './bower_components/fontawesome/css/font-awesome.min.css'
    ])
    .pipe concat('deps.css')
    .pipe gulp.dest("#{BUILD}/css")


gulp.task 'fonts', ->
  gulp.src('./bower_components/fontawesome/fonts/*')
    .pipe gulp.dest("#{BUILD}/fonts")


gulp.task 'deps', ['jsdeps', 'cssdeps', 'fonts']

gulp.task 'watch', ->
  gulp.watch ['./stylus/**/*.styl'], ['stylus']
  gulp.watch ['./coffee/**/*.coffee'], ['coffee']

gulp.task 'build', ['coffee', 'stylus', 'deps']
gulp.task 'default', ['build', 'watch']
