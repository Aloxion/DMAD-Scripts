H = [89, None, None, None, 23, 45 , 11]
key = 73

#used for both linear and double hashing
def hash_one():
    return (key+2)%7

#used only for double hashing
def hash_two():
    return (key%6)+1

def linear_hash():
    H_copy = H
    i = 0
    while(True):
        if H_copy[(hash_one()+i)%len(H)] == None:
            H_copy[(hash_one()+i)%len(H)] = key
            print(H_copy)
            break
        i+=1
        if i == len(H_copy):
            print("no linear solution")
            break

def double_hash():
    H_copy = H
    i = 0
    while(True):
        if H_copy[(hash_one()+(i*hash_two()))%len(H)] == None:
            H_copy[(hash_one()+(i*hash_two()))%len(H)] = key
            print(H_copy)
            break
        i+=1
        if i == len(H_copy):
            print("no double solution")
            break


def main():
    type = input("Input 1 for linear, 2 for double: ")
    if type == "1":
        print("Linear hash:")
        linear_hash()
    elif type == "2":
        print("Double hash")
        double_hash()
    else:
        print("Not a valid input buddy")


if __name__ == "__main__":
    main()