from datamodel import OrderDepth, UserId, TradingState, Order, OwnTrade
from typing import List
import string
import numpy as np


# Define traders and assets in the specified order
traders = ['Adam', 'Amelia', 'Raj', 'Remy', 'Rhianna', 'Ruby', 'Valentina', 'Vinnie', 'Vladimir']
assets = ['AMETHYSTS', 'STARFRUIT', 'GIFT_BASKET', 'CHOCOLATE', 'STRAWBERRIES', 'ROSES', 'COCONUT', 'COCONUT_COUPON']

# Define the data
data = {
    'Adam': [0, 0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Amelia': [1, None, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Raj': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, None, np.nan],
    'Remy': [-1, -2, None, None, None, None, np.nan, np.nan],
    'Rihana': [0, None, None, 0, np.nan, np.nan, -1, -2],
    'Ruby': [-2, 0, None, np.nan, np.nan, np.nan, np.nan, None],
    'Valentina': [0, None, np.nan, np.nan, np.nan, np.nan, np.nan, 3],
    'Vinnie': [1, -2, 1.5, 2, 2.5, 2, -3, -3],
    'Vladimir': [1, -1, 2, -3, -3, -2, np.nan, 2]
}

# Create the DataFrame
df = pd.DataFrame(data, index=assets)


class Trader:
    def __innit__(self):
          self.prices_starfruit = []
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

        result = {}
        for product in state.order_depths:
            order_depth: OrderDepth = state.order_depths[product]
            own_trades: OwnTrade = state.own_trades[product]
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
		# String value holding Trader state data required. 
  
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData