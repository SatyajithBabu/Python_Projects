import json
class users:
    def __init__(self):
        self.todos=[]
        self.n=0
        with open("E:/progs/main/To_Do/To_Do.json",'r') as f:
            self.todos=json.load(f)

    #Adds new record    
    def add(self,name="Nill",desc="None",done="No"):
        for i in self.todos:
            if i["Name"]==name:
                print("Name Exists")
                return
        self.todos.append({"Name":name,"Desc":desc,"Done":done})
        self.apply()

    #Modifys available record
    def modify(self,name,done="No"):
        for i in range(len(self.todos)):
            if self.todos[i]["Name"]==name:
                self.todos[i]["Done"]=done
        self.apply()

    #applys changes
    def apply(self):
        with open("E:/progs/main/To_Do/To_Do.json","w") as f:
            json.dump(self.todos,f,indent=4)

    #displays records
    def display(self):
        self.n=0
        for i in [a for a in self.todos]:
            self.n+=1
            print(self.n)
            for j in i:
                print(f"    {j} : {i[j]}")

    #deletes records
    def delete(self, name):
        self.todos = [todo for todo in self.todos if todo["Name"] != name]
        self.apply()


def menu(i):
    if i==1:
        obj.display()
    elif i==2:
        obj.add(input("Name : "),input("Description : "),input("Done?"))
    elif i==3:
        obj.modify(input("Enter name : "),done=input("Done? : "))
    elif i==4:
        obj.delete(input("Enter name to be deleted : "))
    elif i>5 and i<0:
        print("enter valid value")


obj=users()
choice=0
while choice>=0:
    print("\t\tMENU\n1.Display\n2.Add\n3.modify\n4.Delete\n5.EXIT")
    try:
        choice=int(input("Enter your choice : "))
    except ValueError:
        print("enter valid value")
    menu(choice)