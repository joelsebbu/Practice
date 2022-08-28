from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    data ={
        "category":["code","arts","buisness","crypto"],
        "status":["active","disabled"],
        "instructor":["1","2"]
    }
    return render_template('admin_course.html',data =data)