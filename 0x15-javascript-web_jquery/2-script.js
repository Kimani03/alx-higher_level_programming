// Javascript script that updates the textcolor of the <header> element
// to red (#FF0000) when the user clicks on the tag DIV#red_header:
const $ = window.$;
$('#red_header').blind('click',function () {
    $('header').css({ color: '#FF0000' });
});
