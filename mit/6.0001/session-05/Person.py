import datetime

class Person(object):
    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """Returns self's full name"""
        return self.name

    def getLastName(self):
        """Returns self's last name"""
        return self.lastName

    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate."""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Returns self's name"""
        return self.name


class MITPerson(Person):
    # Class attribute
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year


class Grad(Student):
    pass


class Grades(object):

    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """Return a sorted list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

        
def gradeReport(course):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report = report + '\n'\
                     + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                     + str(s) + ' has no grades'

    return report


class InfoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Dont\'t look at me directly'

    def printVisible(self):
        print(self.visible)

    def printInvisible(self):
        print(self.__invisible)

    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)


if __name__ == '__main__':
    me = Person('Evan Vermilyea')
    him = Person('Bruce Wayne')
    her = Person('Wonder Woman')
    print(him.getLastName())

    him.setBirthday(datetime.date(1900, 8, 4))
    her.setBirthday(datetime.date(1900, 8, 5))
    print(him.getName(), 'is', him.getAge(), 'days old')

    pList = [her, him, me]

    for p in pList:
        print(p)

    pList.sort()

    for p in pList:
        print(p)

    p1 = MITPerson('John Snow')
    print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))

    p2 = MITPerson('Zombie')

    print('p1 < p2', p1 < p2)

    p3 = Grad('Buzz Aldrin')
    p4 = UG('Neil Armstrong', 50)

    print(p3, 'is a grad student is', type(p3) == Grad)
    print(p3, 'is an undergrad student is', type(p3) == UG)
    print(p4, 'is an undergrad student is', type(p4) == UG)

    print(p4, 'is a person is', isinstance(p4, Person))
    print(p4, 'is a student is', isinstance(p4, Student))
    print(p4, 'is an MITPerson is', isinstance(p4, MITPerson))

    print(p4, 'is type', type(p4))


    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')

    sixHundred = Grades()
    sixHundred.addStudent(ug1)
    sixHundred.addStudent(ug2)
    sixHundred.addStudent(g1)
    sixHundred.addStudent(g2)

    for s in sixHundred.getStudents():
        sixHundred.addGrade(s, 75)

    sixHundred.addGrade(g1, 25)
    sixHundred.addGrade(g2, 100)
    sixHundred.addStudent(ug3)

    print(gradeReport(sixHundred))

    infoHiding = InfoHiding()

    print(infoHiding.visible)
    print(infoHiding.__alsoVisible__)

    try:
        print(infoHiding.__invisible)
    except AttributeError:
        print('attribute error: infoHiding.__invisible')

    print(infoHiding.printInvisible())
    print(infoHiding.__printInvisible__())
    
    try:
        print(infoHiding.__printInvisible())
    except AttributeError as e:
        print(e)
