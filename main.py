import getpass
database={"aman":"168","rohit":"165"}
username=input("enter your username")
password=getpass.getpass("enter your password: ")
for i in database.keys():
   if username==i:
     while password!=database.get(i):
          password=getpass.getpass("enter your password again ")
     break
print("Verified")
