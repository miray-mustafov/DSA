def printMaxActivities(activities):
    activities.sort(key=lambda x: x[2])
    i = 0
    firstA = activities[i][0]
    print(firstA)
    for next_i in range(1, len(activities)):
        if activities[next_i][1] > activities[i][2]:
            i = next_i
            print(activities[next_i][0])


activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9], ]

printMaxActivities(activities)
