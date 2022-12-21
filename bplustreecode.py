from bplustree import BPlusTree
import time

insertion_start_time = time.time()

tree = BPlusTree("tmp/bplustree.db",order=50)
for i in range(2000):
    tree[i] = (i*2).to_bytes(10,'big')

insertion_end_time = time.time()
print("You insertion time: ",format((insertion_end_time - insertion_start_time)*1000,".3f"))
data = int(input("Enter key: "))
start_time = time.time()
byte_data = tree.get(data)
end_time = time.time()
int_data = int.from_bytes(byte_data,'big')
print("Value: ", int_data)
print("Time: ", (end_time-start_time)*1000, "ms")