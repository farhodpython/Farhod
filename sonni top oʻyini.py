print("Keling sonni top oʻyinini oʻynaymiz!")
t=True 
while t:
    import random
    print("1 dan 10 gacha son oʻyladim. Topa olasizmi?")
    a=int(random.randint(1,10))
    n=int(input())
    s=0
    for i in range(1,11):
        if a==n:
            s+=1
            print(f"Topdingiz! siz {s} ta urinishda Topdingiz.")
            break 
        else:
            s+=1
            if n<a:print("Topa olmadingiz men oʻylagan son bundan katta");n=int(input())
            else:print("Topa olmadingiz men oʻylagan son bundan kichik"); n=int(input())
    y=0
    m=str(input("Endi siz 1 dan 10 gacha son oʻylang men topaman. "))
    k=random.randint(1,10)
    for i in range(1,11):
                print(k)
                n=str(input("Topgan boʻlsam (t), agar katta boʻlsa(+), kichik boʻlsa(-): "))
                if n=='t':
                    y+=1
                    break
                elif n=='-':
                    y+=1
                    k=random.randint(1,k-1)
                else:
                    y+=1
                    k=random.randint(k+1,10)
    if s==y:print(f"Durrang siz ham {s} ta urinishda. Men ham {y} ta urinishda topdik.")
    elif s>y:print(f"Siz {s} ta urishda topdningiz. Men esa {y} urinishda. Men yutdim!!")
    else:print(f"Siz {s} ta urishda topdningiz. Men esa {y} urinishda. Siz yutdingiz!! TABRIKLAYMAN!!!")
    n=input("Yana oʻynaysizmi (1-ha/yoq-0) ")
    if n=='0': t=False
if t==False:print("Bizning oʻynimizda oʻynaganingiz uchun raxmat!! Tuzuvchi: Ergashov Farhod")
