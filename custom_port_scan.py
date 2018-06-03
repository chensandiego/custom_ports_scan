from threading import Thread

import time
import socket

from datetime import datetime
import cPickle

'''use existed port service'''
pickle_file=open("port_description.dat",'r')
data=skill=cPickle.load(pickle_file)



def scantcp(r1,r2,):
    try:
        for port in range(r1,r2):
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(c)
            result=sock.connect_ex((rmip,port))
            if result ==0:
                print("port open:-->\t",port,"--",data.get(port," not in database"))
            sock.close()
    except Exception as e:
        print(e)

print "*"*60
print (" \tWelcome, this is the port scanner\n")
d=input("\tPress D for Domain Name or press I for ip address\t")

if (d=='D' or d=='d'):
    rmserver=input("\t Enter the domain name to scan:\t")
    rmip=socket.gethostbyname(rmserver)
elif(d=='I' or d=='i'):
    rmip=input("\t Enter the ip address to scan:\t")
else:
    print ("Wrong input")


port_start1 = int(input("\t Enter the start port number\t"))
port_last1 = int(input("\t Enter the last port number\t"))
if port_last1>65535:
  print ("Range not Ok")
  port_last1 = 65535
  print ("Setting last port 65535")
conect=input("For low connectivity press L and High connectivity Press H\t")

if (conect=='L' or conect=='l'):
    c =1.5

elif(conect =='H' or conect=='h'):
    c=0.5

else:
    print ("\twrong Input")


print ("\n Chen's port Scanner is working on ",rmip)
print ("*"*60)
t1= datetime.now()
total_ports=port_last1-port_start1

ports_by_one_thread =30


                   # tn number of port handled by one thread
total_threads=total_ports/ports_by_one_thread # tnum number of threads
if (total_ports%ports_by_one_thread!= 0):
    total_threads= total_threads+1

if (total_threads > 300):
    ports_by_one_thread= total_ports/300
    if (total_ports%300 !=0):
        ports_by_one_thread= ports_by_one_thread+1

    total_threads = total_ports/ports_by_one_thread
    if (total_ports%total_threads != 0):
        total_threads= total_threads+1

threads=[]
start1=port_start1
try:
    for i in range(total_threads):
        last1=start1+ports_by_one_thread
        #thread=str(i)
        if last1>port_last1:
            last1=port_last1
        port_thread=Thread(target=scantcp,args=(start1,last1,))
        port_thread.start()
        threads.append(port_thread)
        start1=last1
except Exception as e:
    print (e)

for t in threads:
    t.join()
print ("Exiting main thread")
t2=datatime.now()
total=t2-t1
print ("Scanning complete in ", total)
