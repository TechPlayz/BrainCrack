vars = {}
lines = []

with open("./Samples/helloworld.bc",'r') as f:
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


