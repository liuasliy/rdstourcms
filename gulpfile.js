var gulp = require('gulp'),
    runSequence = require('run-sequence'), //顺序执行
    minifyCss = require('gulp-minify-css'),  //- 压缩CSS为一行；
    uglify = require('gulp-uglify'),  //压缩文件
    rev = require('gulp-rev'),
    concat = require('gulp-concat'),
    revCollector = require('gulp-rev-collector');
    //sass = require('gulp-sass');        //编译less文件



//CSS里更新引入文件版本号
gulp.task('revCollectorCss', function () {
    return gulp.src(['static/css/rev/*.json', 'static/css/cssRev/*.css'])
        .pipe(revCollector())
        .pipe(gulp.dest('static/css'));
});

//压缩/合并CSS/生成版本号
gulp.task('miniCss', function(){
    return gulp.src(['static/css/rs-account.css','static/css/rs-index.css'])
        .pipe(rev())
        .pipe(rev.manifest())
        .pipe(gulp.dest('static/css/rev'));
});
//压缩Html/更新引入文件版本
gulp.task('miniHtml', function () {
    return gulp.src(['static/css/rev/*.json', 'templates/rev/*.*'])
        .pipe(revCollector())
        .pipe(gulp.dest('templates'));
});




gulp.task('cssminify', function () {
    //please code for your default task here
    return gulp.src(['static/scss/rs-account.css','static/scss/rs-index.css'])
        .pipe(minifyCss())
        .pipe(gulp.dest('static/css/cssRev'))
});
gulp.task('cssconcat', function () {
    //please code for your default task here
    return gulp.src(['static/css/bootstrap.min.css',,'static/css/photo.css','static/css/default-skin/default-skin.css','static/css/photoswipe.css','static/css/font-awesome.min.css','static/scss/rs-account.css','static/scss/rs-index.css'])
        .pipe(concat('rs-index.css'))
        .pipe(minifyCss())
        .pipe(gulp.dest('static/css/cssRev'))
});

//编译sass文件
gulp.task('sass', function () {
    gulp.src(['static/scss/rs-account.scss','static/scss/rs-index.scss'])
        .pipe(sass())
        .pipe(gulp.dest('static/css'))
});

gulp.task('build', function (done) {
    runSequence(
        ['cssconcat'],
        ['revCollectorCss'],
        ['miniCss'],
        ['miniHtml'],
        done);
});


//压缩js
gulp.task('jsminify', function () {
    return gulp.src('static/js/bootstrap-datepicker.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'))
        .pipe(rename({suffix: '.min'}))  //重命名压缩后的文件
        .pipe(uglify())   //执行压缩任务
        //.pipe(concat('until.js'))
        .pipe(gulp.dest('static/js'))
});


