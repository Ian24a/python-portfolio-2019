# Ian Christensen
#9/19
#Cash Register Activity













#Declare and Initialize Variables
num_items= 100
cost_per_item= 3.99
tax_rate= 0.09

#Calculate and store the sub-total
sub_total= num_items* cost_per_item


#calcuate the ammount of tax and store as a result
tax_ammount= sub_total * tax_rate

#calculate the total price and store the amount
total_price= sub_total + tax_ammount

#show the full receipt to the screen

print("------Reciept------")
print("number of items   :"+str(num_items))
print("Cost per item     :$"+str(cost_per_item))
print("Tax Rate          :"+str(tax_rate))
print("Tax Ammount       :$"+str(tax_ammount))
print("Total             :$"+str(total_price))

input("Press enter to exit")
