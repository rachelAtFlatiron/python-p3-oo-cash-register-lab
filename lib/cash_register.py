#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prices = []

  def add_item(self, item, price, quantity=1):
    self.total += price*quantity
    for i in range(0, quantity):
      self.items.append(item)
      self.prices.append(price)

  def apply_discount(self):
    self.total = self.total - (self.total * self.discount/100)

    if(self.discount == 0 or self.total == 0):
      print(f'There is no discount to apply.')
    else:
      print(f'After the discount, the total comes to ${self.total:n}.')

  def void_last_transaction(self):
      i = len(self.items) - 1
      last_item = self.items[i]
      cur_item = self.items[i]
      while(last_item == cur_item and i >= 0):
        self.total -= self.prices[i]
        self.prices.pop()
        self.items.pop()
        i -= 1
        cur_item = self.items[i]
        
      if(len(self.items) == 0):
        self.total = 0

    
#import ipdb; ipdb.set_trace()