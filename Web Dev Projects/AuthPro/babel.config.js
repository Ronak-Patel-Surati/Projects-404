module.exports = function (api) {
  api.cache(true);
  return {
    presets: ['babel-preset-expo'], // or 'module:metro-react-native-babel-preset'
    plugins: [
      [
        'module:react-native-dotenv',
        {
          moduleName: '@env',  // This tells Babel to look for the '@env' imports
          path: '.env',        // Path to your .env file
          allowUndefined: true, // Optional: allows undefined variables
        },
      ],
    ],
  };
};
