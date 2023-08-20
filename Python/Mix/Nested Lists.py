# nested list 

if __name__ == '__main__':
    
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    secondlow = sorted(list(set(scores)))
    names = sorted([name for [name,score] in students if score == secondlow[1]])
    a = [print(i) for i in names]