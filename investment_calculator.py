investment = float(raw_input("What is your initial investment? $"))
irate = (float(raw_input("What is the assumed interest rate? Write as a percent but do not include the percent sign."))) / 100
anual = float(raw_input("How much will you be adding anually? $"))
years = int(raw_input("How many years will you let this investment grow?"))

initinvest = investment

for i in range(years):
    investment += anual
    investment += ((investment * irate) * .85)
    
print "\nAfter %d years you will have $%s after taxes, of which $%s will be pure interest." % (years, str(round(investment, 2)), str(round((investment - (anual * years) - initinvest), 2)))

investment = initinvest
mil_count = 0

while investment < 1000000:
    investment += anual
    investment += ((investment * irate) * .85)
    mil_count += 1

investment = initinvest
year_count = 0

while (investment - (anual * year_count) - initinvest) < (investment - (investment - (anual * year_count) - initinvest)):
    investment += anual
    investment += ((investment * irate) * .85)
    year_count += 1

print "At that rate it will take %d years of growth to make more in interest than you'll have paid in so far at that time, and it will take %d years for you to be a millionaire." % (year_count, mil_count)
