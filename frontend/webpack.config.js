var path = require("path")
var webpack = require("webpack")


module.exports = {
    entry: "./src/index.js",
    output: { path: __dirname, filename: "./dist/main.js" },
    mode: 'development',
    module: {
	rules: [
	    {
		test: /.jsx?$/,
		loader: 'babel-loader',
		exclude: /node_modules/,
		query: {
		    presets: ['es2015', 'react']
		}
	    },
	    {
		test: /\.css$/,
		use: [ 'style-loader', 'css-loader' ]
	    }
	]
    }
}
