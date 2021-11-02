# def csAverageOfTopFive(scores):
#     if not scores:
#         return []

#     scoresMap = {}
#     for eachscore in scores:
#         if eachscore[0] in scoresMap:
#             scoresMap[eachscore[0].append(eachscore[1])]
#             print(scoresMap)
#         else:
#             # print("made it to else")
#             scoresMap[eachscore[0]] = []

#     results = []
#     for key, value in scoresMap.items():
#         value.sort(reverse=True)
#         if len(value) >= 5:
#             average = value[:5]
#         else:
#             average = value

#         scoresMap[key] = sum(average)//len(average)
#         results.append([key, scoresMap[key]])

#     return results

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
