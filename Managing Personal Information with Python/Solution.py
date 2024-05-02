import pickle

Address_book =dict()
secret_person_list=[]
class info:
  def __init__(self,name,dob):
    self.name= name
    self.dob = dob

  def save():
    N=int(input("Enter the no. of data: "))
    for i in range(N):
      name=input("Enter name: ")
      dob=input("Enter dob: ")
      secret=input("Is your dob to be secret(y/n): ")
      Address_book[name]=(dob)
      if secret.lower()=='y':
        secret_person_list.append(name)
    with open('data.pickle','wb') as f:
      pickle.dump(Address_book,f)
    print("Name added succesfully")

  def retrieve():
    print('Retrieve dob')
    name=input("Enter name: ")
    if name in Address_book:
      if name in secret_person_list:
        print("Secret")
      else:
        print(f"The dob is {Address_book[name]}")
    else:
      print("No entry of this name.")



info.save()
info.retrieve()
