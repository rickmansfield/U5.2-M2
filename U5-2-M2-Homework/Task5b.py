import math
def csAverageOfTopFive(scores):
    '''
    Input: a nested array of students ids and their scores
    Output: a nested array of the students average scores
    '''
    students = {}
    results = []
    
    for student in scores:
        if student[0] not in students:
            students[student[0]] = []
        students[student[0]].append(student[1])
        
    for stud in students:
        stud = students[stud].sort()
        print(students)
        
    for stu in students:
        if len(students[stu]) > 5:
            students[stu] = students[stu][-5:]
    
    for st in students:
        students[st] = math.floor(sum(students[st]) / len(students[st]))
    
    for key, value in students.items():
        results.append([key, value])
        
    return results
    
    

print(csAverageOfTopFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
