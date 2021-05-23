
# def get_sequence(st):
    
#     char = list(st)
#     lst = []
#     count = 0
#     idx = 1
    
#     while  idx < len(st):
#         if ord(char[idx]) - ord(char[idx-1]) == 1:
#             if idx == len(st)-1:
#                 lst.append(char[idx]+"$1")
#             count += 1
#             if count > 1 and count < 3:
#                 lst.append('-')
#             elif count > 1:
#                 lst.append(char[idx-1]+"$1")
#                 idx -= 1
#                 count = 0
#             else:
#                 lst.append(char[idx])
#         idx += 1
    
#     return ''.join(lst)

def get_sequence(st):
    char = list(st)
    # char.append(" ")
    # count = 0
    # idx = 0

    diff = []
    for i in range(len(char) - 1):
        diff.append(abs(ord(char[i]) - ord(char[i+1])))
    
    diff.append(None)
    print(diff)
    seq = char[0]
    res = []
    for i in range(len(diff) - 1):
        if (diff[i] == diff[i+1]):
            seq = seq + char[i+1]
            print("in: ", seq)
            continue
        else:
            if diff[i+1] == None:
                seq = seq + char[i+1]

            if len(seq) > 2:
                res.append(seq[0]+"-"+char[i+1]+"$"+str(diff[i]))
            else:
                res.append(seq+char[i+1])
            print(seq)
            seq = ""
    
    if seq:
        #print("if")
        res.append(seq[0]+"-"+seq[-1]+"$"+str(diff[i]))

    # for _ in st:
    #         if abs(ord(char[idx]) - ord(char[idx+1])) == 1:
    #             count = 1
    #             idx += 1
    #             print(idx)
    #             continue
    #         elif count:
    #             lst.append("-"+char[idx]+"$1")
    #             idx += 1
    #             print(lst)
    #         else:
    #             lst.append(char[idx+1])
    #             idx += 1

    #print(res)
    return ''.join(res)
            
            

if __name__ == '__main__':
    st = input('Enter sequence: ')

    print(get_sequence(st))