from builtins import object

class StudentSerializer(object):
    def __init__(self, data):
        self.data = data # init with a QuerySet

    @property
    def all_students(self):
        output = {'students': []}
        for student in self.data:
            student_data = {
                'first_name': student.first_name,
                'last_name': student.last_name
            }
            output['students'].append(student_data)
        return output
    
    @property
    def detail_student(self):
        return {
                'first_name': self.data.first_name,
                'last_name': self.data.last_name
            }
        
class CourseSerializer(object):
    def __init__(self, data):
        self.data = data

    @property
    def all_courses(self):
        output = {'courses': []}
        for course in self.data:
            course_data = {
                'course_id': course.course_id,
                'course_name': course.course_name
            }
            output['courses'].append(course_data)
        return output
        
    @property
    def detail_course(self):
        return {
                'course_id': self.data.course_id,
                'course_name': self.data.course_name
            }