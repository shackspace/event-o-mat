var path = require('path')
var webpack = require('webpack')
var merge = require('webpack-merge')
var utils = require('./utils')
var path = require('path')
var projectRoot = path.resolve(__dirname, '../')
var baseWebpackConfig = require('./webpack.base.conf')
const MiniCssExtractPlugin = require("mini-css-extract-plugin")
var HtmlWebpackPlugin = require('html-webpack-plugin')
var CompressionPlugin = require('compression-webpack-plugin')
var CleanWebpackPlugin = require('clean-webpack-plugin')
var webpackConfig = merge(baseWebpackConfig, {
	mode: 'production',
	resolve: {
		alias: {
			'config': path.resolve(projectRoot, 'config.prod.js'),
		}
	},
	devtool: '#source-map',
	module: {
		rules: [
			{ test: /\.vue$/, use: [{
				loader:'vue-loader',
				options: {
					loaders: {
						stylus: [
							MiniCssExtractPlugin.loader,
							'css-loader',
							'stylus-loader'
						]
					}
				}
			}]},
			{ test: /\.css$/, use: [
				MiniCssExtractPlugin.loader,
				"css-loader"
			]},
			{ test: /\.styl$/, use: [
				MiniCssExtractPlugin.loader,
				'css-loader',
				'stylus-loader'
			]},
		]
	},
	output: {
		filename: utils.assetsPath('js/[name].[chunkhash].js'),
		chunkFilename: utils.assetsPath('js/[name].[chunkhash].js'),
		sourceMapFilename: '[file].map.js',
	},
	optimization: {
		runtimeChunk: true,
		splitChunks: {
			cacheGroups: {
				commons: {
					test: /[\\/]node_modules[\\/]/,
					name: "vendors",
					chunks: "all"
				}
			}
		}
	},
	plugins: [
		new webpack.LoaderOptionsPlugin({
			minimize: true,
			debug: false
		}),
		// new CleanWebpackPlugin(['dist'], {root: path.resolve(__dirname, '../')}),
		new webpack.DefinePlugin({
			'ENV_DEVELOPMENT': false,
			'process.env': {
				NODE_ENV: '"production"'
			},
			TARGET: process.env.TARGET == 'production' ? '"production"' : '"stage"'
		}),
		// extract css into its own file
		new MiniCssExtractPlugin({
			// Options similar to the same options in webpackOptions.output
			// both options are optional
			filename: "[name].[chunkhash].css",
			chunkFilename: "[id].[chunkhash].css"
		}),
		// generate dist index.html with correct asset hash for caching.
		// you can customize output by editing /index.html
		// see https://github.com/ampedandwired/html-webpack-plugin
		new HtmlWebpackPlugin({
			template: 'index.html',
			inject: true,
			minify: {
				removeComments: true,
				collapseWhitespace: true,
				removeAttributeQuotes: true
				// more options:
				// https://github.com/kangax/html-minifier#options-quick-reference
			},
			// necessary to consistently work with multiple chunks via CommonsChunkPlugin
			chunksSortMode: 'dependency'
		}),
		new CompressionPlugin({
			asset: '[path].gz[query]',
			algorithm: 'gzip',
			test: new RegExp(
				'\\.(js|css)$'
			),
			threshold: 10240,
			minRatio: 0.8
		})
	]
})

module.exports = webpackConfig
