print('Hello World')


#madLib:
print("type a noun")
noun = input()

print("type a verb with an -ing ending")
verb = input()

print("the " + noun + "is " + verb)


#level up:
my_list = []

print("type a noun:")
noun = input()
my_list.append(noun)

print("type a verb:")
verb = input()
my_list.append(verb)

print("type a adjective:")
adjective = input()
my_list.append(adjective)

print(my_list)
print(my_list(0))
print(my_list(1))
print(my_list(2))


print("the " + adjective + " " + noun + " " + "was " + verb)
#below does not work :( 
# print("the " + my_list(2) + my_list(0) + "was " + my_list(1))