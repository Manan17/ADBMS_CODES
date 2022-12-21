from BTrees._IIBTree import IIBTree
import time
insertion_start_time = time.time()
tree = IIBTree()

for i in range(3000):
    tree.update({i:i*2})
insertion_end_time = time.time()
print("You insertion time: ",format((insertion_end_time - insertion_start_time)*1000,".3f"))

key = int(input("Enter key to search: "))
search_start_time = time.time()
if tree.has_key(key):
    print(tree[key])

search_end_time = time.time()
print("Your searching time: ",format((search_end_time - search_start_time)*1000,".3f"))