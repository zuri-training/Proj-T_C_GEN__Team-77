menuBtn = document.querySelector(".bars3")
closeBtn = document.querySelector(".close3")
menu = document.querySelector('.asi')

menuBtn.addEventListener('click', function(){
    menu.style.display = "block"
    menuBtn.style.display = "none"
})

closeBtn.addEventListener('click', function(){
    menu.style.display = "none"
    menuBtn.style.display = "block"
})