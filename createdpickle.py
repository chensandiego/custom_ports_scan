import pickle
pickle_file=open("port_description.dat","wb")
file_name=input("Enter the file name")
f=open(file_name,"r")
dict1={}

for line in f:
    key,value=line.split(':',1)
    dict1[int(key.strip())]=value.strip()

print ("Dictionary is created")

pickle.dump(dict1,pickle_file)
pickle_file.close()
print ("port_description.dat is created")
