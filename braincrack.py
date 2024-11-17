vars = {}
lines = []

with open("./Samples/arithmetic.bc",'r') as f: #Enter your desired file name
    for line in f:
        if line != '\n':
            lines.append(line.strip())

for line in lines:
    token = line.split()
    y = ' '.join(token[1::]) #for handling multiword strings

    #output 
    if token[0] == 'yap':
        if ((y.startswith('"') and y.endswith('"')) or (y.startswith("'") and y.endswith("'")) or y.isdigit()):
                if y.isdigit():
                    if ((y.startswith('"') and y.endswith('"')) or (y.startswith("'") and y.endswith("'"))):
                        print(y[1:-1], sep = " " ,end="\n")
                    else:
                        print(y, sep = " " ,end="\n")
                else:
                    print(y[1:-1], sep = " " ,end="\n")
        else: 
            for x in token[1:]:
                if x in vars.keys():
                    print(vars[x], sep = " " ,end="\n")
                    break
                else:
                    print("\nError Bruhhhh: Undefined Variable: %s\nig you forgot quotes buddy"%(x))
                    exit()
                    break

    #variable declaration
    elif token[0] == 'put':
        if token[2].isdigit():
            vars[token[1]] = int(token[2])
        else:
            vars[token[1]] = str(token[2])

    #Addition
    elif token[0] == 'stick':
        addList = []
        for x in token[1::]:
            if ((not(x.isdigit())) and x in vars.keys()):
                addList.append(vars[x])
            elif x.isdigit():
                addList.append(int(x))
            else:
                print(f"Variable {x} is undefined bruhhh")
                exit()
        print(sum(addList))
