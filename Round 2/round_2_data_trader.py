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
            ship_cost = ''
            for _ in range(n-1):
                  ship_cost += '0,'
            import_t = ''
            for _ in range(n-1):
                  import_t += '0,'
            export_t = ''
            for _ in range(n-1):
                  export_t += '0,'
            sunlight = ''
            for _ in range(n-1):
                  sunlight += '0,'            
            humidity = ''
            for _ in range(n-1):
                  humidity += '0,'

            state.traderData = f'ORCHIDS:{prices_0}1035:0:{ship_cost}:{import_t}:{export_t}:{sunlight}:{humidity}' #AMETHYSTS:{prices_0}10000:0.STARFRUIT:{prices_0}5000:0.'

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

                  if index_of_product != None:
                        trader_data_product = parts[index_of_product]
                        splited_trader_data_product = trader_data_product.split(':')
                        inventory = float(splited_trader_data_product[2])
                        Prices = np.array(splited_trader_data_product[1].split(',')).astype(float)
                        new_Prices = Prices[1:]

                        return Prices, new_Prices, inventory
                  
            def get_traderData_Orchids(state, product):
                  parts = state.traderData.split('.')
                  for i, part in enumerate(parts):
                        Prod = part.split(':')[0]
                        if Prod == product:
                              index_of_product = i

                  if index_of_product != None:
                        trader_data_product = parts[index_of_product]
                        splited_trader_data_product = trader_data_product.split(':')
                        inventory = float(splited_trader_data_product[2])
                        Prices = np.array(splited_trader_data_product[1].split(',')).astype(float)
                        shipping_costs = np.array(splited_trader_data_product[3].split(',')).astype(float)
                        import_tariff = np.array(splited_trader_data_product[4].split(',')).astype(float)
                        export_tariff = np.array(splited_trader_data_product[5].split(',')).astype(float)
                        sunlight = np.array(splited_trader_data_product[6].split(',')).astype(float)
                        humidity = np.array(splited_trader_data_product[8].split(',')).astype(float)
                  
                        return Prices, inventory, shipping_costs, import_tariff, export_tariff, sunlight, humidity
                  
            def write_trader_data(state, product):      
                  midprice = calculate_midprice(product, buy_orders=state.order_depths[product].buy_orders, sell_orders=state.order_depths[product].sell_orders)
                  Prices, inventory, shipping_costs, import_tariff, export_tariff, sunlight, humidity = get_traderData_Orchids(state, product)
                                    
                  new_shipping_cost = state.transportFees
                  new_export, new_import = state.exportTariff, state.importTariff
                  new_sunL, new_humid = state.sunlight, state.humidity

                  prices_str = ''
                  for price in Prices[-1:]:
                        prices_str += f'{price},'

                  ship_cost_str = ""
                  for ship in shipping_costs[-1:]:
                        ship_cost_str += f'{ship},'
                  ship_cost_str += f'{new_shipping_cost}'

                  import_t_str = ""
                  for imp in import_tariff[-1:]:
                        import_t_str += f'{imp},'
                  import_t_str += f'{new_export}'

                  export_t_str = ""
                  for exp in export_tariff[-1:]:
                        export_t_str += f'{exp},'
                  export_t_str += f'{new_import}'

                  sunlight_str = ""
                  for sun in sunlight[-1:]:
                        sunlight_str += f'{sun},'
                  sunlight_str += f'{new_sunL}'

                  humidity_str = ""
                  for hum in humidity[-1:]:
                        humidity_str += f'{hum},'
                  humidity_str += f'{new_humid}'

                  trader_data_product = f'{product}:{prices_str},{midprice}:{inventory}:{ship_cost_str}:{import_t_str}:{export_t_str}:{sunlight_str}:{humidity_str}'

                  return trader_data_product

            trader_data = ""

            result = {}
            for product in state.order_depths:
                  if product == 'ORCHIDS':
                        if state.timestamp < n*scale:
                              order_depth: OrderDepth = state.order_depths[product]
                              orders: List[Order] = []

                              midprice = calculate_midprice(product, buy_orders=state.order_depths[product].buy_orders, 
                                                            sell_orders=state.order_depths[product].sell_orders)
                              
                              new_shipping_cost = state.transportFees
                              new_export = state.exportTariff
                              new_import = state.importTariff
                              new_sunL = state.sunlight
                              new_humid = state.humidity

                              if state.timestamp == 0:
                                    prices_str = ""
                                    for _ in range(n-1):
                                          prices_str += f'{0},'
                                    prices_str += f'{midprice}'
                                    inventory = 0

                                    ship_cost_str = ""
                                    for _ in range(n-1):
                                          ship_cost_str += f'{0},'
                                    ship_cost_str += f'{new_shipping_cost}'

                                    import_t_str = ""
                                    for _ in range(n-1):
                                          import_t_str += f'{0},'
                                    import_t_str += f'{new_export}'

                                    export_t_str = ""
                                    for _ in range(n-1):
                                          export_t_str += f'{0},'
                                    export_t_str += f'{new_import}'

                                    sunlight_str = ""
                                    for _ in range(n-1):
                                          sunlight_str += f'{0},'
                                    sunlight_str += f'{new_sunL}'

                                    humidity_str = ""
                                    for _ in range(n-1):
                                          humidity_str += f'{0},'
                                    humidity_str += f'{new_humid}'


                                    trader_data_product = f'{product}:{prices_str}:{inventory}:{ship_cost_str}:{import_t_str}:{export_t_str}:{sunlight_str}:{humidity_str}'
                              else:
                                    #Prices, new_Prices, inventory = get_traderData(state, product)
                                    Prices, inventory, shipping_costs, import_tariff, export_tariff, sunlight, humidity = get_traderData_Orchids(state, product)
                                    trader_data_product = write_trader_data(state, product)               
                                    trader_data += trader_data_product

                  else:
                        if product == 'ORCHIDS':
                              acceptable_price = 1100
                              print("Acceptable price : " + str(acceptable_price))
                              print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))


                              if len(order_depth.sell_orders) != 0:
                                    best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                                    if int(best_ask) < acceptable_price :
                                          print("BUY", str(-best_ask_amount) + "x", best_ask)
                                          orders.append(Order(product, best_ask, -best_ask_amount))
                  
                              if len(order_depth.buy_orders) != 0:
                                    best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                                    if int(best_bid) > acceptable_price:
                                          print("SELL", str(best_bid_amount) + "x", best_bid)
                                          orders.append(Order(product, best_bid, -best_bid_amount))
                              
                              result[product] = orders
                        
                        elif product == 'AMETHYSTS':
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