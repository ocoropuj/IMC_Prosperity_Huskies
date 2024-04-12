from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string
import numpy as np
import pandas as pd


class Trader:
    
      def run(self, state: TradingState):
            n = 10
            scale = 100
            margin_starfruit = 1
            prices_0 = ''
            for _ in range(n-1):
                  prices_0 += '0,'

            state.traderData = f'AMETHYSTS:{prices_0}10000:0.STARFRUIT:{prices_0}5000:0.'

            print("traderData: " + state.traderData)
            print("Observations: " + str(state.observations))



            def calculate_midprice(product, buy_orders, sell_orders, price_basic=10000):
                  Set_p_q = []
                  try:
                        for p in buy_orders:
                              Set_p_q.append([p, buy_orders[p]])
                  except:
                        Set_p_q.append([price_basic,1])

                  try:
                        for p in sell_orders:
                              Set_p_q.append([p, sell_orders[p]])
                  except:
                        Set_p_q.append([price_basic,1])

                  Set_p_q = np.array(Set_p_q)
                  Q = np.abs(Set_p_q[:,1]).sum()
                  midprice = (Set_p_q[:,0] * abs(Set_p_q[:,1]) / Q).sum()

                  return midprice
                  
            def get_traderData(state, product):
                  parts = state.traderData.split('.')
                  for i, part in enumerate(parts):
                        Prod = part.split(':')[0]
                        if Prod == product:
                              index_of_product = i
                  try:
                        dummy_computation = (index_of_product) + 1
                  except:
                        index_of_product = None

                  print(index_of_product)
                  if index_of_product != None:
                        trader_data_product = parts[index_of_product]
                        splited_trader_data_product = trader_data_product.split(':')
                        inventory = prices = float(splited_trader_data_product[2])
                        Prices = np.array(splited_trader_data_product[1].split(',')).astype(float)
                        new_Prices = Prices[1:]

                        return Prices, new_Prices, inventory

            trader_data = ""

            result = {}
            for product in state.order_depths:
                  if state.timestamp < n*scale:
                        order_depth: OrderDepth = state.order_depths[product]
                        orders: List[Order] = []

                        midprice = calculate_midprice(product, buy_orders=state.order_depths[product].buy_orders, 
                                                      sell_orders=state.order_depths[product].sell_orders)
                        
                        if state.timestamp == 0:
                              prices_str = ""
                              for _ in range(n-1):
                                    prices_str += f'{0},'
                              prices_str += f'{midprice}'
                              inventory = 0

                              trader_data_product = f'{product}:{prices_str}:{inventory}.'
                        else:
                              Prices, new_Prices, inventory = get_traderData(state, product)
                              prices_str = ''
                              for price in new_Prices:
                                    prices_str += f'{price}'
                              trader_data_product = f'{product}:{prices_str}:{inventory}.'
                        
                        trader_data += trader_data_product

                  else:
                        if product == 'AMETHYSTS':
                              Prices, new_Prices, inventory = get_traderData(state, product)
                              prices_str = ''
                              for price in new_Prices:
                                    prices_str += f'{price}'
                              trader_data_product = f'{product}:{prices_str}:{inventory}.'
                              trader_data += trader_data_product

                              order_depth: OrderDepth = state.order_depths[product]
                              orders: List[Order] = []

                              if np.abs(Prices - 10000).mean() > 2:
                                    market = 2
                              else:
                                    market = -1

                              acceptable_price = 10000
                              print("Acceptable price : " + str(acceptable_price))
                              print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))


                              if len(order_depth.sell_orders) != 0:
                                    best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                                    if int(best_ask) < acceptable_price - market:
                                          print("BUY", str(-best_ask_amount) + "x", best_ask)
                                          orders.append(Order(product, best_ask, -best_ask_amount))
                  
                              if len(order_depth.buy_orders) != 0:
                                    best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                                    if int(best_bid) > acceptable_price + market:
                                          print("SELL", str(best_bid_amount) + "x", best_bid)
                                          orders.append(Order(product, best_bid, -best_bid_amount))
                              
                              result[product] = orders
                        elif product == 'STARFRUIT':
                              Prices, new_Prices, inventory = get_traderData(state, product)
                              prices_str = ''
                              for price in new_Prices:
                                    prices_str += f'{price}'
                              trader_data_product = f'{product}:{prices_str}:{inventory}.'
                              trader_data += trader_data_product

                              order_depth: OrderDepth = state.order_depths[product]
                              orders: List[Order] = []

                              mu = pd.Series(Prices).diff().dropna().mean()
                              acceptable_price = Prices[-1]
                              print("Acceptable price : " + str(acceptable_price))
                              print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))


                              if len(order_depth.sell_orders) != 0:
                                    best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                                    if int(best_ask) < acceptable_price + margin_starfruit and mu > 0.5:
                                          print("BUY", str(-best_ask_amount) + "x", best_ask)
                                          orders.append(Order(product, best_ask, -best_ask_amount))
                  
                              if len(order_depth.buy_orders) != 0:
                                    best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                                    if int(best_bid) > acceptable_price - margin_starfruit and mu < -0.5:
                                          print("SELL", str(best_bid_amount) + "x", best_bid)
                                          orders.append(Order(product, best_bid, -best_bid_amount))
                  
                  # String value holding Trader state data required. 
                              # It will be delivered as TradingState.traderData on next execution.
            traderData = trader_data 
            
                              # Sample conversion request. Check more details below. 
            conversions = 1
            return result, conversions, traderData