module.exports = {
    "parser": "babel-eslint",
    "extends": "airbnb-base",
    "rules": {
        "indent": ["error", "tab"],
        "no-tabs": 0
    },
    "env": {
        "browser": true,
        "jquery": true
    },
    "globals": {
        "flexibility": true,
        "Swiper": true,
        "tippy": true,
        "dataLayer": true,
        "Cookies": true
    }
};
