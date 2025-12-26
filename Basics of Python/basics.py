print("preparing for interview")
#basic of data types
a=10 #integer
b=20.5 #float
c="hello" #string
d=True #boolean
e=[1,2,3,4,5] #list
f=(1,2,3,4,5) #tuple
g={1:"one",2:"two",3:"three"} #dictionary
h={1,2,3,4,5} #set
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))


#difference between list , tuple , dictionary and set
print("List vs Tuple vs Dictionary vs Set")
print("List is mutable:", e)
print("Tuple is immutable:", f)
print("Dictionary is mutable:", g)
print("Set is mutable:", h)

print("set has no duplicate elements and is unordered")
print("Dictionary stores data in key-value pairs ")


print ("""Lists: Flexible but heavier in memory.

Tuples: Lightweight and fast, but you can’t modify them.

Dictionaries/Sets: Powerful but memory-hungry due to hashing.

Best practice: Use tuples when immutability is fine, lists for general sequences, dicts for mappings, and sets for uniqueness/membership checks.""")