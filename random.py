columns = {"first_name":"TEXT",
           "last_name":"TEXT",
           "Phone_number":"INTEGER",
           "email":"TEXT"}
i=0
for item in columns:
    i=i+1
    columns[item]= i

print (columns["first_name"])