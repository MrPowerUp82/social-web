let aside = document.querySelector('#aside');
let is_open = false


function openAside() {
    if (is_open) {
        aside.classList.add('aside_anime_down')
        setTimeout(function () {
            aside.style.display = 'none'
            aside.classList.remove('aside_anime_down')
        },200)
        is_open = false
    }else{
        aside.classList.add('aside_anime_up')
        setTimeout(function () {
            aside.style.display = 'block'
            aside.classList.remove('aside_anime_up')
        },200)
        is_open = true
    }
}