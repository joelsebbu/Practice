// var instance = M.Tabs.init(el);
// document.addEventListener('DOMContentLoaded', function() {
//     var el = document.querySelectorAll('.tabs');
//     var instance = M.Tabs.init(el);
//   });
//   document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('select');
//     var instances = M.FormSelect.init(elems);
//   });

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems);
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
  });
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
  });

  // var add_course_submit = document.getElementById('add_course_submit');
  // add_course_submit.onclick(addEventListener,function(){
  //   document.getElementById("add_course").submit();// Form submission

  // })

  // var add_course_edit = document.getElementById('add_course_edit');
  // add_course_edit.onclick(addEventListener,function(){
  //   document.getElementById("update_course").disabled;// Form submission

  // })