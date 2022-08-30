def admin_course_get(args):
    data=0,{}
    if not args.get('course_id') and not args.get('category') and not args.get('status') and not args.get('instructor'):
        data =1,{
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
        else: # if corresponding data not found
            data =0,{}
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
        return "hola"
    elif form.get('type') == 'update':
        return "aloha"

def admin_course_update():
    pass