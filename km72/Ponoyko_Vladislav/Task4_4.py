x=int(input())
if(((x%4==0) & (x%100!=0)) | (x%400==0)):
    print('this year is intercalary')
else:
    print('this year in not intercalary')
