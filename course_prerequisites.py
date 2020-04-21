#You are given a hash table where the key is a course code, and the value is a list of
#all the course codes that are prerequisites for the key. Return a valid ordering in
#which we can complete the courses. If no such ordering exists, return NULL.

#Example:
#{
#  'CSC300': ['CSC100', 'CSC200'], 
#  'CSC200': ['CSC100'], 
#  'CSC100': []
#}

#This input should return the order that we need to take these courses:
# ['CSC100', 'CSC200', 'CSCS300']


def courses_to_take(course_to_prereqs): #O(n_courses * n_prereqs) time O(n) memory
  n = len(course_to_prereqs)
  visited = set()
  order = []
  while len(order) < n:
    visited_something = False
    keys = list(courses.keys())
    for key in keys:
      can_visit_now = True
      for course in courses[key]:
        if course not in visited:
          can_visit_now = False
      if can_visit_now:
        visited_something = True
        visited.add(key)
        order.append(key)
        del courses[key]
        break
    if not visited_something:
      return None
  return order

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
