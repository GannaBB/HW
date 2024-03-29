x = 570

A=x//100
B=x%100//10
C=x%10
print(A, ' ', B, ' ', C)

if A!=0:
    
    if A==1:
        first_word='one hundred'
    elif A==2:
        first_word='two hundred'
    elif A==3:
        first_word='three hundred'
    elif A==4:
        first_word='four hundred'
    elif A==5:
        first_word='five hundred'
    elif A==6:
        first_word='six hundred'
    elif A==7:
        first_word='seven hundred'
    elif A==8:
        first_word='eight hundred'
    elif A==9:
        first_word='nine hundred'
else: first_word=''



if B!=0:
    if B==2:
        second_word='twenty'
    elif B==3:
        second_word='thirty'
    elif B==4:
        second_word='fourty'
    elif B==5:
        second_word='fifty'
    elif B==6:
        second_word='sixty'
    elif B==7:
        second_word='seventy'
    elif B==8:
        second_word='eighty'
    elif B==9:
        second_word='ninety'
    if  B==1: 
        if C==0: second_word='ten'
        elif C==1: second_word='eleven'
        elif C==2: second_word='twelve'
        elif C==3: second_word='thirteen'
        elif C==4: second_word='fourteen'
        elif C==5: second_word='fifteen'
        elif C==6: second_word='sixteen'
        elif C==7: second_word='seventeen'
        elif C==8: second_word='eighteen'
        elif C==9: second_word='nineteen'
else: second_word=''
       
if B!=1 or (A==0 and B==0):
    if C==0: third_word=''
    if C==1: third_word='one'
    if C==2: third_word='two'
    if C==3: third_word='three'
    if C==4: third_word='four'
    if C==5: third_word='five'
    if C==6: third_word='six'
    if C==7: third_word='seven'
    if x==8: third_word='eigth'
    if x==9: third_word='nine'

if A==0 and B==0 and C==0:
    third_word='zero'
if B==1:
    third_word = ''



    

if A!=0:
    if B==0 and C==0:
        print(first_word)
    else:
        print(first_word, 'and', second_word, third_word)
    
else: 
    print(first_word, second_word, third_word)







