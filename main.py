# Auction Code by Alan Jaison for ThoughtMachine
def test_method3(z):
    a = 20
    b = 21
    return 8

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Auction Code by Alan Jaison for, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    #f = open("input.txt", "r")

    #print(f.read())
    strip_line = []
    with open("Input.txt", "r") as param_file:
       # first_line = param_file.split("\n", 1)[0]
        new_list = []
        for line in param_file:
            strip_line = line.strip().split("|")
            new_list.append(strip_line)

        print(strip_line[0])
        print(new_list[0])

        if (new_list[0][2] == 'SELL'):
            #here create a new object
            print('print statement')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('ThoughtMachine')
