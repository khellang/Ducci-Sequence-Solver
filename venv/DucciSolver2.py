def check_end(ducci):
    return all(i == 0 for i in ducci)

def compute(ducci):
    copy = ducci[0]
    new_seq = ducci
    for i in range(0,len(ducci)-1):
        new_seq[i] = abs(ducci[i] - ducci[i+1])
    new_seq[len(ducci)-1] = abs(ducci[len(ducci)-1] - copy)
    return tuple(new_seq)

def solve(ducci):
    check_dupl = set()
    steps = 0
    while(check_end(ducci) != True):
        ducci = compute(list(ducci))
        if(tuple(ducci) in check_dupl):
            break
        else:
            check_dupl.add(ducci)
            steps += 1
    return steps

ducci1 = [1,5,7,9,9]
ducci2 = [1,2,1,2,1,0]
ducci3 = (10,12,41,62,31,50)
ducci4 = (10,12,41,62,31)

steps = solve(ducci4)

print(steps)