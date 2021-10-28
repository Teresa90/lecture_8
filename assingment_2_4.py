#define input
#define the input
#define the relation/operations
#result=num
#result=result*num
#15*15*15*15
#result=result*15=(15*15=225)0
#result=result*15=(225*15=3375)1
#result=result*15=(3375*15=50625)2


def main():#we define the function
    num=int(input("enter a whole number"))#15
    exponent=int(input("enter exponent number"))#3

    result=num

#we use the aspect of for loop to in range
    for i in range(3):
        result=result*num


        print (result)


main()





