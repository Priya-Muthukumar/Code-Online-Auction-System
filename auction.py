
import json
import heapq

class AuctionItem:
    def _init_(self, item_id, name, description):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.current_bid = 0
        self.bids = []

    def place_bid(self, bid_amount):
        if bid_amount > self.current_bid:
            heapq.heappush(self.bids, (-bid_amount, bid_amount))  # Use a max-heap
            self.current_bid = bid_amount
            return True
        return False

class AuctionSystem:
    def _init_(self):
        self.items = {}
        self.next_item_id = 1
    def add_item(self, name, description):
        item = AuctionItem(self.next_item_id, name, description)
        self.items[self.next_item_id] = item
        self.next_item_id += 1

    def place_bid(self, item_id, bid_amount):
        if item_id in self.items:
            return self.items[item_id].place_bid(bid_amount)
        return False

    def get_items(self):
        return list(self.items.values())

auction_system = AuctionSystem()

def main():
    while True:
        print("\n1. Add Item")
        print("2. Place Bid")
        print("3. List Items")
        print("4. View History")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            auction_system.add_item(name, description)
            print("Item added successfully.")

        elif choice == '2':
            item_id = int(input("Enter item ID to place a bid on: "))
            bid_amount = float(input("Enter bid amount: "))
            success = auction_system.place_bid(item_id, bid_amount)
            if success:
                print("Bid placed successfully.")
            else:
                print("Bid failed. Amount too low or item ID not found.")

        elif choice == '3':
            items = auction_system.get_items()
            for item in items:
                print(f"Item ID: {item.item_id}, Name: {item.name}, Current Bid: ${item.current_bid}")

        elif choice == '4':
            items = auction_system.get_items()
            for item in items:
                print(f"Item ID: {item.item_id}, Name: {item.name}, Bids: {[-bid[0] for bid in item.bids]}")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()