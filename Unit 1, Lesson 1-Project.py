# 7 October 2026
# Unit 1, Lesson 1 Project

# Business details
business = "RSR Advisory"
budget = 1000 # Budget displayed in Pounds

# Start-up items
startupitems = ["web", "cards", "phone", "license", "campaigns"]
startupitems += ["insurance"] # Uses the += operator to add another item to the list
print(startupitems)

# Quantities
web = 1 # Web hosting packages
cards = 2 # Business card packs
phone = 1 # Business phone lines
license = 1 # Licences/qualifications
campaigns = 3 # Advertising campaigns
insurance = 1 # insurance

# Prices
webprice = 120 # Cost of web hosting
cardsprice = 15 # Cost per pack
phoneprice = 180 # Cost for line
licenseprice = 200 # Cost for license
campaignsprice = 100 # Cost per campaign
insuranceprice = 150 # Cost for insurance

# Calculate individual costs
webtotal = web * webprice # Total web hosting cost
cardstotal = cards * cardsprice # Total business card cost
phonetotal = phone * phoneprice # Total business phone line cost
licensetotal = license * licenseprice # Total license/qualification cost
campaignstotal = campaigns * campaignsprice # Total advertising campaign cost
insurancetotal = insurance * insuranceprice # Total insurance cost

# Calculate and display budget, start-up cost total and remaining
startuptotal = webtotal + cardstotal + phonetotal + licensetotal + campaignstotal + insurancetotal
remaining = budget - startuptotal
print("Budgeted Amount", budget)
print("Total start-up costs:", startuptotal)
print("Remaining:", remaining)

# Check item membership
if "phone" in startupitems:
    print("Phone is included in the start-up items")

# Check whether start-up costs are within budget
if startuptotal > budget:
    print("Start-up costs are over budget")
else:
    print("Start-up costs are within budget")