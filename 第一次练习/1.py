

def toLevel (score):
    if(90 <= score <= 100 ): return 'A'
    elif(70 <= score < 90): return 'B'
    elif(60 <= score < 70): return 'C'
    elif(score < 60): return 'D'
    else: return 'invalid score'

score = input()

s = toLevel(score)

print(s)