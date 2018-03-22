var webpack = require('webpack')
var merge = require('webpack-merge')
var path = require('path')
var projectRoot = path.resolve(__dirname, '../')
var baseWebpackConfig = require('./webpack.base.conf')
var HtmlWebpackPlugin = require('html-webpack-plugin')

// add hot-reload related code to entry chunks
Object.keys(baseWebpackConfig.entry).forEach(function (name) {
	baseWebpackConfig.entry[name] = ['webpack-hot-middleware/client'].concat(baseWebpackConfig.entry[name])
})

module.exports = merge(baseWebpackConfig, {
	mode: 'development',
	module: {
		rules: [
			{ test: /\.vue$/, use: ['vue-loader']},
			{ test: /\.css$/, use: ['style-loader','css-loader'] },
			{ test: /\.styl$/, use: ['style-loader','css-loader', 'stylus-loader'] }
		]
	},
	resolve: {
		alias: {
			'config': path.resolve(projectRoot, 'config.dev.js'),
		}
	},
	plugins: [
		new webpack.DefinePlugin({
			'ENV_DEVELOPMENT': true,
			'process.env': {
				NODE_ENV: '"development"'
			},
			TARGET: '"development"'
		}),
		new webpack.HotModuleReplacementPlugin(),
		new HtmlWebpackPlugin({
			filename: 'index.html',
			template: 'index.html',
			inject: true
		})
	]
})
