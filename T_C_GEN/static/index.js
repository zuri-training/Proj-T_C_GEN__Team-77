// function googleTranslateElementInit() {
//     new google.translate.TranslateElement(
//         {pageLanguage: 'en', layout:
//         google.translate.TranslateElement.InlineLayout.HORIZONTAL},
//         'google_translate_element'
//     );
// }

// const translate = document.querySelector(".translate")

// translate.addEventListener("onload", function googleTranslateElementInit(e) {
//         e.target(
//             new google.translate.TranslateElement(
//                 {pageLanguage: 'en', layout:
//                 google.translate.TranslateElement.InlineLayout.SIMPLE},
//                 'google_translate_element'
//             )
//         )
        
// })

const trans = document.querySelector(".trans")

trans.addEventListener("click", () => {
    trans.classList.toggle("show")
})

function googleTranslateElementInit() {
    new google.translate.TranslateElement(
        {pageLanguage: 'en', layout:
        google.translate.TranslateElement.InlineLayout.SIMPLE},
        'google_translate_element'
    );
}

// function googleTranslateElementInit() {
//     new google.translate.TranslateElement(
//         {pageLanguage: 'en'},
//         'google_translate_element'
//     );
// }