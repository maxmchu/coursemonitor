from HTMLParser import HTMLParser

class CourseHTMLParser(HTMLParser):

    def __init__(self):
        self.status_classes = ["open-status-open", "open-status-closed", "open-status-warning", "open-status-archived"]
        self.section_names = []
        self.section_statuses = []
        self.valid = True
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if (tag == "ul"):
            for pair in attrs:
                if (len(pair) >= 2 and pair[0] == 'aria-label' and "Class Section" in pair[1]):
                    self.section_names.append(pair[1].replace("Class Section ", ""))

        if (tag == "i"):
            for pair in attrs:
                if (len(pair) >= 2):
                    attrlist = pair[1].split(" ")
                    matches = list(filter(lambda x: x in self.status_classes, attrlist))
                    if (len(matches) == 1):
                        status = matches[0].replace("open-status-", "")
                        status = status.replace("warning", "waitlisted")
                        self.section_statuses.append(status)

    def handle_data(self, data):
        if "Class Not Found." in data:
            self.valid = False
            print("Invalid URL!")

    def get_section_names(self):
        return self.section_names

    def get_section_statuses(self):
        return self.section_statuses