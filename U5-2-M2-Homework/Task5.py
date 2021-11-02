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
        
    for i, eachStudent in enumerate(students):
        # print("Greater than or = five:", students[eachStudent])
        topFive = sorted(students[eachStudent])[-5:]
        # print("Students Dict Sorted", students)
        # print("Top Five", topFive)
        topFiveSumed = sum(topFive) // len(topFive)
        results.append([i+1, topFiveSumed])
    return results
    

print("final Avg Score Per Student", csAverageOfTopFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
