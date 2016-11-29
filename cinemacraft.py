

import sys
global denominations
amount = 4
denominations =[2,3,5]
#
# O(n*m)
def solve(denominataions,amount):
    countOfNotes = 0
    notesChosen =[]
    for index,note in enumerate(denominataions[::-1]):
        if amount>0:
            nNotes = amount/note
            countOfNotes +=nNotes
            notesChosen.append([note,nNotes,index])
            amount %=note
    # print amount
    # print notesChosen
    if amount!=0:
        while 1:
            if len(notesChosen)==0 and len(denominations)==0:
                return [-1,-1]
            elif len(notesChosen)==0 and len(denominations)>1:
                denominations.pop()
            print denominations
            print notesChosen
            if notesChosen[-1][1] >= 1:
                notesChosen[-1][1] -=1
                amount +=notesChosen[-1][0]
                # print len(denominations)-notesChosen[-1][2]
                # sys.exit()
                nextDenominations= denominations[:len(denominations)-notesChosen[-1][2]-1]
                # print nextDenominations
                # print amount
                # print notesChosen
                return solve(nextDenominations,amount)

            else:
                notesChosen.pop()
    else:
        return [countOfNotes, notesChosen]



for i in xrange(1,15):
    count, notes = solve(denominations, 9)
    #print count
    print "amount: ",i,
    print notes
    sys.exit()

# if result[0]==-1:
#     print "not possible"
# else:
#     print "number: ",result[0]
#     print "denominations: ",result[1]













#
# def solve(amount,denominations):
#     moneyTable = []
#     moneyTable.append([0]*(amount+1))
#     for indexRow,row in enumerate(denominations):
#         for amountRow in xrange(1,amount+1):






