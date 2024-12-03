from copy import copy

def unsafeCheck(report):
    for i in range(len(report)):
        try:
            if report[i+1] == report[i] or abs(report[i] - report[i+1]) > 3:
                return False
        except:
            pass
        
    if sorted(report) == report or sorted(report, reverse=True) == report:
        return True
    else:
        return False
        

with open("input.txt", "r") as f:
    approved = 0
    unsafe = []
    reports = []
    
    for line in f:
        safe = True
        line = line.strip().split()
        reports.append ([int(level) for level in line])

for report in reports:
    if unsafeCheck(report) == True:
        approved += 1
    else:
        unsafe.append(report)

print(f"Part one: {approved}")

for report in unsafe:
    for i in range(len(report)):
        tmpReport = copy(report)
        del(tmpReport[i])

        if unsafeCheck(tmpReport) == True:
            approved += 1
            break
        
        tmpReport = copy(report)

print(f"Part two: {approved}")
