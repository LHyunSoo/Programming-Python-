for i in range(2,10):
    if i > 7:
        break
    else:
        print("----",i,"단","----")
        for j in range(1,10):
            if j % 2 == 0:
                continue
            else:
                print (i," x ",j," = ",i*j)
    print("--------------")