menuBtn = document.querySelector(".bars2")
closeBtn = document.querySelector(".close2")
menu = document.querySelector('.asid')

menuBtn.addEventListener('click', function(){
    menu.style.display = "block"
    menuBtn.style.display = "none"
})

closeBtn.addEventListener('click', function(){
    menu.style.display = "none"
    menuBtn.style.display = "block"
})