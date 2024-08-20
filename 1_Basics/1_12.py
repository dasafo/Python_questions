# Calculate income tax for the given income by adhering to the rules below:
#
# Taxable Income	Rate (in %)
# First $10,000         0
# Next $10,000          10
# The remaining         20
#
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

income = 45000

tax_playable = 0

if income <= 10000:
    tax_playable = 0

elif income <= 20000:
    tax_playable = (income - 10000) *10/100

else:

    tax_playable = (10000*10/100) + (income - 20000) * 20/100

print("You have to pay: ", tax_playable)
