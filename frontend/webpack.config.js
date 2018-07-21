const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, '../principal/static/js/')
  },
  devServer: {
    contentBase: path.resolve(__dirname, '../principal/static/')
  },
};