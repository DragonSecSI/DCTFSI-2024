/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./public/**/*.{js,css}",
    "./views/**/*.ejs",
    "./node_modules/tw-elements/js/**/*.js",
  ],
  removeDuplicates: true,
};