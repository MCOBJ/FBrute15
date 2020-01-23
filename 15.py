import os
os.system("clear")
print """                                                    
                                                             
  ______   ____                   _            __   _____    
 |  ____| |  _ \                 | |          /_ | | ____|   
 | |__    | |_) |  _ __   _   _  | |_    ___   | | | |__     
 |  __|   |  _ <  | '__| | | | | | __|  / _ \  | | |___ \    
 | |      | |_) | | |    | |_| | | |_  |  __/  | |  ___) |   
 |_|      |____/  |_|     \__,_|  \__|  \___|  |_| |____/    
                                                             
                                                             
============================================================

Rename your wordlist to "wordlist0.txt" and place it in the FBrute15 directory


"""
continu=raw_input("Press any key to continue...")
os.system("rm -r pass")
os.system("mkdir pass")

g=0
m=0
while True:
    wordopn=open("./wordlist"+str(g)+".txt","r")
    lineas=wordopn.readlines()
    wordopn.close()

    n=0
    while True:
        os.system("echo "+str(lineas[n]).replace("\n","")+" >> ./pass/"+str(m)+".txt")
        if n>14:
            v=15
            e=0
            while True:
                try:
                    os.system("echo "+str(lineas[v]).replace("\n","")+" >> ./wordlist"+str(g+1)+".txt")
                    v=v+1
                except:
                    break
            m=m+1
            print "Division "+str(m)+" ready"
            break
        else:
            n=n+1
    g=g+1
