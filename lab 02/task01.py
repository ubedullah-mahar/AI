# task 01
#  student performance analyzer 

students={
    "ubedullah":94,
    "shahzeb":81,
    "moiz":67,
    "subhash":89,
    "najaf":98
}
sum=0
max=0;
topper=" "
for i in students:
    if students[i]>max:
        topper=i
        max=students[i]
    sum+=students[i]
    if students[i]>90 and students[i]<=100:
        print(i ," A grade")
    elif students[i]>=80 and students[i]<=90:
        print(i ," B grade")
    elif students[i]>=70 and students[i]<80:
        print(i ," C grade")
    else :
        print(i ,"fail")
    

avg=sum/len(students)
print("average of the class is ", avg)
print("topper of the class is ",topper)







