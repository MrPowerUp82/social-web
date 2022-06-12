const mario = document.querySelector('.mario')
const pipe = document.querySelector('.pipe')
const button = document.querySelector('.button-container')
let score = 0
const scoreSpan = document.querySelector('.score')
let char = 1
let token = document.cookie.replace('csrftoken=','')


async function api_post(){
    await fetch(`/api/score/`,{
    method: 'POST',
    headers: {"X-CSRFToken": token,'Content-Type': 'application/json'},
    body: JSON.stringify({score: score})
    }).then(r=>r.json()).then(json=>console.log(json))
}

if(localStorage.getItem('char')){
    char = parseInt(localStorage.getItem('char'))
}

if(char == 2){
    mario.src="/static/images/sonic.gif"
}

function charChange(value){
    if(value){
        char = value
        localStorage.setItem('char', value.toString())
    }
}

for (ele of button.children[3].children){
    if(ele.value == char){
        ele.selected=true
    }
}

function buttonClick(){
    window.location.reload()
}

document.addEventListener('keydown', (e) => {
    mario.classList.add('jump')
    setTimeout(() => {
        mario.classList.remove('jump')
    },501)
})

document.addEventListener('touchstart', (e) => {
    mario.classList.add('jump')
    setTimeout(() => {
        mario.classList.remove('jump')
    },501)
})

function saveScore(score){
    let oldScore = localStorage.getItem('score')
    if (oldScore){
        if (parseInt(oldScore) < score){
            localStorage.setItem('score', score.toString())
            return score
        }else{
            return parseInt(oldScore)
        }
    }else{
        localStorage.setItem('score', score.toString())
        return score
    }
}

const countScore = setInterval(() => {
    score += 1
    scoreSpan.innerHTML = score
},500)

const loop = setInterval(() => {
    const marioPosition = parseFloat(window.getComputedStyle(mario).bottom.replace('px', ''))

    const pipePosition = pipe.offsetLeft

    if (pipe.offsetLeft <= 120 && pipe.offsetLeft > 0 && marioPosition < 60){
        pipe.style.animation= 'none'
        pipe.style.left= `${pipePosition}px`

        mario.style.animation= 'none'
        mario.style.bottom= `${marioPosition}px`

        mario.src= char == 1 ? "/static/images/game-over.png" : "/static/images/sonic-game-over.png"
        mario.style.width= '75px'
        mario.style.marginLeft = '50px'

        clearInterval(loop)
        clearInterval(countScore)
        button.style.display="block"
        let bestscore = saveScore(score)
        button.children[0].innerHTML = `Best Score: ${bestscore}`
        button.children[1].innerHTML = `Score: ${score}`
        if (score >= bestscore) {
            api_post()
        }
    }
},11)