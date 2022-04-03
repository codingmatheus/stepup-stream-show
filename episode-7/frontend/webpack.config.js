// Import path for resolving file paths
var path = require("path");
module.exports = {
  mode: "development",
  // Specify the entry point for our app.
  entry: [path.join(__dirname, "game.js")],
  // Specify the output file containing our bundled code.
  output: {
    path: __dirname,
    filename: 'bundle.js'
  },
   // Enable WebPack to use the 'path' package.
   resolve:{
  fallback: { path: require.resolve("path-browserify")}
  }
};