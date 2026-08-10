#5.7-Chained_Conditionals (`elif`)
#Example 1 – Player Rank
score = 250
if score >= 500:
    print("Gold")
elif score >= 100:
    print("Silver")
else:
    print("Bronze")

#Example 2 – Grade System
marks = 82
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")