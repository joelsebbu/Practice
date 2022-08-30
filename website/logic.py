import random 
import pyodbc
import json

connString = 'Driver={SQL Server};Server=DESKTOP-UDFFDCR\SQLEXPRESS;Database=learnify;Trusted_Connection=yes;'
conn = pyodbc.connect(connString)
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM course")
courses = []


for course in cursor:
    courses.append({
        "img_url":"thisistheimageurl",
        "course_id": course[0],
        "course_name":course[1],
        "instructor": course[4],
        "category_id": course[2],
        "course_duration": course[3],
        "max_batch_size": course[5],
        "description":course[6],
        "preview_video":course[7],
        "syllabus":course[8],
        "status":course[10],
        "narration":course[11]
    })




def admin_course_get(args):
    
    
    

    data=0, json.dumps({
        "category":["code","arts","buisness","crypto"],
        "status":["active","disabled"],
        "instructor":["9","3"],
        "course": courses
    })

    if not args.get('course_id') and not args.get('category') and not args.get('status') and not args.get('instructor'):
        #return all data
        data =1,json.dumps({
        "category":["code","arts","buisness","crypto"],
        "status":["active","disabled"],
        "instructor":["9","3"],
        "course": courses
    }) 

    elif args.get('course_id'):
        if args.get('course_id') == "java":
            data =1,{
                "category":["code","arts","buisness","crypto"],
                "status":["active","disabled"],
                "instructor":["1","2"],
                "course":[
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
        else: # if corresponding data not found so 0 is send
              # 0 means flash has to be send to say error 
            data =0,{
                "category":["code","arts","buisness","crypto"],
                "status":["new","in_review","admitted","rejected"],
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
    else:
        category =args.get('category')
        status = args.get('status')
        instructor =args.get('instructor')
        if category and status and instructor:
            pass
        elif category:
            if status:
                pass
            elif instructor:
                pass
            else:
                pass
        elif status:
            if instructor:
                pass
            else:
                pass
        elif instructor:
            pass
        
    return data

def admin_course_add(form):
    if form.get('type') == 'add':
        
        # add info and make a redirect to /admin/course
        return "hola"
    elif form.get('type') == 'update':
        return "aloha"

def admin_course_update():
    pass

def admin_enquiry_get(args):
    db=""
    enq_id =str(random.randrange(1, 1000))
    data=0,{"category":["code","arts","buisness","crypto"],
            "status":["active","disabled"],
            "instructor":["1","2"],
            "course":["c++","java","py"],
            "enquiry":[
                {
                    "img_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.aJAThVeZ_XpZ_nr6T7lPvQHaE7%26pid%3DApi&f=1",
                    "course_id":"c++",
                    "user_id":6,
                    "enquiry_id":enq_id,
                    "instructor": 2,
                    "status":"new",
                    "comment":"adipoli",
                    "enquiry":"how is this course"
                },
                {
                    "img_url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.aJAThVeZ_XpZ_nr6T7lPvQHaE7%26pid%3DApi&f=1",
                    "course_id":"java",
                    "user_id":6,
                    "enquiry_id":"7",
                    "instructor": 5,
                    "status":"admitted",
                    "comment":"adipoli kollam",
                    "enquiry":"I'll pay for it"
                }
            ]
        }
    return data