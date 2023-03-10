let sliderCount = 1;
let menuIsOpen = false;

const nextSlideBtn = document.getElementById("next");
const backSlideBtn = document.getElementById("back");
const menuBtn = document.getElementById("menuBtn");

function slideController(n) {
  const navSection = document.querySelector("section.nav-section");
  const titleSlide = document.getElementById("title-slide");
  const textSlide = document.getElementById("text-slide");
  if (sliderCount + n === 1) {
    navSection.style.backgroundImage = "url(https://ucfe6a8e87b61bf03e8384d730b1.previews.dropboxusercontent.com/p/thumb/ABYr8P6SGPc2pVogSE8H096HwVhGf5QARA9r5qcWTm-SNRlyua3n5E1AbiHQG4-rtuWYslAk_fDa1ZOEHC4-nXPRHG1MbwHCPBHxNqWbyCig87jfK_aO_GjfTKYq8zGZMy_O9ET1idl7gq9cAIHiygDqZs375L4Nco8Wexo9mStL8pf5BWBWn3x0DyqJR56eb5APXQBxmdAnXPo2B4ZgtL3C1BNqwR2pC7eoRGcz8zcke0YZZb5_3x3Z3dOBycsBpxvDzE07a5EhKUIyIX32SCmjtj6t-BjZ2zsfzqgpMESS5BzDLEQWVJh6Ef48YFncsU6u2YtJnEUyWSucTPSgYM07nzumITuhy2oUhu_MEy3GAXh61zpaHzE9ZFbZ5e_hkc0/p.jpeg)";
    titleSlide.innerHTML = "Discover innovative ways to decorate";
    textSlide.innerHTML = `We provide unmatched quality, comfort, and style for property owners across the country.
      Our experts combine form and function in bringing your vision to life. Create a room in your
      own style with our collection and make your property a reflection of you and what you love.`;
  } else if (sliderCount + n === 2) {
    navSection.style.backgroundImage = "url(https://uca434644deac523cd145ce666e2.previews.dropboxusercontent.com/p/thumb/ABZIpvwxwhNNtYv3LOY3u6DySwsGL8hOYC6RxQYG_LyOVdp6yNOAf1ESm-DWKR2mDl81vs9ihHtdGezNd9jeyMf14PFIlym3eAmmafZARJ6ApowSyJt_G8VsDTEx8JFHhxkdOfamx0B1_z5-c_KKXwSLHpYDgachna2q6x9Si1XSm1htthh6GhPWI9jrVHeN5HohSl3t3V6g9FkkCDmqY711VScl1Qr4ZQggwQtFie2e08s6JIFKvxTqiaHzaQTEswMoXKboCCEU6hLBkC87bGgb3ZWraF2NqpCsqSgG52vXbTLKAc-eukXn5G9ZM_Lquxx-eJqKRzwUPGeYEL1dUP9a_P5cPG7D2rnKb-aRQaTtwNAMcsBW3lZERBSnR7x1EN1y-8-_nW2uTR_RwSSXa5ho/p.jpeg)";
    titleSlide.innerHTML = "We are available all across the globe";
    textSlide.innerHTML = `With stores all over the world, it's easy for you to find furniture for your home or place of business.
    Locally, we’re in most major cities throughout the country. Find the branch nearest you using our
    store locator..`;
  } else if (sliderCount + n === 3) {
    navSection.style.backgroundImage = "url(https://uc3b0b6fa501ff08fa426bcc7924.previews.dropboxusercontent.com/p/thumb/ABa6GKwoUn59ATi-E2apZ5mxYLwm-bVstpANaGZT6r40E0TmRlsC79J2YonQI7fKoOtp7R_oNpsiGr6vmAGQsKteefZ7q8vharDhG-8iQkTV6aRtp-RjODtDsGzwZW8cKUsF0IqkltBazbnWpGqkjF-C01NEn6F4Mh5-FVkYnaiUPvrihg6XHc6ayYEx_Fw-drF8SM7HBSK8An2wj0l7uPiEZrElgXk_LWpim4_ZOAc-uoX19Pv4dDg1Fdj450EHGubmAG6ueKoWJ3GgJN8f2RihQbGmrS9BxzUlHch6dO1hC_MLNcifKA6eFJ_oOSrhdtgAwfIHQe5wsU7umHcyntuUT9JWo9Cby-G1o7m3EcuvJIM539B5ZHHOU_MeiEWBrsY/p.jpeg)";
    titleSlide.innerHTML = "Manufactured with the best materials";
    textSlide.innerHTML = `Our modern furniture store provide a high level of quality. Our company has invested in advanced technology
    to ensure that every product is made as perfect and as consistent as possible.`;
  }
  sliderCount = sliderCount + n;
}

function menuController() {
  const menuImg = document.getElementById("menuImg");
  const menuItems = document.getElementsByClassName("menu-item");
  const logo = document.getElementById("logo");
  const nav = document.getElementById("nav");
  menuIsOpen = !menuIsOpen;
  if (menuIsOpen) {
    menuBtn.innerHTML = '<svg width="16" height="16" xmlns="http://www.w3.org/2000/svg"><path d="M14.364.222l1.414 1.414L9.414 8l6.364 6.364-1.414 1.414L8 9.414l-6.364 6.364-1.414-1.414L6.586 8 .222 1.636 1.636.222 8 6.586 14.364.222z" fill="#000" fill-rule="evenodd" opacity=".201"/></svg>';
    logo.style.display = "none";
    Array.prototype.forEach.call(menuItems, (item) => {
      item.style.display = "block";
    });
    nav.style.background = "white";
  } else {
    menuBtn.innerHTML = '<svg width="20" height="14" xmlns="http://www.w3.org/2000/svg"><path d="M20 12v2H0v-2h20zm0-6v2H0V6h20zm0-6v2H0V0h20z" fill="#FFF" fill-rule="evenodd"/></svg>';
    logo.style.display = "block";
    Array.prototype.forEach.call(menuItems, (item) => {
      item.style.display = "none";
    });
    nav.style.background = "transparent";
  }
}

nextSlideBtn.addEventListener("click", () => {
  if (sliderCount + 1 > 3) {
    sliderCount = 1;
    slideController(0);
  } else {
    slideController(1);
  }
});

backSlideBtn.addEventListener("click", () => {
  if (sliderCount - 1 < 1) {
    sliderCount = 3;
    slideController(0);
  } else {
    slideController(-1);
  }
});

menuBtn.addEventListener("click", () => menuController());
