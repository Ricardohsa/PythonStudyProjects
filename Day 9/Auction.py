import arts

print(arts.logo)
end_of_auction = False
auctions = {}
bid = 0
highest_bid = 0
name = ""

def check_winner(bidding_record):
    """ Take a dictionay of auction and returns the highest or winner of the auction.

    Args:
        bidding_record (_type_): _description_
    """
    highest_bid = 0
    for auctionkey in auctions:
        bind_amount = auctions[auctionkey]
            
        if (bind_amount > highest_bid):
            highest_bid = bind_amount
            name = auctionkey           
            
    print(f"The winner is: {name} with a bid of ${highest_bid}")
    
        

while not end_of_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    
    auctions[name] = bid 
            
    bidders = input("Are there any other bidders? Type 'yes or 'no'. ")
    
    if bidders == 'no':
        end_of_auction = True
    
        check_winner(auctions)
    




