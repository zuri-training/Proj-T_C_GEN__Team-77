// (function () {
//     function checkTime(i) {
//         return (i < 10) ? "0" + i : i;
//     }

//     function startTime() {
//         var today = new Date(),
//             h = checkTime(today.getHours()),
//             m = checkTime(today.getMinutes()),
//             s = checkTime(today.getSeconds());
//         const timm = h + ":" + m + ":" + s;
//         document.querySelector(".time").innerHTML = timm
//         // document.querySelector(".date").innerHTML = today
//         t = setTimeout(function () {
//             startTime()
//         }, 500);
//     }
//     startTime();
// })();

// const date = new Date()
// document.querySelector(".date").innerHTML = date

// const today = new Date();
// const yyyy = today.getFullYear();
// let mm = today.getMonth() + 1; // Months start at 0!
// let dd = today.getDate();

// if (dd < 10) dd = '0' + dd;
// if (mm < 10) mm = '0' + mm;

// const formattedToday = dd + "-" + mm + "-" + yyyy;

// document.querySelector('.date').innerHTML = formattedToday;

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