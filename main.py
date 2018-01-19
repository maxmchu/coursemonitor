from coursemonitor import coursemonitor, courseinfo

monitor1 = coursemonitor.CourseMonitor()

course1 = courseinfo.CourseInfo("SP18", "CS", "2110", "LEC 001")
course2 = courseinfo.CourseInfo("SP18", "ECON", "3300", "LEC 001")

monitor1.add_course(course1)
monitor1.add_course(course2)

monitor1.refresh_status()