from coursehtmlparser import CourseHTMLParser
import urllib2

class courseUpdate():

    def __init__(self, term, dept, number, section):
        self.url="https://classes.cornell.edu/browse/roster/{}/class/{}/{}".format(term, dept, number)
        self.section = section

    def get_status(self):

        location = urllib2.urlopen(self.url)
        htmldata = location.read()
        parser = CourseHTMLParser()
        parser.feed(htmldata)

        status = parser.get_section_statuses()[parser.get_section_names().index(self.section)]
        return status

