#list and all its methods
a = [7, 2, 9, 10, 4, 3]

print("Original:", a)

a.append(5)          # Add at end
print("append the value of 5 :", a)

a.insert(1, 100)     # Insert at index 1
print("insert the value of 100 at index 1:", a)

a.extend([20, 30])   # Extend with another list
print("extend with [20, 30]:", a)

a.remove(9)          # Remove first occurrence of 9
print("remove the first occurrence of 9:", a)

print("pop the last element:", a.pop())   # Remove last element and return it
print("after pop:", a)

print("index of 10:", a.index(10))
print("the element of the list a :", a)  # Find index
print("count of 2:", a.count(2))    # Count occurrences

a.sort()             # Sort ascending
print("sort:", a)

a.reverse()          # Reverse order
print("reverse:", a)

b = a.copy()         # Copy list
print("copy:", b)

a.clear()            # Clear all elements
print("clear:", a)


#tuple and all its methods

t = (5, 2, 9, 1, 5, 3)
# Length of tuple
print("Length:", len(t))   # 6
# Largest and smallest element
print("Max:", max(t))      # 9
print("Min:", min(t))      # 1
# Sum of elements
print("Sum:", sum(t))      # 25
# Sorted tuple (returns a list, not a tuple)
print("Sorted:", sorted(t))   # [1, 2, 3, 5, 5, 9]
# Slicing (subset of tuple)
print("Slice [1:4]:", t[1:4])   # (2, 9, 1)
# Concatenation (joining tuples)
new_t = t + (100, 200)
print("Concatenation:", new_t)   # (5, 2, 9, 1, 5, 3, 100, 200)
# Repetition (repeat tuple elements)
print("Repetition:", t * 2)   # (5, 2, 9, 1, 5, 3, 5, 2, 9, 1, 5, 3)



#dictionary and all its methods
# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)
# 1. copy() → shallow copy
new_dict = my_dict.copy()
print("Shallow copy:", new_dict)
# 2. clear() → remove all items
my_dict.clear()
print("After clear():", my_dict)
# 4. get(key, default) → safe access
print(my_dict.get('a', 'Not Found'))

# 5. items() → key-value pairs
print(new_dict.items())

# 6. keys() → all keys
print(new_dict.keys())

# 7. values() → all values
print(new_dict.values())

# 8. pop(key) → remove key and return value
val = new_dict.pop('b')
print(val)

# 9. popitem() → remove last inserted pair
pair = new_dict.popitem()
print(pair)

# 10. setdefault(key, default) → return value or insert default
print(new_dict.setdefault('z', 100))

# 11. update(other_dict) → merge/update
new_dict.update({'a': 10, 'd': 40})
# 12. len() → number of items
print(len(new_dict))





#set and all its methods
# Create a set
my_set = {1, 2, 3}
another_set = {3, 4, 5}

# 1. add(x) → add element
my_set.add(10)

# 2. clear() → remove all elements
my_set.clear()

# 3. copy() → shallow copy
new_set = my_set.copy()

# 4. difference(other) → elements in set but not in other
print(my_set.difference(another_set))

# 5. difference_update(other) → remove common elements
my_set.difference_update(another_set)

# 6. discard(x) → remove element if present (no error)
my_set.discard(2)

# 7. intersection(other) → common elements
print(my_set.intersection(another_set))

# 8. intersection_update(other) → keep only common elements
my_set.intersection_update(another_set)

# 9. isdisjoint(other) → True if no common elements
print(my_set.isdisjoint(another_set))

# 10. issubset(other) → True if all elements in other
print(my_set.issubset(another_set))

# 11. issuperset(other) → True if contains all elements of other
print(my_set.issuperset(another_set))

# 12. pop() → remove and return random element
print(my_set.pop())

# 13. remove(x) → remove element (error if not found)
my_set.remove(3)

# 14. symmetric_difference(other) → elements in either but not both
print(my_set.symmetric_difference(another_set))

# 15. symmetric_difference_update(other) → update with symmetric difference
my_set.symmetric_difference_update(another_set)

# 16. union(other) → all elements from both sets
print(my_set.union(another_set))

# 17. update(other) → add elements from another set
my_set.update(another_set)
print("Final set:", my_set)






#common built-in functions for data types
print(
""" Function	   Works On	              Description	                         Example
len()	         all	              Number of elements	                   len([1,2,3]) → 3
max()	         list, tuple, set	  Largest element	                         max((5,2,9)) → 9
min()	         list, tuple, set	  Smallest element	                   min({5,2,9}) → 2
sum()	         list, tuple, set	  Sum of numeric elements	             sum([1,2,3]) → 6
sorted()	   all          	        Returns sorted list	                   sorted({3,1,2}) → [1,2,3]
any()	         all	              True if any element is truthy	       any([0,0,1]) → True
all()	         all	              True if all elements are truthy	       all([1,2,3]) → True
enumerate()	   list, tuple, set	  Get index + value pairs	             for i,v in enumerate(['a','b']): ...
zip()	         list, tuple	        Combine multiple iterables	             zip([1,2],[‘a’,‘b’]) → [(1,'a'),(2,'b')]
map()	         list, tuple, set	  Apply function to each element	       map(str, [1,2,3]) → ['1','2','3']
filter()	   list, tuple, set	  Filter elements by condition	       filter(lambda x:x>2,[1,2,3]) → [3]  """ )

