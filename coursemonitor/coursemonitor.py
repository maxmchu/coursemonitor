from courseupdate import courseUpdate
import time

class CourseMonitor:
    def __init__(self):
        self.courses = []

    def add_course(self, term, dept, number, section):
        course = [courseUpdate(term, dept, number, section), (term, dept, number, section)]
        self.courses.append(course)

    def check_courses(self):
        removals = []

        for course in self.courses:
            status = course[0].get_status()
            print ("{} {} {} status: {}".format(course[1][1], course[1][2], course[1][3], status))
            if (status == "open" or status == "archived"):
                print("Stopping monitoring...")
                removals.append(course)
            else:
                print("Continuing monitoring...")

        for course in removals:
            self.courses.remove(course)

    def refresh_status(self):
        while len(self.courses) > 0:
            self.check_courses()
            if (len(self.courses) > 0):
                time.sleep(10)