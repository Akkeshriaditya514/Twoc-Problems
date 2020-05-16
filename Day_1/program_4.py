cp = float(input("Enter the cost price of the product: "))
sp = float(input("Enter the selling price of the product: "))
profit = sp - cp #if cp>sp then negative sign shows the loss in product
newPriceforsell = 1.05 * profit + cp
print("Profit from the sell is", profit)
print("To get profit 5% extra then new selling price is", newPriceforsell)