import math
total=int(input("Enter the total number of data available "))
true=int(input("Enter the number of trues in the data "))
false=int(input("Enter the number of falses in the data "))
info_D=(-(true/total)*math.log(true/total,2))+(-(false/total)*math.log(false/total,2))
print("Expected info is : ",info_D)
m=1
while m==1 :
    t=0
    num=int(input("Enter the number of condition in the selected attribute "))
    for i in range(0,num):
        true1=int(input("Enter the number to trues in the condition of  selected Attribute "))
        false1=int(input("Enter the number to falses in the condition of selected Attribute "))
        total1=true1+false1
        if true1 == 0:
            true_t = 0
        else:
            true_t=(-(true1/total1)*math.log(true1/total1,2))
        if false1 == 0:
            false_t = 0
        else:
            false_t=(-(false1/total1)*math.log(false1/total1,2))
        t1=(total1/total)*(true_t+false_t)
        t=t+t1
    print("Info of the given attribute is : ",t)
    print("Gain of the given attribute is : ",info_D-t)
    m=int(input("To continue with other attribute enter 1, else enter any other number "))