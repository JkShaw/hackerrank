# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y = map(int, raw_input().split()) #mm dd yyyy
print calendar.day_name[calendar.weekday(y, m, d)].upper()
