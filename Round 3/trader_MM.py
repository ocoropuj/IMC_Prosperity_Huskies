from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string


class Trader:
    def __innit__(self):
          self.prices_starfruit = []
    
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

		# Orders to be placed on exchange matching engine
        result = {}
        order_depth_GB: OrderDepth = state.order_depths['GIFT_BASKET']
        order_depth_C: OrderDepth = state.order_depths['CHOCOLATE']
        order_depth_S: OrderDepth = state.order_depths['STRAWBERRIES']
        order_depth_R: OrderDepth = state.order_depths['ROSES']
        len_GB_B, len_GB_S = len(order_depth_GB.buy_orders), len(order_depth_GB.sell_orders)
        len_C_B, len_C_S = len(order_depth_C.buy_orders), len(order_depth_C.sell_orders)
        len_S_B, len_S_S = len(order_depth_S.buy_orders), len(order_depth_S.sell_orders)
        len_R_B, len_R_S = len(order_depth_R.buy_orders), len(order_depth_R.sell_orders)

        orders_GB: List[Order] = []
        orders_C: List[Order] = []
        orders_S: List[Order] = []
        orders_R: List[Order] = []

        if len_GB_S != 0 and len_C_S != 0 and len_S_S != 0 and len_R_S != 0:
            best_ask_GB, best_ask_amount_GB = list(order_depth_GB.sell_orders.items())[0]
            best_ask_C, best_ask_amount_C = list(order_depth_C.sell_orders.items())[0]
            best_ask_S, best_ask_amount_S = list(order_depth_S.sell_orders.items())[0]
            best_ask_R, best_ask_amount_R = list(order_depth_R.sell_orders.items())[0]
            
        if len_GB_B != 0 and len_C_B != 0 and len_S_B != 0 and len_R_B != 0:
            best_bid_GB, best_bid_amount_GB = list(order_depth_GB.buy_orders.items())[0]
            best_bid_C, best_bid_amount_C = list(order_depth_C.buy_orders.items())[0]
            best_bid_S, best_bid_amount_S = list(order_depth_S.buy_orders.items())[0]
            best_bid_R, best_bid_amount_R = list(order_depth_R.buy_orders.items())[0]
            

        acceptable_price_short_GB = 4 * best_ask_C + 6 * best_ask_S + best_ask_R
        acceptable_price_long_GB = 4 * best_bid_C + 6 * best_bid_S + best_bid_R
        if best_ask_GB > acceptable_price_short_GB:
            orders_GB.append(Order('GIFT_BASKET', best_ask_GB, -best_ask_amount_GB))
        if best_bid_GB < acceptable_price_long_GB:
            orders_GB.append(Order('GIFT_BASKET', best_bid_GB, -best_bid_amount_GB))
        result['GIFT_BASKET'] = orders_GB
        
        acceptable_price_short_C = 0.25 * (best_ask_GB - 6 * best_ask_S - best_ask_R)
        acceptable_price_long_C = 0.25 * (best_bid_GB - 6 * best_bid_S - best_bid_R)
        if best_ask_C > acceptable_price_short_C:
            orders_C.append(Order('CHOCOLATE', best_ask_C, -best_ask_amount_C))
        if best_bid_C < acceptable_price_long_C:
            orders_C.append(Order('CHOCOLATE', best_bid_C, -best_bid_amount_C))
        result['CHOCOLATE'] = orders_C

        acceptable_price_short_S = (best_ask_GB - 4 * best_ask_C - best_ask_R) / 6
        acceptable_price_long_S = (best_bid_GB - 4 * best_bid_C - best_bid_R) / 6
        if best_ask_S > acceptable_price_short_S:
            orders_S.append(Order('STRAWBERRIES', best_ask_S, -best_ask_amount_S))
        if best_bid_S < acceptable_price_long_S:
            orders_S.append(Order('STRAWBERRIES', best_bid_S, -best_bid_amount_S))
        result['STRAWBERRIES'] = orders_S

        acceptable_price_short_R = (best_ask_GB - 4 * best_ask_C - 6 * best_ask_S)
        acceptable_price_long_R = (best_bid_GB - 4 * best_bid_C - 6 * best_bid_S)
        if best_ask_R > acceptable_price_short_R:
            orders_R.append(Order('ROSES', best_ask_R, -best_ask_amount_R))
        if best_bid_R < acceptable_price_long_R:
            orders_R.append(Order('ROSES', best_bid_R, -best_bid_amount_R))
        result['ROSES'] = orders_R

        traderData = 'sample'


        return result, 1, traderData
    