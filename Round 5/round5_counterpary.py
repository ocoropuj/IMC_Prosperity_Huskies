from datamodel import OrderDepth, UserId, TradingState, Order, OwnTrade
from typing import List
import string
import numpy as np

class Trader:
    def __innit__(self):
          self.prices_starfruit = []
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

				# Orders to be placed on exchange matching engine
        result = {}
        for product in state.order_depths:
            if product == 'AMETHYSTS':
                  order_depth: OrderDepth = state.order_depths[product]
                  own_trades: OwnTrade = 
                  orders: List[Order] = []
                  acceptable_price = 10000  # Participant should calculate this value
                  print("Acceptable price : " + str(acceptable_price))
                  print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
      
                  if len(order_depth.sell_orders) != 0:
                        best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                        print(f'Best Ask: {best_ask_amount}')
                        if int(best_ask) < acceptable_price:
                              print("BUY", str(-best_ask_amount) + "x", best_ask)
                              orders.append(Order(product, best_ask, -best_ask_amount))
      
                  if len(order_depth.buy_orders) != 0:
                        best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                        print(f'Best bid: {best_bid_amount}')
                        if int(best_bid) > acceptable_price:
                              print("SELL", str(best_bid_amount) + "x", best_bid)
                              orders.append(Order(product, best_bid, -best_bid_amount))
                  
                  result[product] = orders
            else:
                  order_depth: OrderDepth = state.order_depths[product]
                  orders: List[Order] = []
                  
                  acceptable_price_sell = 5070  # Participant should calculate this value
                  acceptable_price_buy = 5000
                  print("Acceptable price : " + str(acceptable_price))
                  print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))
      
                  if len(order_depth.sell_orders) != 0:
                        best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                        print(f'Best Ask: {best_ask_amount}')
                        if int(best_ask) < acceptable_price_buy:
                              print("BUY", str(-best_ask_amount) + "x", best_ask)
                        orders.append(Order(product, best_ask, -best_ask_amount))
      
                  if len(order_depth.buy_orders) != 0:
                        best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                        print(f'Best bid: {best_bid_amount}')
                        if int(best_bid) > acceptable_price_sell:
                              print("SELL", str(best_bid_amount) + "x", best_bid)
                              orders.append(Order(product, best_bid, -best_bid_amount))
                  
                  result[product] = orders 
		    # String value holding Trader state data required. 
				# It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData