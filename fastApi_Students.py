from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str
    grade: float
    course: str    
    year:int

student_list=[]

@app.get("/")
def home():
    return{"message": f"STUDENT LIST {student_list}"}

#add #post ang una para magamit ang key/label para sa get 
@app.post("/students")
def add_student(student:Student):
    student_list.append({"id":student.student_id, "name":student.name, "grade":student.grade,"course":student.course,"year":student.year})
    return{"message": f"ID:{student.student_id}, Name:{student.name}, Grade:{student.grade}, Year:{student.year} added successfully!"}

#get&search
@app.get("/students")
def get_students(search: str=None, year_level: int=None, std_id: int =None):
    results  = student_list
    if search:
        results = [student for student in results if search.lower() in student["name"].lower()]
    if year_level: 
        results = [student for student in results if student["year"] == year_level]
    if std_id:
        results = [student for student in results if student["id"] == std_id]
    return{"students":results}


#delete
@app.delete("/student/{student_id}")
def delete_std(student_id:int):
    for id in student_list:
        if id["id"] == student_id:
            student_list.remove(id)
            return{"Message": f"ID:{student_id} has been Deleted!"}
    return{"Message": "Cannot find student"}

class update_student_grade(BaseModel):
    grade:float
#update
@app.put("/students/{student_id}")
def update_grade(student_id: int, updated: update_student_grade):
    for id in student_list:
        if id ['id'] == student_id:  
            old_grade = id["grade"] #saving old grade first
            id["grade"] = updated.grade #updating  old grade 
            return{"message":f"Student Grade Update from {old_grade} => {updated.grade}"}
    return{"message": "Student not found"}