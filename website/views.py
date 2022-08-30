from ctypes.wintypes import HLOCAL

from flask import Blueprint,render_template,request
from . import logic

views = Blueprint('views',__name__)

@views.route('/admin/course')
def admin_course_load():
    args =request.args
    data =logic.admin_course_get(args)
    return render_template('admin_course.html',data =data[1])

@views.route('/admin/course',methods=['POST'])
def admin_course_add():
    form =request.form
    data = logic.admin_course_add(form)
    return render_template('admin_course.html',data =data[1])

@views.route('/admin/enquiry')
def admin_enquiry_load():
    args =request.args
    data =logic.admin_enquiry_get(args)
    return render_template('admin_enquiry.html',data = data[1])