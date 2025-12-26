f = open("salary.txt","a")
eid = input("ID: ")
name = input("Name: ")
basic = float(input("Basic Salary: "))
total = basic + basic*0.2 + basic*0.1
f.write(f"{eid},{name},{total}\n")
f.close()
print(open("salary.txt").read())
