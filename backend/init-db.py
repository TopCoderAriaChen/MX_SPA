from app import create_app
from app.campus.model import Campus
from app.user.model import Admin, Student, Teacher, get_hashed_password
from app.course.model import Course
print("Loading...")

create_app()

print("Configuring database")
Campus.objects().delete()

unimelb_campus = Campus(name="University of Melbourne")
monash_campus = Campus(name="Monash University")
deakin_campus = Campus(name="RMIT University")
swinburne_campus = Campus(name="Swinburne University of Technology")
unimelb_campus.save()
monash_campus.save()
deakin_campus.save()
swinburne_campus.save()

admin = Admin(
    username="admin",
    display_name="Admin",
    password=get_hashed_password("password"),
    telephone="0414639683",
    permissions=["sys_owner", "campus_admin", "course_admin", "user_admin","order_admin", "lecture_admin"],
    campus=unimelb_campus,
)
admin.save()

support = Admin(
    username="support_1",
    display_name="Support A",
    password=get_hashed_password("password"),
    telephone="0414357395",
    permissions=["course_admin", "user_admin","order_admin", "lecture_admin"],
    campus=unimelb_campus,
)
support.save()

student = Student(
    username="student_1",
    display_name="John Smith",
    password=get_hashed_password("password"),
    telephone="04147343952",
    wx="wx123",
    uni="Unimelb",
    campus=unimelb_campus,
)
student.save()

teacher = Teacher(
    username="teacher_1",
    display_name="Michael Smith",
    password=get_hashed_password("password"),
    telephone="0414239943",
    abn="123123124124512",
    campus=unimelb_campus,
)
teacher.save()

course1 = Course(
  name= "Python-Basics",
  uni_course_code= "COMP90052",
  description= "Python 1 tutorial",
  teacher= teacher,
  campus=unimelb_campus,
  created_time= "2024-03-12T07:08:42.583000", 
  publish_time= "2024-03-12T07:08:42.583000", 
  original_price= "199.99",
  cover_image= "https://files.realpython.com/media/Newbie_Watermarked.a9319218252a.jpg",
  
)
course1.save()

course2 = Course(
  name= "Python-Intermediate",
  uni_course_code= "COMP90068",
  description= "Python 2 tutorial",
  teacher= teacher,
  campus=unimelb_campus,
  created_time= "2024-03-12T07:08:42.583000", 
  publish_time= "2024-03-12T07:08:42.583000", 
  original_price= "199.99",
  cover_image= "https://files.realpython.com/media/Newbie_Watermarked.a9319218252a.jpg",
  
)
course2.save()

course3 = Course(
  name= "Python-Advanced",
  uni_course_code= "COMP90086",
  description= "Python 3 tutorial",
  teacher= teacher,
  campus=unimelb_campus,
  created_time= "2024-03-12T07:08:42.583000", 
  publish_time= "2024-03-12T07:08:42.583000", 
  original_price= "199.99",
  cover_image= "https://files.realpython.com/media/Newbie_Watermarked.a9319218252a.jpg",
  
)
course3.save()
