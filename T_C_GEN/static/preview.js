function generatePDF(){
    const element = document.getElementById("container");

    html2pdf()
    .from(element)
    .save();
}