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