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
  //   document.getElementById('add_course_id') =4;
  //   document.getElementById("add_course").submit();// Form submission

  // })

  // var add_course_edit = document.getElementById('add_course_edit');
  // add_course_edit.onclick(addEventListener,function(){
  //   document.getElementById("update_course").disabled;// Form submission

  // })
  // var main_submit =document.getElementById('main_submit');
  // main_submit.addEventListener("click",function(){
  //   alert("inside main_submit")
  // })
  // function add(){
  //   alert("lalo");
  //   fetch('https://127.0.0.1:5000/admin/course/'+URLSearchParams({
  //       "course_id":"1"
  //     })
  //   )
  // }