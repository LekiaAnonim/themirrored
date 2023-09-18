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
}
searchIcon.addEventListener('click', () => {
    searchArea.classList.remove('hide');
});
cancelsearch.addEventListener('click', () => {
    searchArea.classList.add('hide');
})

function toggleEllipsis(el) {
    el.classList.toggle('text-truncate');
    el.nextElementSibling.classList.toggle('hide');

}

function toggleEllipsisMore(el) {
    el.previousElementSibling.classList.toggle('text-truncate');
    el.classList.toggle('hide');

}