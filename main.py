# Auction Code by Alan Jaison for ThoughtMachine

#class for each auction items:
class Item:   #self, close_time, name, user_id, status, price_paid, total_bid_count, highest_bid, lowest_bid
    def __init__(self, line):
        self.name = line[3]
        self.min_price = line[4]
        self.close_time = line[5]

        self.user_id = line[1]
        #self.status = status
        # self.price_paid = price_paid
        # self.total_bid_count = total_bid_count
        # self.highest_bid = highest_bid
        # self.lowest_bid = lowest_bid

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
                 if ((row[2] == 'SELL')):
                     auction_items.append(Item(line=new_list[i]))
            i = i + 1
            #here create a new object
        #    print('print statement')
#test
        #info = Item()
        #auction_items.append(Item(line=new_list[0]))
        #uction_items.append(Item(line=new_list[3]))
        #  print(info.name)
        #  print(info.user_id)


        print("you are here")
        print(auction_items)
        for obj in auction_items:
            print(obj.name, obj.user_id, sep=' ')

        #Updating Object
        print("first object name " + auction_items[0].name)
        auction_items[0].name = 'keyboard'
        print("first object name " + auction_items[0].name)


        # p1 = Item(user_id=new_list[0][1], name=new_list[0][3])

        # print(p1.user_id)
        #  print(p1.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('ThoughtMachine')
