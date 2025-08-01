import art

print(art.logo)
bid_dict = {}
# TODO-1: Ask the user for input
again = "y"
while again.lower() == "y":

    print("Welcome to Silent biding\n")

    name = input("What's your name: ")
    bid = float(input("What's your bid: "))
# Save data into dictionary {name: price}
    bid_dict[name] = bid
# Whether if new bids need to be added
    again = input(" Do you want add another bidder Y/N: ")
    print("\n" * 20)

# Compare bids in dictionary
highest_bid = -1
bidder_name = ""
for bidder in bid_dict:
    bidder_bid = bid_dict[bidder]
    if  bidder_bid > highest_bid:
        highest_bid = bidder_bid
        bidder_name = bidder
print(f"Congratulations \n Winner is {bidder_name} with bidding ${highest_bid}")
print("Thank you and see again in another Silent bidding")

