logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bidders = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    lucky = ("nobody", 0)
    for bidders_name, bidders_bid in bidding_record.items():
        if bidders_bid > highest_bid:
            lucky = (bidders_name, bidders_bid)
            highest_bid = bidders_bid
        else:
            continue
    return lucky


while not bidding_finished:
    name = input('What is you name? ')
    price = int(input('What is you bid? $'))
    bidders[name] = price

    should_continue = input('Are there any other bidders? Type "yes" of "no". \n')
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        continue
    else:
        print("Invalid name!")

winner = find_highest_bidder(bidders)
print(f'Winner is {winner[0]} {winner[1]}')