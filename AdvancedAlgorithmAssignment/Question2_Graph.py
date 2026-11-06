class Course:
    def __init__(self, courseCode, courseName, creditHours, level):
        self.courseCode = courseCode
        self.courseName = courseName
        self.creditHours = creditHours
        self.level = level


class UDGraph:
    def __init__(self):
        self.adj_list = dict()

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)

        else:
            raise ValueError("One or both vertices are not found in the graph")

    def removeEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            if to_vertex in self.adj_list[from_vertex]:
                self.adj_list[from_vertex].remove(to_vertex)

    def listIncomingAdjacentVertex(self, courseCode):
        for vertex in self.adj_list:
            if vertex.courseCode == courseCode:
                print(f"Prerequisites for {vertex.courseCode}:")
                found = False
                for neighbour in self.adj_list:
                    if vertex in self.adj_list[neighbour]:
                        print(f"- {neighbour.courseCode} ({neighbour.courseName})")
                        found = True

                if not found:
                    print("No prerequisites found.")

                return
        print(f"The Course Code ({courseCode}) does not exist.")

    def listOutGoingAdjacentVertex(self, courseCode):
        for vertex in self.adj_list:
            if vertex.courseCode == courseCode:
                print(f"Course unlocked by {vertex.courseCode}:")
                found = False
                for neighbour in self.adj_list:
                    if neighbour in self.adj_list[vertex]:
                        print(f"- {neighbour.courseCode} ({neighbour.courseName})")
                        found = True

                if not found:
                    print("No unlocks found.")

                return
        print(f"The Course Code ({courseCode}) does not exist.")

    def searchCourse(self, courseCode):
        for vertex in self.adj_list:
            if vertex.courseCode == courseCode:
                print(f"Course Code: {vertex.courseCode}\n"
                      f"Course Name: {vertex.courseName}\n"
                      f"Credit Hours: {vertex.creditHours}")
                return
        print(f"The Course Code ({courseCode}) does not exist.")

    def display_all(self):
        count = 1
        for vertex in self.adj_list:
            print(f"{count}. {vertex.courseCode} - {vertex.courseName}")
            count += 1
        return

    def addCourse(self, course):
        for vertex in self.adj_list:
            if vertex.courseCode == course.courseCode:
                print(f"The course code ({vertex.courseCode}) already exists.")
                return
        self.addVertex(course)
        return

    def addPrerequisite(self, course_id, prereq_id):
        course = None
        prerequisite = None

        for vertex in self.adj_list:
            if vertex.courseCode == course_id:
                course = vertex
            elif vertex.courseCode == prereq_id:
                prerequisite = vertex
        if course is None:
            print(f"The course ({course_id}) does not exist.")
            return
        if prerequisite is None:
            print(f"The prerequisite course ({prereq_id}) does not exist.")
            return
        if course == prerequisite:
            print(f"A course cannot be its own prerequisite.")
            return
        if course in self.adj_list[prerequisite]:
            print(f"The prerequisite has already been added to this course.")
            return
        if int(course.level) < int(prerequisite.level):
            print(f"A higher-level course cannot be a prerequisite for a lower-level course.")
            return
        self.addEdge(prerequisite, course)
        return

    def removePrequisite(self, course_id, prereq_id):
        course = None
        prerequisite = None

        for vertex in self.adj_list:
            if vertex.courseCode == course_id:
                course = vertex
            elif vertex.courseCode == prereq_id:
                prerequisite = vertex
        if course is None:
            print(f"The course ({course_id}) does not exist.")
            return
        if prerequisite is None:
            print(f"The prerequisite course ({prereq_id}) does not exist.")
            return
        if course == prerequisite:
            print(f"A course cannot be its own prerequisite.")
            return
        if course in self.adj_list[prerequisite]:
            self.removeEdge(prerequisite, course)
        else:
            print(f"The course ({course_id}) does not have the course ({prereq_id}) as its prerequisite.")
        return


graph = UDGraph()

courses = {
    "C001": Course("C001", "Intro to Programming", "4", "1"),
    "C002": Course("C002", "Discrete Mathematics", "3", "1"),
    "C003": Course("C003", "Computer Fundamentals", "3", "1"),
    "C004": Course("C004", "Object-Oriented Programming", "4", "2"),
    "C005": Course("C005", "Data Structures and Algorithms", "4", "2"),
    "C006": Course("C006", "Advanced Algorithm", "4", "3")
}

for course in courses.values():
    graph.addVertex(course)

prerequisites = [
    ("C001", "C004"),
    ("C001", "C005"),
    ("C002", "C004"),
    ("C002", "C005"),
    ("C003", "C005"),
    ("C004", "C006"),
    ("C005", "C006")
]

for course, unlocked in prerequisites:
    graph.addEdge(courses[course], courses[unlocked])

while True:
    print(f"=== Course Prerequisite System ==="
          f"\n1. View All Courses"
          f"\n2. View Course Details"
          f"\n3. View Prerequisite of a Course"
          f"\n4. View Courses Unlocked by a Course"
          f"\n5. Add Course"
          f"\n6. Add Prerequisite to a Course"
          f"\n7. Remove Prerequisite from a Course"
          f"\n8. Exit")
    option = input("Select an option: ")

    match option:
        case "1":
            graph.display_all()
            print(f"")

        case "2":
            course_code = input(f"Enter the course code: ")
            graph.searchCourse(course_code)
            print(f"")

        case "3":
            course_code = input(f"Enter the course code: ")
            graph.listIncomingAdjacentVertex(course_code)
            print(f"")

        case "4":
            course_code = input(f"Enter the course code: ")
            graph.listOutGoingAdjacentVertex(course_code)
            print(f"")

        case "5":
            course_code = input(f"Enter the course code: ")
            course_name = input(f"Enter the course name: ")
            credit_hour = input(f"Enter the credit hour: ")
            level = input(f"Enter the level: ")
            course = Course(course_code, course_name, credit_hour, level)
            graph.addCourse(course)

        case "6":
            course_code = input(f"Enter the course code: ")
            prerequisite_code = input(f"Enter the course code to add as a prerequisite: ")
            graph.addPrerequisite(course_code, prerequisite_code)

        case "7":
            course_code = input(f"Enter the course code: ")
            prerequisite_code = input(f"Enter the course code to add as a prerequisite: ")
            graph.removePrequisite(course_code, prerequisite_code)

        case "8":
            print(f"Exiting System.")
            break
