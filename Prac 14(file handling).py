try:
    f=open('file1.txt','r')
    g=open('file2.txt','w')
    s=f.readline()
    g.write(s)
    count=0
    while(s!=''):
        s=f.readline()
        count+=1
        if count%2==0:
            g.write(s)

    f.close()
    g.close()
    g=open('file2.txt','r')
    s=g.readlines()
    print(s)
    g.close()
except NameError:
    print('Variable not defined')
except FileNotFoundError:
    print('File not found')
except:
    print('Something went wrong')
finally:
    f.close()
    g.close()
