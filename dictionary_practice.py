#Module 6, Part 5: Practice with dictionaries here


my_phonebook={
    "Statue of Liberty":2125555555,
    "Ghostbusters":2125551234
    }
num = my_phonebook["Statue of Liberty"]
print(num)
my_phonebook["Ghostbusters"] = 2125559876
print(my_phonebook["Ghostbusters"])

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
###

###
#Print the variable, num
###

###
#Change the value of the Ghostbusters' phone number to 2125559876
###

#Here's an empty dictionary
your_phonebook={}
your_phonebook['hi'] = "hello"
your_phonebook['bye'] = "goodbye"
your_phonebook['Sup'] = "whats up"
your_phonebook['Cya'] = "Cya later aligator"
your_phonebook['key'] = "value"
print(your_phonebook.keys())
for i in range(5):
    keys = [your_phonebook.keys()]
    print(keys[0])


###
#Add 5 values to it like this
#your_phonebook['key']=value
###

###
#Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys

#Loop over this sequence with a for loop
#using syntax like

#for key in sequence_of_keys :
#    #Do stuff

#Use the loop to print to the shell the key and value
#of every element in the dictionary
###

