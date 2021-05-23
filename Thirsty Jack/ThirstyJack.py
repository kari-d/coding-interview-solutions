import math

def get_output1(litres, temp, res=[]):
    bottles = math.ceil(litres/temp[0])
    if not res:
        res.append({temp[0]: bottles})
    else:
        #print("res: ", res)
        key = list(res[-1].keys())[-1]
        res.append({key: res[-1][key] - 1, temp[0]: bottles})
    if (temp[0] * bottles > litres):
        get_output1(litres - temp[0], temp[1:], res)
    #print(res)
    return res
    

if __name__ == '__main__':
    print('n = no. of types of bottles and L = required amt of water in liters')
    firstLine = input('Enter two integers n and L: ').split()
    total_litres = int(firstLine[1])

    secondLine = input(f'Enter cost of {firstLine[0]} bottles separated by space: ').split()
    cost = [int(x) for x in secondLine]

    cap = [2 ** idx for idx in range(int(firstLine[0]))]

    temp = {ent[1]:ent[0]/(ent[1] if ent[1] else 1) for ent in zip(cost, cap)}
    temp = [key for key, val in sorted(temp.items(), key=lambda x: x[1])]

    litres = total_litres

    result = get_output1(total_litres, temp)

    amt = [0] * len(result)

    for i, items in enumerate(result):
        for key, value in items.items():
            idx = cap.index(key)
            amt[i] = amt[i] + value * cost[idx]
    
    op2 = min(amt)
    op1 = result[amt.index(op2)]


    # print ("cost: ", cost)
    # print ("capacity: ", cap)
    # print ("temp: ", temp)
    print(','.join([str(key)+':'+str(value) for key, value in op1.items()]))
    print(op2)


