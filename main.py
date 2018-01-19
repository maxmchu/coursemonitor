from coursemonitor import coursemonitor, courseinfo

# Edit this file to add your own courses

# Create a new CourseMonitor
monitor1 = coursemonitor.CourseMonitor()

# Create your courses
course1 = courseinfo.CourseInfo("SP18", "CS", "2110", "LEC 001")
# course2 = courseinfo.CourseInfo("SP18", "ECON", "3300", "LEC 001")
course3 = courseinfo.CourseInfo("SP18", "CS", "4780", "LEC 001")

# Add your courses to the monitor
monitor1.add_course(course1)
# monitor1.add_course(course2)
monitor1.add_course(course3)

# Begin monitoring
monitor1.refresh_status()