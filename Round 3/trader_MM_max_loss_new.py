from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string


class Trader:

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

        if len_GB_S != 0 and len_C_S != 0 and len_S_S != 0 and len_R_S != 0 and len_GB_B != 0 and len_C_B != 0 and len_S_B != 0 and len_R_B != 0:
            best__bid_GB, best__bid_amount_GB = list(order_depth_GB.sell_orders.items())[0]
            best__bid_C, best__bid_amount_C = list(order_depth_C.sell_orders.items())[0]
            best__bid_S, best__bid_amount_S = list(order_depth_S.sell_orders.items())[0]
            best__bid_R, best__bid_amount_R = list(order_depth_R.sell_orders.items())[0]
            
            best_ask_GB, best_ask_amount_GB = list(order_depth_GB.buy_orders.items())[0]
            best_ask_C, best_ask_amount_C = list(order_depth_C.buy_orders.items())[0]
            best_ask_S, best_ask_amount_S = list(order_depth_S.buy_orders.items())[0]
            best_ask_R, best_ask_amount_R = list(order_depth_R.buy_orders.items())[0]

            ratio_short = 0.99
            ratio_long = 1.01

            acceptable_price_long_GB = 4 * best__bid_C + 6 * best__bid_S + best__bid_R
            acceptable_price_short_GB = 4 * best_ask_C + 6 * best_ask_S + best_ask_R
            if best_ask_GB > ratio_short * acceptable_price_short_GB:
                orders_GB.append(Order('GIFT_BASKET', best__bid_GB, -best__bid_amount_GB))
            if best__bid_GB < ratio_long * acceptable_price_long_GB:
                orders_GB.append(Order('GIFT_BASKET', best_ask_GB, -best_ask_amount_GB))
            result['GIFT_BASKET'] = orders_GB
            
            acceptable_price_long_C = 0.25 * (best__bid_GB - 6 * best__bid_S - best__bid_R)
            acceptable_price_short_C = 0.25 * (best_ask_GB - 6 * best_ask_S - best_ask_R)
            if best_ask_C > ratio_short * acceptable_price_short_C:
                orders_C.append(Order('CHOCOLATE', best__bid_C, -best__bid_amount_C))
            if best__bid_C < ratio_long * acceptable_price_long_C:
                orders_C.append(Order('CHOCOLATE', best_ask_C, -best_ask_amount_C))
            result['CHOCOLATE'] = orders_C

            acceptable_price_long_S = (best__bid_GB - 4 * best__bid_C - best__bid_R) / 6
            acceptable_price_short_S = (best_ask_GB - 4 * best_ask_C - best_ask_R) / 6
            if best_ask_S > ratio_short * acceptable_price_short_S:
                orders_S.append(Order('STRAWBERRIES', best__bid_S, -best__bid_amount_S))
            if best__bid_S < ratio_long * acceptable_price_long_S:
                orders_S.append(Order('STRAWBERRIES', best_ask_S, -best_ask_amount_S))
            result['STRAWBERRIES'] = orders_S

            acceptable_price_long_R = (best__bid_GB - 4 * best__bid_C - 6 * best__bid_S)
            acceptable_price_short_R = (best_ask_GB - 4 * best_ask_C - 6 * best_ask_S)
            if best_ask_R > ratio_short * acceptable_price_short_R:
                orders_R.append(Order('ROSES', best__bid_R, -best__bid_amount_R))
            if best__bid_R < ratio_long * acceptable_price_long_R:
                orders_R.append(Order('ROSES', best_ask_R, -best_ask_amount_R))
            result['ROSES'] = orders_R

        traderData = 'sample'


        return result, 1, traderData
    