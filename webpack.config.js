const webpack = require('webpack');


module.exports = {
  mode: 'development',  
  entry: './src/index.js',
  output: {
    filename: 'index.js',
    publicPath: "./dist/"
  },
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              modules: true,
              localsConvention: 'camelCase',
              sourceMap: true
            }
          }
        ]
      }
    ]
  },
  plugins: [
   
  ],
  devServer: {
    host: 'localhost',
    historyApiFallback: true,
    open: true
  }
};