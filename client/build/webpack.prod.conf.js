var path = require('path')
var webpack = require('webpack')
var merge = require('webpack-merge')
var utils = require('./utils')
var path = require('path')
var projectRoot = path.resolve(__dirname, '../')
var baseWebpackConfig = require('./webpack.base.conf')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var HtmlWebpackPlugin = require('html-webpack-plugin')
var CompressionPlugin = require('compression-webpack-plugin')
var CleanWebpackPlugin = require('clean-webpack-plugin')
var webpackConfig = merge(baseWebpackConfig, {
	mode: 'production',
	resolve: {
		alias: {
			'config': path.resolve(projectRoot, process.env.TARGET == 'production' ? 'config.prod.js' : process.env.TARGET == 'testing' ? 'config.test.js' : 'config.stage.js'),
		}
	},
	devtool: '#source-map',
	module: {
		rules: [
			{ test: /\.vue$/, use: [{
				loader:'vue-loader',
				options: {
					loaders: {
						stylus: ExtractTextPlugin.extract({
							use: ['css-loader', 'stylus-loader'],
							fallback: 'vue-style-loader'
						})
					}
				}
			}]},
			{ test: /\.css$/, use: ExtractTextPlugin.extract({
				fallback: 'style-loader',
				use: 'css-loader'
			})},
			{ test: /\.styl$/, use: ExtractTextPlugin.extract({
				fallback: 'style-loader',
				use: ['css-loader', 'stylus-loader']
			})}
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
		new ExtractTextPlugin({
			filename: utils.assetsPath('css/[name].[contenthash].css'),
			allChunks: true
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
