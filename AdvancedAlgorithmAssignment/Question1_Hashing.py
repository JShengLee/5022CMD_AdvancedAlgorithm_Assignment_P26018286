import time

class Inventory:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key.item_id)
        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is not None:
                if self.table[new_index].item_id == key.item_id:
                    print(f"\nThe item_id is currently in use.")
                    return

            if self.table[new_index] is None:
                self.table[new_index] = key
                array.append(key)
                return
        print(f"\nThe table is full.")
        return

    def search(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                break

            if self.table[new_index].item_id == key:
                print(f"\nitem_id: {key}"
                      f"\nitem_name: {self.table[new_index].name}"
                      f"\nitem_price: RM{self.table[new_index].price}"
                      f"\nitem_quantity: {self.table[new_index].quantity}")
                return
        print(f"\nThe item ({key}) you are searching for does not exist")
        return

    def searchTime(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                break

            if self.table[new_index].item_id == key:
                return self.table[new_index]
        return
    def delete(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                break

            if self.table[new_index].item_id == key:
                self.table[new_index] = None

                for item in array:
                    if item.item_id == key:
                        array.remove(item)
                        print(f"Successfully deleted the item ({key}).")
                        break

                return
        print(f"\nThe item ({key}) does not exist")
        return

    def display(self):
        for i, value in enumerate(self.table):
            if value is None:
                print(f"Index {i}: Empty")

            else:
                print(f"Index {i}: "
                      f"item_id: {value.item_id} | "
                      f"item_name: {value.name} | "
                      f"item_price: RM{value.price} | "
                      f"item_quantity: {value.quantity}")


ht = HashTable(1009)
array = []
items = {
    Inventory(i, f"Item{i}", 50.0, 50)
    for i in range(1000, 1500)
}

for item in items:
    ht.insert(item)

def array_search(item_id):
    for item in array:
        if item.item_id == item_id:
            return item
    return

while True:
    print(f"\nSelect an option:"
          f"\n1. Display"
          f"\n2. Insert"
          f"\n3. Search"
          f"\n4. Delete"
          f"\n5. Exit")
    option = input("Enter an option: ")

    match option:
        case "1":
            ht.display()

        case "2":
            item_id = int(input(f"Enter item_id: "))
            name = input(f"Enter item_name: ")
            price = float(input(f"Enter item_price: "))
            quantity = int(input(f"Enter item_quantity: "))
            inventory = Inventory(item_id, name, price, quantity)
            ht.insert(inventory)

        case "3":
            item_id = int(input(f"Enter item_id: "))
            ht.search(item_id)
            hash_start = time.perf_counter()
            ht.searchTime(item_id)
            hash_end = time.perf_counter()
            arr_start = time.perf_counter()
            array_search(item_id)
            arr_end = time.perf_counter()
            print(f"Search completed in {hash_end - hash_start:.10f} seconds. (Hash Table)")
            print(f"Search completed in {arr_end - arr_start:.10f} seconds. (One Dimension Array - same record)")

        case "4":
            item_id = int(input(f"Enter item_id: "))
            ht.delete(item_id)

        case "5":
            print(f"Exiting System.")
            break
