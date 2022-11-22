hour,minute=map(int,input().split())
if minute>=45:
    minute-=45
else:
    minute+=15
    # minute= 60 - ( 45 - minute )
    if hour:
        hour -= 1
    else:
        hour = 23
print(hour,minute)