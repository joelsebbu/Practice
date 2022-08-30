from urllib import request
from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/admin/course')
def admin_course_load():
    data ={
        "category":["code","arts","buisness","crypto"],
        "status":["active","disabled"],
        "instructor":["1","2"],
        "course":[
            {
                "img_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.aJAThVeZ_XpZ_nr6T7lPvQHaE7%26pid%3DApi&f=1",
                "course_id":"c++",
                "course_name":"coding in cpp",
                "instructor": 2
            },
            {   
                "img_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.aJAThVeZ_XpZ_nr6T7lPvQHaE7%26pid%3DApi&f=1",
                "course_id":"java",
                "course_name":"coding in java",
                "instructor": 5
            }
        ]
    }
    return render_template('admin_course.html',data =data)

@views.route('/admin/course',methods=['POST'])
def admin_course_add():
    return request.form.get('add_course_id')
    # if request.form.get('add_course_id') == '55':
    #     return 'hola'
    # else:
    #     return 'no hola'