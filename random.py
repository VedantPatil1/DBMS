import inspect
class Dict2Class(object):
      
    def __init__(self, my_dict):
          
        for key in my_dict:
            setattr(self, key, my_dict[key])
  

my_dict = {"first_name":"TEXT",
           "last_name":"TEXT",
           "phone_number":"INTEGER",
           "email":"TEXT"}
    
result = Dict2Class(my_dict)

attributes = []

for i in inspect.getmembers(result):  
    # to remove private and protected
    # functions
    if not i[0].startswith('_'):
          
        # To remove other methods that
        # doesnot start with a underscore
        if not inspect.ismethod(i[1]): 
            attributes.append(i)
attributes.sort()
print (attributes)