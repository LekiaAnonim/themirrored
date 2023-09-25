let searchIcon = document.querySelector('.search-icon');
let searchArea = document.querySelector('.search-area');
let cancelsearch = document.querySelector('.cancel-search-area');
let more = document.querySelector('.more');
let ellipsisEx = document.querySelector('.ellipsis-ex');
searchIcon.addEventListener('click', () => {
    searchArea.classList.remove('hide');
});
cancelsearch.addEventListener('click', () => {
    searchArea.classList.add('hide');
})

// ellipsisEx.addEventListener('click', () => {
//     ellipsisEx.classList.toggle('text-truncate');
//     more.classList.toggle('hide')
// })

// more.addEventListener('click', () => {
//     ellipsisEx.classList.toggle('text-truncate');
//     more.classList.toggle('hide')
// })

function toggleEllipsis(el) {
    el.classList.toggle('text-truncate');
    el.nextElementSibling.classList.toggle('hide');

}

function toggleEllipsisMore(el) {
    el.previousElementSibling.classList.toggle('text-truncate');
    el.classList.toggle('hide');

}