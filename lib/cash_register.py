#!/usr/bin/env python3

import ipdb
class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = [] 
    self.prev_transaction = [] #[{}, {}]

  def add_item(self, title, price, quantity=1):
    self.total += (price * quantity)
    #self.items.append(title)
    # for i in range(quantity):
    #   self.items.append(title)
    # [title] * quantity = [title, title, title, ...]
    self.items.extend([title] * quantity)
    self.prev_transaction.append({
      'quantity': quantity,
      'price': price, 
      'title': title
    })
    #print(self.prev_transaction)


  def apply_discount(self):
    if(self.discount == 0):
      print("There is no discount to apply.")
    else:
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")


  def void_last_transaction(self):
    #what info do we need to accomplish this - price, quantity, title
    #how are we going to store said info - self.prev_transactions, list of dictionaries
    #math to take into account discount
    
    # check if any transactions have been made
    if(len(self.items) == 0):
      raise Exception("No transactions made")
    
    # pop off last item from .prev_transaction (which both removes and returns last item)
    prev = self.prev_transaction.pop()
    
    # get total value to subtract from price 
    subtract_price = prev['price'] * prev['quantity'] 
    self.total = self.total - (subtract_price)
    # update self.items and remove relevant items 
    # for _ in range(prev['quantity']):
    #   self.items.pop()
    print(f'prev is {prev} self.total is {self.total}')
    self.items = self.items[:-prev['quantity']]



  def __repr__(self):
    return f'<CashRegister prev_transaction = {self.prev_transaction} total = {self.total} discount = {self.discount} items={self.items} />'

# cash_register = CashRegister()
# cash_register_with_discount = CashRegister(20)
# cash_register_with_discount.add_item("macbook air", 1000)
# cash_register.add_item("apple", 0.99)
# cash_register.add_item("tomato", 1.76)
# cash_register.add_item("cucumber", 0.99)
# cash_register.add_item("onion", 0.99)
# cash_register.add_item("tomato", 1.76, 2)
# cash_register_with_discount.add_item("eggs", 1.99, 2)
# cash_register_with_discount.add_item("tomato", 1.76, 3)
# cash_register.add_item("Ritz Crackers", 5.0)
# cash_register_with_discount.add_item("Justin's Peanut Butter Cups", 2.50, 2)

# ipdb.set_trace()

