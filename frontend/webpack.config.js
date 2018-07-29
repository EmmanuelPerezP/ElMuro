const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, '../principal/static')
  },
  devServer: {
    filename: 'main.js',
    contentBase: path.resolve(__dirname, '../principal/static'),
    watchContentBase: true,
  },
};