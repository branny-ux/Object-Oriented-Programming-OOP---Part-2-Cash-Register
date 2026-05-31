class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        if self.total == int(self.total):
            self.total = int(self.total)

    def void_last_transaction(self):
        if not self.previous_transactions:
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
