class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' Tambahkan ke dalam List.")

    def dequeue(self):
        if not self.queue:
            print("Tidak ada Pesanan di List.")
            return None
        order = self.queue.pop(0)
        print(f"Pesanan '{order}' telah disajikan.")
        return order

    def display_queue(self):
        print("List saat ini:")
        for i, order in enumerate(self.queue):
            print(f"{i+1}. {order}")

queue = RestaurantQueue()

queue.enqueue("Mie Ayam")
queue.enqueue("Teh Anget")
queue.enqueue("Es Teh")
queue.enqueue("Bakso")

queue.display_queue()

queue.dequeue()

queue.display_queue()

queue.dequeue()

queue.display_queue()