from unicodedata import category
from . import db
from sqlalchemy.sql import func

class Role(db.Model):
    role_id = db.Column(db.String(25),primary_key =True)
    role_name = db.Column(db.String(25),primary_key =False)
    user_ids = db.relationship('User',backref='role')

class Qualification(db.Model):
    qualification_id = db.Column(db.String(25),primary_key =True)
    qualification_name =db.Column(db.String(25),primary_key =False)
    status =db.Column(db.String(25),primary_key =False)

class User(db.Model):
    user_id =db.Column(db.Integer,primary_key =True)
    full_name =db.Column(db.String(25),primary_key =False)
    hashed_password = db.Column(db.String(25),primary_key =False)
    role_id =db.Column(db.String(25),db.ForeignKey('role.role_id'))
    email = db.Column(db.String(25),primary_key =False)
    phone = db.Column(db.String(25),primary_key =False)
    log_ids = db.relationship('Activity_Log',backref='user')
    course_ids = db.relationship('Course',backref='user')
    enrollment_ids = db.relationship('Enrollment',backref='user')
    enquiry_ids = db.relationship('Enquiry',backref='user')

class Activity_Log(db.Model):
    log_id = db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())


class User_Qualification(db.Model):
    index =db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    qualification_id = db.Column(db.Integer,db.ForeignKey('qualification.qualification_id'))

class Category(db.Model):
    category_id = db.Column(db.String(25),primary_key =True)
    category_name = db.Column(db.String(25),primary_key =False)
    status =db.Column(db.String(25),primary_key =False)
    narration = db.Column(db.String(25),primary_key =False)
    course_ids = db.relationship('Course',backref='category')

class Course(db.Model):
    course_id = db.Column(db.String(25),primary_key =True)
    course_name = db.Column(db.String(25),primary_key =False)
    category_id = db.Column(db.String(25),db.ForeignKey('category.category_id'))
    course_duration = db.Column(db.Integer,primary_key =False)
    instructor_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    max_batch_size = db.Column(db.String(25),primary_key =False)
    description = db.Column(db.String(50),primary_key =False)
    preview_link = db.Column(db.String(50),primary_key =False)
    syllabus =  db.Column(db.String(100),primary_key =False)
    rating =  db.Column(db.String(25),primary_key =False)
    status =  db.Column(db.String(25),primary_key =False)
    narration = db.Column(db.String(25),primary_key =False)
    enrollment_ids = db.relationship('Enrollment',backref='course')
    enquiry_ids = db.relationship('Enquiry',backref='course')

class Course_Requirement(db.Model):
    requirement_id = db.Column(db.String(25),primary_key =True)
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    qualification_id = db.Column(db.Integer,db.ForeignKey('qualification.qualification_id'))
    min_percentage = db.Column(db.String(25),primary_key =False)

class Batch(db.Model):
    batch_id = db.Column(db.String(25),primary_key =True)
    batch_name = db.Column(db.String(25),primary_key =False)
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    status = db.Column(db.String(25),primary_key =False)
    enrollment_ids = db.relationship('Enrollment',backref='batch')

class User_Batch(db.Model):
    index =db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    batch_id = db.Column(db.String(25),db.ForeignKey('batch.batch_id'))

class Enrollment(db.Model):
    enrollment_id =db.Column(db.Integer,primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    course_id = db.Column(db.String(25),db.ForeignKey('course.course_id'))
    batch_id = db.Column(db.String(25),db.ForeignKey('batch.batch_id'))
    status = db.Column(db.String(25),primary_key =False)
    score = db.Column(db.String(25),primary_key =False)

class Enquiry(db.Model):
    enquiry_id =db.Column(db.String(25),primary_key =True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    course_id =  db.Column(db.String(25),db.ForeignKey('course.course_id'))
    enquiry = db.Column(db.String(100),primary_key =False)
    status = db.Column(db.String(25),primary_key =False)
    comment = db.Column(db.String(50),primary_key =False)


