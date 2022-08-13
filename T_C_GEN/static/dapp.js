menuBtn = document.querySelector(".bars")
closeBtn = document.querySelector(".close")
menu = document.querySelector('aside')

menuBtn.addEventListener('click', function(){
    menu.style.display = "block"
    menuBtn.style.display = "none"
})

closeBtn.addEventListener('click', function(){
    menu.style.display = "none"
    menuBtn.style.display = "block"
})