jQuery(document).ready(function($){
  
  $('button').on('click', function(){
    var values = [];
    const reducer = (previousValue, currentValue) => parseInt(previousValue) + parseInt(currentValue);
    $('[name="first_name"]:checked').each(function(){
      values.push($(this).val());
    }); 
    
    alert(values.reduce(reducer) + 'm2');
  });
  
});


// function changeItem() {
//   document.getElementById('one').style.display = 'none';
// }// функция, которая сработает при наведении.
// //она означает - выбрать элемент к Id у которого надо что-то изменить.
// // когда в скобки где написано one-two добавите Id своего элемента
// function rechangeItem() {
//   document.getElementById('one').style.display = 'flex';
// }// тут всё также. н