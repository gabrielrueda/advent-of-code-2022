class Monkey:
    def __init__(self, file) -> None:
        self.items = [int(i) for i in ((file.readline())[18:]).split(", ") ]
        self.oper = ((file.readline())[19:]).split(" ")

        if(self.oper[0][0] != 'o'): 
            self.oper[0] = int(self.oper[0])
        else:
            self.oper[0] = 'x'

        if(self.oper[2][0] != 'o'): 
            self.oper[2] = int(self.oper[2])
        else:
            self.oper[0] = 'x'

        self.div = int((file.readline())[21:])

        self.true_cond = int((file.readline())[29])
        self.false_cond = int((file.readline())[30])

        self.inspected = 0

from math import gcd
        
def completeOperation(num1, op, num2, old):
    if(type(num1) == str):
        num1 = old
    if(type(num2) == str):
        num2 = old
    
    if(op == "*"):
        return num1 * num2
    elif(op == "+"):
        return num1 + num2

file = open("data.txt", "r")

monkeys = []


for i in range(0,4):
    file.readline()
    monkeys.append(Monkey(file))
    file.readline()



for round in range(0, 10000):
    for monkey in monkeys:
        while(monkey.items):
            monkey.items[0] = completeOperation(monkey.oper[0], monkey.oper[1], monkey.oper[2], monkey.items[0])
            # monkey.items[0] = monkey.items[0] // 3
            tmp = monkey.items.pop(0)
            if(tmp % monkey.div == 0):
                monkeys[monkey.true_cond].items.append(tmp)
            else:
                monkeys[monkey.false_cond].items.append(tmp)
            monkey.inspected += 1

    if(round % 2 == 0):
        print(f"Round {round} complete.")


# res = [monkeys[0].inspected, monkeys[1].inspected]

# if(res[0] < res[1]): 
#     res[0], res[1] = res[1], res[0]
 
# for i in range(2, len(monkeys)):
#     if(monkeys[i].inspected > res[0]):
#         res[1] = res[0]
#         res[0] = monkeys[i].inspected
#     elif(monkeys[i].inspected > res[1]):
#         res[1] = monkeys[i].inspected

# print(f"The result is {res[0] * res[1]}")

file.close()
