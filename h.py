l=[]
while True:
    c=int(input('''
    1 Push Elements
    2 Pop Elements
    3 Peak Elements
    4 Display stack
    5 Exit


    '''))
    if c==1:
        n=input("Enter The Value -: ");
        l.append(n);
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
         else:
           p=l.pop()
           print(p)
    elif c==3:
        if len(l)==0:
            print("Empty Stack");
        else:
            print("last stack",l[-1]);
    elif c==4:
        print("Display Stack")
            
                






        
        
