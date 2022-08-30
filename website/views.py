from ctypes.wintypes import HLOCAL

from flask import Blueprint,render_template,request

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
                "instructor": 2,
                "category_id": 'code',
                "course_duration": "4",
                "max_batch_size": "20",
                "description":"kollam",
                "preview_video":"youtube.com/mrbeast",
                "syllabus":"into maathram",
                "status":"active",
                "narration":"adipoli"
            },
            {   
                "img_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.aJAThVeZ_XpZ_nr6T7lPvQHaE7%26pid%3DApi&f=1",
                "course_id":"java",
                "course_name":"coding in java",
                "instructor": 5,
                "category_id": 'code',
                "course_duration": "4",
                "max_batch_size": "20",
                "description":"kollam",
                "preview_video":"youtube.com/mrbeast",
                "syllabus":"into maathram",
                "status":"disabled",
                "narration":"adipoli"
            }
        ]
    }
    return render_template('admin_course.html',data =data)

@views.route('/admin/course',methods=['POST'])
def admin_course_add():
    print(request.form.get('type'))
    if request.form.get('type') == 'add':
        return "hola"
    elif request.form.get('type') == 'update':
        return "aloha"