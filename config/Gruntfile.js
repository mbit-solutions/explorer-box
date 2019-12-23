module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        concat: {
            "options": { "separator": ";" },
            "build": {
                "src": ["node_modules/jquery/dist/jquery.js", "assets/js/index.js"],
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

        watch: {
            scripts: {
                files: ['**/*.js'],
                tasks: ['concat', 'uglify'],
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

    // Task definitions
    grunt.registerTask('default', ['concat', 'uglify', 'watch']);
};