def get_all_prereqs():
    req = []
    if len(self.prereqs) == 0:
        return []
    else:
        for course in req:
            req.append(course.get_all_prereqs())
        
