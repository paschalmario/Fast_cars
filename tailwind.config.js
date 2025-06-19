module.exports = {
  content: [
    "./website/templates/**/*.html",
    "./website/static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        main: "#fd4646",
        accent: "#02ac70",
        "primary-bg": "#eaeaea",
        "primary": "#211C84",
        "secondary": "#7A73D1",
        "footer-bg": "#211C84",
        "footer-text": "#bbb",
        "footer-link-hover": "#fff",
        "gradient-purple": "#7A73D1",
        "gradient-blue": "#211C84",
      },
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
        lato: ["Lato", "sans-serif"],
        oswald: ["Oswald", "sans-serif"],
      },
      spacing: {
        'header-x': '8%',
        'header-x-md': '5%',
        'header-x-sm': '2%',
        'footer-py': '20px',
        'footer-section-p': '20px',
        'footer-bottom-py': '10px',
      },
      borderRadius: {
        'btn': '6px',
        'product': '5px',
        'profile': '10px',
      },
      boxShadow: {
        'footer': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',
      }
    },
  },
  plugins: [],
}
