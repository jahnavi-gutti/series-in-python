"""
A mountain is a non-empty sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a non-empty sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary’s sequence of up and down steps during his last hike, find and print the number of valleys he walked through."""
def countvalley(steps,path):
    valleycount=level=0
    d={"U":1,"D":-1}
    for step in path:
        level+=d[step]
        if level==0 and step=="U":
            valleycount+=1
    return valleycount
steps=int(input())
path=input()
print(countvalley(steps,path))
"""
8
UDDDUDUU
1"""
