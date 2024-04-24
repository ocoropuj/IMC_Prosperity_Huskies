from datamodel import OrderDepth, UserId, TradingState, Order, OwnTrade
from typing import List
import string
import numpy as np
import pandas as pd


# Define traders and assets in the specified order
traders = ['Adam', 'Amelia', 'Raj', 'Remy', 'Rhianna', 'Ruby', 'Valentina', 'Vinnie', 'Vladimir']
assets = ['AMETHYSTS', 'STARFRUIT', 'GIFT_BASKET', 'CHOCOLATE', 'STRAWBERRIES', 'ROSES', 'COCONUT', 'COCONUT_COUPON']

# Define the data
data = {
      'Vinnie': [1, -2, 1.5, 2, 2.5, 2, -3, -3],
      'Vladimir': [1, -1, 2, -3, -3, -2, np.nan, 2],
      'Valentina': [0, None, np.nan, np.nan, np.nan, np.nan, np.nan, 3],
      'Adam': [0, 0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
      'Amelia': [1, None, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
      'Raj': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, None, np.nan],
      'Remy': [-1, -2, None, None, None, None, np.nan, np.nan],
      'Rihana': [0, None, None, 0, np.nan, np.nan, -1, -2],
      'Ruby': [-2, 0, None, np.nan, np.nan, np.nan, np.nan, None]
}

# Create the DataFrame
people_data = pd.DataFrame(data, index=assets)


class Trader:
      def __innit__(self):
          self.prices_starfruit = []
    
      def run(self, state: TradingState):
            print("traderData: " + state.traderData)
            print("Observations: " + str(state.observations))

            result = {}
            for trader in state.own_trades:
                  orders: List[Order] = []
                  own_trade: OwnTrade = state.own_trades[trader]
                  try:
                        symbol = own_trade.symbol
                        score = people_data[trader].loc[symbol]
                        price = own_trade.price
                        quantity = own_trade.quantity
                        if quantity > 0 and score > 0:
                              price_delta = 1.01
                        elif quantity < 0 and score > 0:
                              price_delta = 0.99
                        else:
                              price_delta = 1


                        orders.append(Order(symbol, price_delta*price, int(score*quantity)))
                        result[symbol] = orders 
                  
                  except:
                        print(f'No trades from {trader}')
                  
            traderData = "SAMPLE" 
            
                              # Sample conversion request. Check more details below. 
            conversions = 1
            return result, conversions, traderData