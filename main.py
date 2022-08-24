# Auction Code by Alan Jaison for ThoughtMachine

#class for each auction items:
class Item:   #self, close_time, name, user_id, status, price_paid, total_bid_count, highest_bid, lowest_bid
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

    def enter_data(self, line):
        self.user_id = line[1]
        self.name = line[3]

    def display(self):
        print("Name:", self.name)
        print("user id:", self.user_id)

def test_method3(z):
    a = 20
    b = 21
    return 8


def update_object(auction_items,line):
    print("you are in update object function")
    print(line)


    #Check if the names match
    i = 0
    while i < len(auction_items):
        if auction_items[i].name == line[3]:
            #minimum price
            if auction_items[i].close_time >= line[0]:
                # Update the Second Highest Bid
                auction_items[i].price_paid = auction_items[i].highest_bid

                auction_items[i].highest_bid = line[4]
                print("Current object name " + auction_items[i].name)
                print("Current object Max Bid " + auction_items[i].highest_bid)

                # iterate bid count
                auction_items[i].total_bid_count += 1

                # Update the Lowest Bid
                if auction_items[i].total_bid_count == 1:
                    auction_items[i].lowest_bid = line[4]

        i += 1

    return 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Auction Code by Alan Jaison for, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    auction_items = []
    strip_line = []

    with open("Input.txt", "r") as param_file:
       # first_line = param_file.split("\n", 1)[0]
        new_list = []

        for line in param_file:
            strip_line = line.strip().split("|")
            new_list.append(strip_line)

        currentelement = []
      #  for i in range(len(new_list)):
      #      currentelement = new_list[i]
       #     if (currentelement[2] == 'SELL'):
      #          auction_items.append(Item(line=currentelement))

        print(strip_line[0])
        print(new_list[4])
        i = 0
       # for i in range(len(new_list)):
        while i < len(new_list):
            row = new_list[i]
            if (len(row) > 1):
                #Adding new items
                 if row[2] == 'SELL':
                     auction_items.append(
                         Item(line=new_list[i], highest_bid=0, status='Null', price_paid=0, total_bid_count=0, lowest_bid=0)
                     )
                     print("OBJECT CLOSE TIME " + auction_items[0].close_time)
                 elif row[2] == 'BID':
                     #Call object update function
                     update_object(auction_items, line=new_list[i])
            i = i + 1

        print("you are here")
        print(auction_items)
        for obj in auction_items:
            print(obj.name, obj.user_id, sep=' ')

        #Updating Object test and print objects
        #print("first object name " + auction_items[0].name)
        #auction_items[0].name = 'keyboard'

        print("first object name " + auction_items[0].name)
        print("First object max bid " + str(auction_items[0].highest_bid))

        print("Second object name " + auction_items[1].name)
        print("Second object max bid " + auction_items[1].highest_bid)

        #print("Second object name " + auction_items[1].name)
        #print("Second object name " + auction_items[1].name)

        #Final Statement
        z= 0
        while z < len(auction_items):

            if auction_items[z].price_paid >= auction_items[z].min_price:
                auction_items[z].status = 'SOLD'
            else:
                auction_items[z].status = 'UNSOLD'
                auction_items[z].price_paid = 0.00
                auction_items[z].user_id = ''

            print(auction_items[z].close_time, auction_items[z].name, auction_items[z].user_id,
                  auction_items[z].status, auction_items[z].price_paid, auction_items[z].total_bid_count,
                  auction_items[z].highest_bid, auction_items[z].lowest_bid, sep='|')
            z += 1

        #Actual object updating


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('ThoughtMachine')
