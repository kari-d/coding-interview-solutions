#Check if the brackets are balanced or unbalanced

st = "{ ( [ ] ) } }"

arr = st.split()
stack = []

switcher = {
    "{": "}",
    "(":")",
    "[":"]"
}
op = "Balanced"
for x in arr:
    if x in ["{", "(", "["]:
        stack.append(x)

    if x in ["}", ")", "]"]:
        temp = switcher.get(stack[-1], "")
        
        if temp == x:
            stack.pop()
        else:
            op = "Unbalanced"
            break

print(op)