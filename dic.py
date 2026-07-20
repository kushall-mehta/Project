d1 = {
    "name ": "John",
    "age": 30,  
    "city": "New York",
    "clg_cgpa":[9,8,7,8,]
}
print(d1)
print(type(d1)) 
print(d1.keys())          
d1["clg_name"] = "ABC University"  # Adding a new key-value pair
print(d1)
d1.pop("age")  # Removing a key-value pair
print(d1)
d1.clear()  # Clearing the dictionary
print(d1)  # Should print an empty dictionary   


d2 ={ 
     'ch1':{    "name": "Alice",
    "age": 25,
     },
        'ch2':{    "name": "Bob",   
    },
        'ch3':{    "name": "Charlie",
    "age": 22,
        }
     
    }
print(d2['ch1'])
    