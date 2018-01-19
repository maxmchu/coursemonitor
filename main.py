from coursemonitor import coursemonitor

monitor1 = coursemonitor.CourseMonitor()
monitor1.add_course("SP18", "CS", "2110", "LEC 001")
monitor1.add_course("SP18", "ECON", "3300", "LEC 001")

monitor1.refresh_status()