let searchIcon = document.querySelector('.search-icon');
let searchArea = document.querySelector('.search-area');
let cancelsearch = document.querySelector('.cancel-search-area');
let more = document.querySelector('.more');
let ellipsisEx = document.querySelector('.ellipsis-ex');
let headerNav = document.querySelector('.header-nav');
window.onscroll = function() {fixHeader()};

function fixHeader() {
  headerTopLength = headerNav.getBoundingClientRect().top;
  if (headerTopLength <=0) {
    headerNav.classList.add('header-fix-top');
  }if(window.scrollY < 30) {
    headerNav.classList.remove('header-fix-top');
  }
};
searchIcon.addEventListener('click', () => {
    searchArea.classList.remove('hide');
});
cancelsearch.addEventListener('click', () => {
    searchArea.classList.add('hide');
});

let howContentText = document.querySelector('.how-content p');
window.onload = ()=>{
  howContentText.classList.add('text-truncate');
};
  
function toggleEllipsis() {
  howContentText.classList.toggle('text-truncate');
  howContentText.nextElementSibling.classList.toggle('hide');

};
howContentText.addEventListener('click', toggleEllipsis);
function toggleEllipsisMore(el) {
    el.previousElementSibling.classList.toggle('text-truncate');
    el.classList.toggle('hide');

};

function displaySideMenu() {
  document.querySelector('.ham-side-nav-bar').classList.toggle('translate-left-right');
};