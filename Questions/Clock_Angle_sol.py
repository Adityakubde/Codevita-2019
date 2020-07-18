a=int(input())
b=float(input())
hour=((a/360)*b)%12
minutes=int((hour-int(hour))*60)
hour=int(hour)
if hour==12:hour=0
if minutes==60:minutes=0
angle=abs((0.5*(hour*60+minutes))-(minutes*6))
print("%.2f"%min(360-angle,angle))
