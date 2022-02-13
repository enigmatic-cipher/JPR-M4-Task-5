"""
Given a string as input, print the index of the first, second and third occurrence of 0 in the string or else print "Not Found".
Input-> "9810098100"
Output-> First:3 Second:4 Third:8
"""

st = "9810098100"
ln = len(st)
index = 0
for i in range(0,ln):
  e = st[i]
  if (e=="0"):
    print(f"First:{i}")
    index = index + int(i)
  elif (e=="0" and i>index):
    print(f"Second={i}")
    index = index + int(i)
  elif (e=="0" and i>index):
    print(f"Third={i}")
