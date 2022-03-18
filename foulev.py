# Python program to evaluate whether to foul a shooter
# define variables
shotpercentage = int(input("Enter the percentage chance of the shooter making the shot without being fouled: "))
shotpercentageiffouled = int(input("Enter the percentage chance of the shooter making the shot with being fouled: "))
freethrowpercentage = int(input("Enter the free throw percentage of the shooter: "))

nofoulEV = float(shotpercentage*2/100)
print("The EV of not fouling is %.2f" % nofoulEV);
foulEV = float((shotpercentageiffouled*2/100)+shotpercentageiffouled/100*freethrowpercentage/100)+2*(((1-shotpercentageiffouled/100)*freethrowpercentage/100))
print("The EV of fouling is %.2f" % foulEV);
gain= round(float(nofoulEV-foulEV),2)
print("With these percentages you gain", gain, "points by fouling");