credit=[]
grade=[]
SGPA=0
Sum=0
n=int(input("Enter the number of subjects : "))
print("\nEnter the credits and grade points of individual subjects:")
for i in range(n):
    credit.append(int(input(f"\nCredit of subject {i+1} : ")))
    grade.append(int(input(f"Grade point of subject {i+1}   : ")))
    Sum+=(credit[i]*grade[i])
SGPA=Sum/sum(credit)
print(f"The SGPA is {SGPA}")