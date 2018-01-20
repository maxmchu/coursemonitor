import time
import twilio_handler

class CourseInfo:
    def __init__(self, term, dept, course, section):
        self.term = term
        self.dept = dept
        self.course = course
        self.section = section
        self.status = "new"

class CourseMonitor:
    def __init__(self):
        self.courses = []
        self.courses_to_monitor = 0
        self.twilio_client = twilio_handler.TwilioHandler()

    def add_course(self, courseInfo):
        self.courses.append(courseInfo)
        self.courses_to_monitor += 1

    def check_courses(self):

        for course in self.courses:

            if (course.monitor):
                course.past_status = course.status
                course.status = course.get_status()
                print ("{} {} {} status: {}".format(course.term, course.dept, course.course_num, course.status))

                if (course.past_status == "new"):
                    if (course.status != "closed"):
                        print("No monitoring needed, course is {}.".format(course.status))
                        course.monitor = False
                        self.courses_to_monitor -= 1
                    else:
                        print("Starting monitoring!")
                        self.twilio_client.send_start_message(course)

                else:
                    if (course.status != "closed" and course.status != course.past_status):
                        print("Stopping monitoring and sending a message")
                        self.twilio_client.send_update_message(course)

    def refresh_status(self):
        while self.courses_to_monitor > 0:
            self.check_courses()
            if (self.courses_to_monitor > 0):
                print("Checking again in 5 minutes...")
                # set to 5 minutes
                time.sleep(300)