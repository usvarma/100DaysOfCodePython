import art

bidders = {}


def calculate_highest_bidder():
    more_bidders = True
    while more_bidders:
        name = input("Enter the bidder's name: ")
        bid_value = float(input(f"Enter the bid value for {name}: "))
        bidders[name] = bid_value
        bidders_left = input("Do you want to add more bids? Type 'yes' to add more or 'no' to stop.").lower()
        if bidders_left != 'yes':
            more_bidders = False

    name_of_top_bid = ''
    top_bid_value = 0

    for name in bidders:
        current_bid = bidders[name]
        if current_bid > top_bid_value:
            name_of_top_bid = name
            top_bid_value = current_bid

    print(f"The winner of the bid is {name_of_top_bid} and the winning bid value is {top_bid_value}")


if __name__ == '__main__':
    print(art.logo)
    calculate_highest_bidder()
