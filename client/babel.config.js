module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        corejs: '3',
        modules: 'commonjs',
        useBuiltIns: true,
      },
    ],
    [
      '@babel/preset-react',
      {
        development: true,
      },
    ],
  ],
};
