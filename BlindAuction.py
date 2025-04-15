# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
auction_details = {}
new_bid = True

def highest_bidder(auction_info):
    max_bid = 0
    winner = ''
    for bidder in auction_info:
        if auction_info[bidder] > max_bid:
            max_bid = auction_details[bidder]
            winner = bidder
    print(f'The winner is {winner} with a bid of ${max_bid}')

while new_bid == True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_details[name] = bid
    want_new_bid = input("Is there anyone else want to bid: yes/no?")
    print('\n' * 270)
    if want_new_bid.lower() == "no":
        new_bid = False
        highest_bidder(auction_details)
