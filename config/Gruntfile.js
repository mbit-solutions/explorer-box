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
                "dest": "public/dist/js/app.js"
            }
        },
        uglify: {
            my_target: {
                files: {
                    'public/dist/js/app.min.js': ['public/dist/js/app.js']
                }
            }
        },

        sass: {
            dist: {
                options: {
                    style: 'expanded'
                },
                files: {
                    'public/dist/css/index.css': 'assets/scss/index.scss',
                }
            }
        },

        cssmin: {
            target: {
                files: [{
                    expand: true,
                    cwd: 'public/dist/css',
                    src: ['*.css', '!*.min.css'],
                    dest: 'public/dist/css',
                    ext: '.min.css'
                }]
            }
        },


        watch: {
            scripts: {
                files: ['assets/js/**/*.js'],
                tasks: ['concat', 'uglify'],
                options: {
                    spawn: false,
                },
            },
            css: {
                files: ['assets/scss/**/*.scss'],
                tasks: ['sass', 'cssmin'],
                options: {
                    spawn: false,
                },
            }
        }

    });

    // Load required modules
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // Task definitions
    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'cssmin']);
};