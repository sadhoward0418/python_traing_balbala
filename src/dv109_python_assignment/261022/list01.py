#串列初始化
course_names = [
    "Python",
    "FastAPI",
    "MySQL",
    1

]

tmp=[]

print(course_names[0])
print(course_names[3])

mystr= "I Love Python"
print(mystr[0]) #字串也是一個list

for course_name in course_names: 
    print(course_name)

courses=[["python",4],
         ["Java",6],
         ["LLM",4],
         ["DB",3]
]

print(courses[0])
newcourse="AI Security"
newcourses=["PA", "Cymulate"]
courses.append(newcourse)
print(courses)
courses.extend(newcourse)
print(courses)
print(len(courses))

learner = {
    "name": "小明",
    "hours_per_week": 8,
    "goal": "學會 Python",
    "courses":["Python","AI agent"],
    "newcourses":[["LLM",4],["DB",3]]
}

print(learner["name"]) #小明
print(learner["courses"])

print(learner["name"])
print(learner["courses"])
print(learner["courses"][0])
print(learner["courses"] [1])
print(learner['newcourses'][0][0])
print(learner['newcourses'] [0] [1]) 

goal=learner.get("score","未提供分數") 
#物件導向
print(goal)
#print(learner["score"])

#在for迴圈中,條件指定可存取対象的key value

for key, value in learner.items():
    print(key, value)