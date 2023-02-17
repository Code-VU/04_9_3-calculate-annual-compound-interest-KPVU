def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    try:
        client_one_principal = float((input("Principle (amount): ")))
        client_one_time =      float((input("Time:               ")))
        client_one_rate =      float((input("Rate:               ")))
    except:
        print("Enter a valid amount for each.")
    Amount = float((client_one_principal)*(1+client_one_rate/100)**client_one_time)
    CompoundInterest = Amount - client_one_principal
    print("Compound Interest: {:.1f}".format(CompoundInterest))
    print("---")
    try:
        client_two_principal = float((input("Principle (amount): ")))
        client_two_time =      float((input("Time:               ")))
        client_two_rate =      float((input("Rate:               ")))
    except:
        print("Enter a valid amount for each.")
        exit()
    Amount = ((client_two_principal)*(1+client_two_rate/100)**client_two_time)
    CompoundInterestTwo = Amount - client_two_principal
    print("Compound Interest: {:.2f}".format(CompoundInterestTwo))
    print("---")
    try:
        client_thr_principal = float((input("Principle (amount): ")))
        client_thr_time =      float((input("Time:               ")))
        client_thr_rate =      float((input("Rate:               ")))
    except:
        print("Enter a valid amount for each.")
        exit()
    Amount = ((client_thr_principal)*(1 + client_thr_rate/100)**client_thr_time)
    CompoundInterestThr = Amount - client_thr_principal
    print("Compound Interest: {:.1f}".format(CompoundInterestThr))
 #print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
