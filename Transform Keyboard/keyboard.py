
def h_transform(kb):
    for lst in kb:
        lst.reverse()
    return kb

def v_transform(kb):
    kb.reverse()
    return kb

def shift(num, kb):
    st = ""

    for lst in kb:
        st = st + ''.join(lst)
    
    ans = ""
    if num > 0:
        ans = st[:-num]
        ans = st[-num:] + ans
    else:
        ans = st[abs(num):]
        ans = ans + st[:abs(num)]
    
    print(ans)
    final = []
    for x in range(4):
        final.append(list(ans[:10]))
        if x != 3:
            ans = ans[10:]
    
    print(final)
    return final
        
if __name__ == '__main__':
    keyboard = {str(x):'0'+str(x-1) for x in range(1, 10)} | {'0':'09'} | {x:'1'+str(i) for i, x in enumerate('qwertyuiop')} | {x:'2'+str(i) for i, x in enumerate('asdfghjkl;')} | {x:'3'+str(i) for i, x in enumerate('zxcvbnm,./')}
    
    kb = [[str(x) for x in range(1, 10)] + ['0'],
            list('qwertyuiop'),
            list('asdfghjkl;'),
            list('zxcvbnm,./')]

    print("Enter 1st line input")
    first = input().split(',')

    print("Enter 2nd line input")
    second = input()

    for x in first:
        if x.isalpha():
            if x == 'H':
                kb = h_transform(kb)
            else:
                kb = v_transform(kb)
        else:
            kb = shift(int(x), kb)
    
    output = ""
    for x in second:
        if x in keyboard.keys():
            ind = keyboard[x]
            output += kb[int(ind[0])][int(ind[1])]
        else:
            output += x

    print("Final Output string: ",output)

        


