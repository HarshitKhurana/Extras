
#!/usr/bin/python

class Student(object):
    """ Class representing student & reqd details of a student """

    def __init__ (self, name, cls, studentId):
        """ Constructor

        Args:
            name: Name of student
            cls : Class in which student in studying
            studentId: Unique ID of student
        """
        self.__name = name
        self.__cls = cls
        self.__studentId = studentId

    def __repr__ (self):
        return "Name: {}\nClass: {}\nStudentId: {}\n".\
                format(self.name, self.cls, self.studentId)

    @property
    def name(self):
        return self.__name
    @property
    def cls(self):
        return self.__cls
    @property
    def studentId(self):
        return self.__studentId

class StudentRecords():
    """Class for holding details of all the students"""

    # Kept singleton in-order to avoid potential multi-threading issues, as datastore is class variable.
    __instance__ = None     
    student_map = {}
    studentId = 112233

    def __init__(self):
        """Constructor """

        if StudentRecords.__instance__  is None:
            StudentRecords.__instance__ = self
        else:
            raise Exception('Only single instance of {} is allowed'.\
                    format(self.__class__.__name__))

    @staticmethod
    def getInstance():
        """Singleton Class"""

        if StudentRecords.__instance__:
            return StudentRecords.__instance__
        else:
            return StudentRecords()

    def addStudent(self, name, cls):
        """ Add student to datastore"""

        sid = StudentRecords.studentId
        student_object = Student(name, cls, sid)
        StudentRecords.student_map[sid] = student_object
        StudentRecords.studentId += 1
        return student_object.studentId

    def getStudent(self, studentId):
        """Fetch student details from datastore"""

        student_object = Student("",-1,-1)
        if studentId in StudentRecords.student_map:
            student_object = StudentRecords.student_map[studentId]
        return student_object

    def removeStudent(self, studentId):
        """ Remove student from datastore"""

        student_object = Student("",-1,-1)
        if studentId in StudentRecords.student_map:
            student_object = StudentRecords.student_map.pop(studentId)
        return student_object
