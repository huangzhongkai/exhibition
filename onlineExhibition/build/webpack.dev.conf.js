var utils = require('./utils')
var webpack = require('webpack')
var config = require('../config')
var merge = require('webpack-merge')
var baseWebpackConfig = require('./webpack.base.conf')
var HtmlWebpackPlugin = require('html-webpack-plugin')
var FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')

// add hot-reload related code to entry chunks
Object.keys(baseWebpackConfig.entry).forEach(function (name) {
  baseWebpackConfig.entry[name] = ['./build/dev-client'].concat(baseWebpackConfig.entry[name])
})

module.exports = merge(baseWebpackConfig, {
  module: {
    rules: utils.styleLoaders({ sourceMap: config.dev.cssSourceMap })
  },
  // cheap-module-eval-source-map is faster for development
  devtool: '#cheap-module-eval-source-map',
  plugins: [
    new webpack.DefinePlugin({
      'process.env': config.dev.env
    }),
    // https://github.com/glenjamin/webpack-hot-middleware#installation--usage
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    // https://github.com/ampedandwired/html-webpack-plugin
    new HtmlWebpackPlugin({
      // filename: 'index.html',
      // template: 'index.html',
      // inject: true
      filename: 'artist.html',
      template: './src/view/artist/artist.html',
      inject: true,
      chunks: ['artist']
    }),
    new HtmlWebpackPlugin({
      filename: 'exhibition/exhibition.html',
      template: './src/view/exhibition/exhibition.html',
      inject: true,
      chunks: ['exhibition']
    }),
    new HtmlWebpackPlugin({
      filename: 'home/home.html',
      template: './src/view/home/home.html',
      inject: true,
      chunks: ['home']
    }),
    new HtmlWebpackPlugin({
      filename: 'exhibit/exhibit.html',
      template: './src/view/exhibit/exhibit.html',
      inject: true,
      chunks: ['exhibit']
    }),
    new HtmlWebpackPlugin({
      filename: 'readings/image_text_readings.html',
      template: './src/view/readings/image_text_readings/image_text_readings.html',
      inject: true,
      chunks: ['image_text_readings']
    }),
    new HtmlWebpackPlugin({
      filename: 'readings/video_readings.html',
      template: './src/view/readings/video_readings/video_readings.html',
      inject: true,
      chunks: ['video_readings']
    }),
    new HtmlWebpackPlugin({
      filename: 'ratings/ratings.html',
      template: './src/view/ratings/ratings.html',
      inject: true,
      chunks: ['ratings']
    }),
    new FriendlyErrorsPlugin()
  ]
})
