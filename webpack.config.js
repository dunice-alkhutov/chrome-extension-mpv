const path = require('path');

module.exports = {
  entry: [
    // Set up an ES6-ish environment
    'babel-polyfill',

    // Add your application's scripts below
    __dirname + '/js/main.js',
  ],
  output: {
    path: __dirname + '/build/js',
    filename: "bundle.js"
  },
  module: {
    loaders: [{
      // Only run `.js` and `.jsx` files through Babel
      test: /\.js?$/,

      loader: "babel-loader",

      // Skip any files outside of your project's `src` directory
      include: [
        path.resolve(__dirname, "js"),
      ]
    }]
  }
}