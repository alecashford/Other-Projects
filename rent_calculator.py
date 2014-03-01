print "Input the ammounts for each prompt. Do not include the dollar sign.\n"
rent = float(raw_input("How much was the rent this month? $"))
gas = float(raw_input("How much was the gas bill this month? $"))
electric = float(raw_input("How much was the electricity bill this month? $"))
water = float(raw_input("How much was the water bill this month? $"))
internet = float(raw_input("How much was the Comcast bill this month?"))
garbage = float(raw_input("How much was the garbage bill this month? $"))

equalshare = round(float(((rent + gas + electric + water + internet + garbage) / 4)), 2)

print "\nSplit equally, everybody's share of rent and utilities for this month is would be $%s. Let's correct that number to account for how much each person paid this month for communal items (e.g. detergent, paper towels, milk, etc.)" % str(round(float(((rent + gas + electric + water + internet + garbage) / 4)), 2))

class Renter:
    def __init__(self, name, moneyspent):
        self.name = name
        self.totalspent = totalspent
        self.moneyspent = moneyspent
        self.equalshare = equalshare
        self.moneyowed = (((totalspent - self.moneyspent) / 4) - (self.moneyspent * .75))
    
    def printdata(self):
        print "%s's grand total is $%s" % (self.name, str(round((equalshare + self.moneyowed), 2)))


aaronspent = float(raw_input("\nHow much did Aaron spend? $"))
alecspent = float(raw_input("How much did Alec spend? $"))
noamspent = float(raw_input("How much did Noam spend? $"))
philspent = float(raw_input("How much did Phil spend? $"))

totalspent = (aaronspent + alecspent + noamspent + philspent)

aaron = Renter("Aaron", aaronspent)
alec = Renter("Alec", alecspent)
noam = Renter("Noam", noamspent)
phil = Renter("Phil", philspent)
print "\n"
aaron.printdata()
alec.printdata()
noam.printdata()
phil.printdata()
