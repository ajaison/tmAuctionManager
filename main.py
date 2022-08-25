# Auction Code by Alan Jaison for ThoughtMachine

# class for each auction items:
class Item:
    def __init__(self, line, highest_bid, status, price_paid, total_bid_count, lowest_bid):
        self.name = line[3]
        self.min_price = line[4]
        self.close_time = line[5]

        self.user_id = line[1]
        self.status = status
        self.price_paid = price_paid
        self.total_bid_count = total_bid_count
        self.highest_bid = highest_bid
        self.lowest_bid = lowest_bid


def update_auction_item(auction_items,line):
    # Loop through items and check if the names match
    i = 0
    while i < len(auction_items):
        if auction_items[i].name == line[3]:
            # Updating minimum price
            if auction_items[i].close_time >= line[0]:
                # Updating the Second Highest Bid
                auction_items[i].price_paid = auction_items[i].highest_bid
                # Updating the Highest Bid
                auction_items[i].highest_bid = line[4]

                # iterate bid count
                auction_items[i].total_bid_count += 1

                # Update the Lowest Bid
                if auction_items[i].total_bid_count == 1:
                    auction_items[i].lowest_bid = line[4]
        i += 1
    return


def process_auction():
    auction_items = []
    # Process text file
    with open("Input.txt", "r") as param_file:
        new_list = []

        for line in param_file:
            strip_line = line.strip().split("|")
            new_list.append(strip_line)

        # Adding new items and updating items based on if it's a sell or buy
        i = 0
        while i < len(new_list):
            row = new_list[i]
            if len(row) > 1:
                # Adding new items
                if row[2] == 'SELL':
                    auction_items.append(
                        Item(line=new_list[i], highest_bid=0, status='Null', price_paid=0, total_bid_count=0,
                             lowest_bid=0)
                    )
                elif row[2] == 'BID':
                    # Call object update function
                    update_auction_item(auction_items, line=new_list[i])
            i = i + 1

        # Final Statement
        z = 0
        while z < len(auction_items):

            if float(auction_items[z].price_paid) >= float(auction_items[z].min_price):
                auction_items[z].status = 'SOLD'
            else:
                auction_items[z].status = 'UNSOLD'
                auction_items[z].price_paid = 0.00
                auction_items[z].user_id = ''

            print(auction_items[z].close_time, auction_items[z].name, auction_items[z].user_id,
                  auction_items[z].status, auction_items[z].price_paid, auction_items[z].total_bid_count,
                  auction_items[z].highest_bid, auction_items[z].lowest_bid, sep='|')
            z += 1


# Main
if __name__ == '__main__':
    process_auction()


