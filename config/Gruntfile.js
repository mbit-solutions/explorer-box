module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        concat: {
            "options": { "separator": ";" },
            "build": {
                "src": [
                    "node_modules/jquery/dist/jquery.js",
                    "assets/js/popper/popper.min.js",
                    "assets/js/bootstrap/bootstrap.js",
                    "assets/js/toastr/toastr.min.js",
                    "assets/js/index.js"
                ],
                "dest": "dist/js/app.js"
            }
        },
        uglify: {
            my_target: {
                files: {
                    'dist/js/app.min.js': ['dist/js/app.js']
                }
            }
        },

        sass: {
            dist: {
                options: {
                    style: 'expanded'
                },
                files: {
                    'dist/css/index.css': 'assets/scss/index.scss',
                }
            }
        },

        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'dist/css',
                    src: ['*.css', '!*.min.css'],
                    dest: 'dist/css',
                    ext: '.min.css'
                }]
            }
        },


        watch: {
            scripts: {
                files: ['**/*.js', '**/*.scss'],
                tasks: ['concat', 'uglify', 'sass', 'cssmin'],
                options: {
                    spawn: false,
                },
            },
        }

    });

    // Load required modules
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // Task definitions
    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'cssmin', 'watch']);
};