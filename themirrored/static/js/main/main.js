let searchIcon = document.querySelector('.search-icon');
let searchArea = document.querySelector('.search-area');
let cancelsearch = document.querySelector('.cancel-search-area');
let shareArea = document.querySelector('.social-share');
let more = document.querySelector('.more');
let ellipsisEx = document.querySelector('.ellipsis-ex');
let headerNav = document.querySelector('.header-nav');
const menuBar1 = document.querySelector('.ham-1');
const menuBar2 = document.querySelector('.ham-2');
const menuBar3 = document.querySelector('.ham-3');
window.onscroll = function() {fixHeader()};


function fixHeader() {
  headerTopLength = headerNav.getBoundingClientRect().top;
  if (headerTopLength <=0) {
    headerNav.classList.add('header-fix-top');
  }if(window.scrollY < 30) {
    headerNav.classList.remove('header-fix-top');
  }
}
searchIcon.addEventListener('click', () => {
    searchArea.classList.remove('hide');
});
cancelsearch.addEventListener('click', () => {
    searchArea.classList.add('hide');
})

function displayShare() {
  shareArea.classList.remove('hide');
}
function cancelShare() {
  shareArea.classList.add('hide');
}

let howContentText = document.querySelector('.how-content .post-full-text');
let moreContentText = document.querySelector('.how-content .more');
window.onload = ()=>{
  howContentText.classList.add('text-truncate');
}
  
function toggleEllipsis(el) {
  el.classList.toggle('text-truncate');
  moreContentText.classList.toggle('hide');

}
howContentText.addEventListener('click', toggleEllipsis)


function toggleEllipsisMore(el) {
  howContentText.classList.toggle('text-truncate');
  el.classList.toggle('hide');
}
// moreContentText.addEventListener('click', toggleEllipsis)

function displaySideMenu() {
  document.querySelector('.ham-side-nav-bar').classList.toggle('translate-left-right');
  menuBar2.classList.toggle('disappear');
  menuBar1.classList.toggle('rotate45');
  menuBar3.classList.toggle('rotateneg45');
}