from coursehtmlparser import CourseHTMLParser
import urllib2

class CourseInfo:

    def __init__(self, term, dept, course_num, section):
        self.term = term
        self.dept = dept
        self.course_num = course_num
        self.section = section
        self.status = "new"
        self.past_status = ""
        self.url = "https://classes.cornell.edu/browse/roster/{}/class/{}/{}".format(term, dept, course_num)
        self.monitor = True


    def get_status(self):

        location = urllib2.urlopen(self.url)
        htmldata = location.read()
        parser = CourseHTMLParser()
        parser.feed(htmldata)

        self.status = parser.get_section_statuses()[parser.get_section_names().index(self.section)]
        return self.status