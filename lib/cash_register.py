#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.quantities = []
    self.last_item_price = 0
    #list of dictionaries of previous transactions
    #each dictionary will contain info regarding one transaction
    #item, price, quantity
    #best for keeping a single source of truth
    self.prev_transactions = []

  def add_item(self, title, price, quantity=1):
    self.prev_transactions.append({
      "title": title,
      "price": price,
      "quantity": quantity
    })
    self.total += (price * quantity)
    # for i in range(0, quantity):
    #   self.items.append(title)

    #this way each list will contain one entry for title and one corresponding entry for quantity 
    self.items.append(title)
    self.quantities.append(quantity)
    self.last_item_price = price

  def apply_discount(self):
    if(self.discount > 0):
      self.total = self.total - ((self.discount/100) * self.total )
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else: 
      print("There is no discount to apply.")

  def void_last_transaction(self):
    #length = len(self.quantities) - 1 #length of list
    #self.total = self.total - (self.last_item_price * self.quantities[length])
    # last_quantity = self.quantities[len(self.quantities) - 1]
    # for i in range(0, last_quantity):
    #   self.items.pop()
    #   self.quantities.pop()


    #subtract last transaction from total using self.prev_transactions
    last_transaction = self.prev_transactions.pop()
    self.total = self.total - (last_transaction["price"] * last_transaction["quantity"])

cr = CashRegister()
cr.add_item('tomato', 2, 3)
cr.add_item('egg', 1, 8)
cr.add_item('bread', 5, 2)
# import ipdb; ipdb.set_trace()