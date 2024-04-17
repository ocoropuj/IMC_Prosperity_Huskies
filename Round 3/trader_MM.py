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
            
        ratio_long = 1.001
        ratio_short = 0.999

        B_GB = 1
        B_C = 4
        B_S = 6
        B_R = 1

        acceptable_price_long_GB = (B_C * best_ask_C + B_S * best_ask_S + B_R * best_ask_R) / B_GB
        acceptable_price_short_GB = (B_C * best_bid_C + B_S * best_bid_S + B_R * best_bid_R) / B_GB 

        acceptable_price_long_C = (B_GB * best_ask_GB - B_S * best_ask_S - B_R * best_ask_R) / B_C
        acceptable_price_short_C = (B_GB * best_bid_GB - B_S * best_bid_S - B_R * best_bid_R) / B_C

        acceptable_price_long_S = (B_GB * best_ask_GB - B_C * best_ask_C - B_R * best_ask_R) / B_S
        acceptable_price_short_S = (B_GB * best_bid_GB - B_C * best_bid_C - B_R * best_bid_R) / B_S

        acceptable_price_long_R = (B_GB * best_ask_GB - B_C * best_ask_C - B_S * best_ask_S) / B_R
        acceptable_price_short_R = (B_GB * best_bid_GB - B_C * best_bid_C - B_S * best_bid_S) / B_R


        if best_ask_GB < ratio_short * acceptable_price_short_GB:
            orders_GB.append(Order('GIFT_BASKET', best_ask_GB, -best_ask_amount_GB)) # I Buy Gift Basket
            orders_C.append(Order('CHOCOLATE', best_bid_C, - int(B_C * best_bid_amount_GB / B_GB))) # I Sell 4 chocolates
            orders_S.append(Order('STRAWBERRIES', best_bid_S, - int(B_S * best_bid_amount_GB / B_GB))) # I Sell 6 strawberries
            orders_R.append(Order('ROSES', best_bid_R, - int(B_R * best_bid_amount_GB / B_GB))) # I Sell 1 rose

        if best_bid_GB > ratio_long * acceptable_price_long_GB:
            orders_GB.append(Order('GIFT_BASKET', best_bid_GB, -best_bid_amount_GB)) # I Sell Gift Basket
            orders_C.append(Order('CHOCOLATE', best_ask_C, - int(B_C * best_ask_amount_GB / B_GB))) # I Buy 4 chocolates
            orders_S.append(Order('STRAWBERRIES', best_ask_S, - int(B_S * best_ask_amount_GB / B_GB))) # I Buy 6 strawberries
            orders_R.append(Order('ROSES', best_ask_R, - int(B_R * best_ask_amount_GB / B_GB))) # I Buy 1 rose



        if best_ask_C < ratio_short * acceptable_price_short_C:
            orders_C.append(Order('CHOCOLATE', best_ask_C, -best_ask_amount_C)) # I Buy Chocolate
            orders_GB.append(Order('GIFT_BASKET', best_bid_GB, - int(B_GB * best_bid_amount_C / B_C))) # I Sell Gift Basket
            orders_S.append(Order('STRAWBERRIES', best_ask_S, - int(B_S * best_ask_amount_C / B_C))) # I Buy 6 strawberries
            orders_R.append(Order('ROSES', best_ask_R, - int(B_R * best_ask_amount_C / B_C))) # I Buy 1 rose
        
        if best_bid_C > ratio_long * acceptable_price_long_C:
            orders_C.append(Order('CHOCOLATE', best_bid_C, -best_bid_amount_C)) # I Sell Chocolate
            orders_GB.append(Order('GIFT_BASKET', best_ask_GB, - int(B_GB * best_ask_amount_C / B_C))) # I Buy Gift Basket
            orders_S.append(Order('STRAWBERRIES', best_bid_S, - int(B_S * best_bid_amount_C / B_C))) # I Sell 6 strawberries
            orders_R.append(Order('ROSES', best_bid_R, - int(B_R * best_bid_amount_C / B_C))) # I Sell 1 rose
        


        if best_ask_S < ratio_short * acceptable_price_short_S:
            orders_S.append(Order('STRAWBERRIES', best_ask_S, -best_ask_amount_S)) # I Buy Strawberries
            orders_GB.append(Order('GIFT_BASKET', best_bid_GB, - int(B_GB * best_bid_amount_S / B_S))) # I Sell Gift Basket
            orders_C.append(Order('CHOCOLATE', best_ask_C, - int(B_C * best_ask_amount_S / B_S))) # I Buy 4 chocolates
            orders_R.append(Order('ROSES', best_ask_R, - int(B_R * best_ask_amount_S / B_S))) # I Buy 1 rose
        
        if best_bid_S > ratio_long * acceptable_price_long_S:
            orders_S.append(Order('STRAWBERRIES', best_bid_S, -best_bid_amount_S)) # I Sell Strawberries
            orders_GB.append(Order('GIFT_BASKET', best_ask_GB, - int(B_GB * best_ask_amount_S / B_S))) # I Buy Gift Basket
            orders_C.append(Order('CHOCOLATE', best_bid_C, - int(B_C * best_bid_amount_S / B_S))) # I Sell 4 chocolates
            orders_R.append(Order('ROSES', best_bid_R, - int(B_R * best_bid_amount_S / B_S))) # I Sell 1 rose



        if best_ask_R < ratio_short * acceptable_price_short_R:
            orders_R.append(Order('ROSES', best_ask_R, -best_ask_amount_R)) # I Buy Roses
            orders_GB.append(Order('GIFT_BASKET', best_bid_GB, - int(B_GB * best_bid_amount_R / B_R))) # I Sell Gift Basket
            orders_C.append(Order('CHOCOLATE', best_ask_C, - int(B_C * best_ask_amount_R / B_R))) # I Buy 4 chocolates
            orders_S.append(Order('STRAWBERRIES', best_ask_S, - int(B_S * best_ask_amount_R / B_R))) # I Buy 6 strawberries
        
        if best_bid_R > ratio_long * acceptable_price_long_R:
            orders_R.append(Order('ROSES', best_bid_R, -best_bid_amount_R)) # I Sell Roses
            orders_GB.append(Order('GIFT_BASKET', best_ask_GB, - int(B_GB * best_ask_amount_R / B_R))) # I Buy Gift Basket
            orders_C.append(Order('CHOCOLATE', best_bid_C, - int(B_C * best_bid_amount_R / B_R))) # I Sell 4 chocolates
            orders_S.append(Order('STRAWBERRIES', best_bid_S, - int(B_S * best_bid_amount_R / B_R))) # I Sell 6 strawberries


        result['GIFT_BASKET'] = orders_GB
        result['CHOCOLATE'] = orders_C
        result['STRAWBERRIES'] = orders_S
        result['ROSES'] = orders_R

        traderData = 'sample'


        return result, 1, traderData
