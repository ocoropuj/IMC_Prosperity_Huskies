from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string
import numpy as np
import pandas as pd
import math
import statistics

def norm_pdf(x):
  if isinstance(x, pd.Series):
        return x.apply(lambda y: np.exp(-0.5 * y**2) / np.sqrt(2 * np.pi))
  else:
      return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)

def norm_cdf(x):
    if isinstance(x, pd.Series):
        return x.apply(lambda y: 0.5 * (1 + math.erf(y / math.sqrt(2))))
    else:
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def black_scholes(S, sigma, K=K, T=T, r=r):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    C = S * norm_cdf(d1) - K * np.exp(-r * T) * norm_cdf(d2)
    return C

def inverse_black_scholes(C_target, sigma, K=K, T=T, r=r):
    # Initial guess for S
    S = C_target  # Starting guess as the option price is often close to the stock price
    tolerance = 1e-5  # Tolerance for convergence
    max_iterations = 100  # Max iterations to prevent infinite loops
    
    for i in range(max_iterations):
        C = black_scholes(S, sigma, K, T, r)
        # Calculate Black-Scholes derivative w.r.t. S (Vega)
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        vega = S * norm_cdf(d1) * np.sqrt(T)  # approximation
        
        # Newton-Raphson iteration
        S_next = S - (C - C_target) / max(vega.any(), 1e-3)
        
        # Check if the change is within the tolerance
        if (abs(S_next - S) < tolerance).all():
            return S_next
        S = S_next
    
    return S  # Return the last computed value if not converged

sigma_coco = 0.010325871983015607
T = 250
r = 0
K = 10000
        

class Trader:
    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

		# Orders to be placed on exchange matching engine
        result = {}

        order_depth_COCO: OrderDepth = state.order_depths['COCONUT']
        order_depth_CC: OrderDepth = state.order_depths['COCONUT_COUPON']

        len_COCO_B, len_COCO_S = len(order_depth_COCO.buy_orders), len(order_depth_COCO.sell_orders)
        len_CC_B, len_CC_S = len(order_depth_CC.buy_orders), len(order_depth_CC.sell_orders)

        orders_COCO: List[Order] = []
        orders_C: List[Order] = []


















        order_depth_GB: OrderDepth = state.order_depths['GIFT_BASKET']
        order_depth_C: OrderDepth = state.order_depths['CHOCOLATE']
        order_depth_S: OrderDepth = state.order_depths['STRAWBERRIES']
        order_depth_R: OrderDepth = state.order_depths['ROSES']
        order_depth_A: OrderDepth = state.order_depths['AMETHYSTS']

        len_GB_B, len_GB_S = len(order_depth_GB.buy_orders), len(order_depth_GB.sell_orders)
        len_C_B, len_C_S = len(order_depth_C.buy_orders), len(order_depth_C.sell_orders)
        len_S_B, len_S_S = len(order_depth_S.buy_orders), len(order_depth_S.sell_orders)
        len_R_B, len_R_S = len(order_depth_R.buy_orders), len(order_depth_R.sell_orders)
        len_A_B, len_A_S = len(order_depth_A.buy_orders), len(order_depth_A.sell_orders)


        orders_GB: List[Order] = []
        orders_C: List[Order] = []
        orders_S: List[Order] = []
        orders_R: List[Order] = []
        orders_A: List[Order] = []

        acceptable_price_A = 10000
        if len_A_B != 0 and len_A_S != 0:
            best_ask, best_ask_amount = list(order_depth_A.sell_orders.items())[0]
            if int(best_ask) < acceptable_price_A:
                orders_A.append(Order('AMETHYSTS', best_ask, -best_ask_amount))
            best_bid, best_bid_amount = list(order_depth_A.buy_orders.items())[0]
            if int(best_ask) < acceptable_price_A:
                orders_A.append(Order('AMETHYSTS', best_bid, -best_bid_amount))

        result['AMETHYSTS'] = orders_R


        if len_GB_S != 0 and len_C_S != 0 and len_S_S != 0 and len_R_S != 0 and len_GB_B != 0 and len_C_B != 0 and len_S_B != 0 and len_R_B != 0:
            best_ask_GB, best_ask_amount_GB = list(order_depth_GB.sell_orders.items())[0]
            best_ask_C, best_ask_amount_C = list(order_depth_C.sell_orders.items())[0]
            best_ask_S, best_ask_amount_S = list(order_depth_S.sell_orders.items())[0]
            best_ask_R, best_ask_amount_R = list(order_depth_R.sell_orders.items())[0]
            
            best_bid_GB, best_bid_amount_GB = list(order_depth_GB.buy_orders.items())[0]
            best_bid_C, best_bid_amount_C = list(order_depth_C.buy_orders.items())[0]
            best_bid_S, best_bid_amount_S = list(order_depth_S.buy_orders.items())[0]
            best_bid_R, best_bid_amount_R = list(order_depth_R.buy_orders.items())[0]
                
            ratio_long = 1 - 0.00025
            ratio_short = 1 + 0.00025

            B_GB = 1
            B_C = 4
            B_S = 6
            B_R = 1

            ask_mid_delta = 368
            bid_mid_delta = 372

            acceptable_price_long_GB = (B_C * best_ask_C + B_S * best_ask_S + B_R * best_ask_R) / B_GB - ask_mid_delta / B_GB
            acceptable_price_short_GB = (B_C * best_bid_C + B_S * best_bid_S + B_R * best_bid_R) / B_GB - bid_mid_delta / B_GB

            acceptable_price_long_C = (B_GB * best_ask_GB - B_S * best_ask_S - B_R * best_ask_R) / B_C - ask_mid_delta / B_C
            acceptable_price_short_C = (B_GB * best_bid_GB - B_S * best_bid_S - B_R * best_bid_R) / B_C - bid_mid_delta / B_C

            acceptable_price_long_S = (B_GB * best_ask_GB - B_C * best_ask_C - B_R * best_ask_R) / B_S - ask_mid_delta / B_S
            acceptable_price_short_S = (B_GB * best_bid_GB - B_C * best_bid_C - B_R * best_bid_R) / B_S - bid_mid_delta / B_S

            acceptable_price_long_R = (B_GB * best_ask_GB - B_C * best_ask_C - B_S * best_ask_S) / B_R + ask_mid_delta / B_R
            acceptable_price_short_R = (B_GB * best_bid_GB - B_C * best_bid_C - B_S * best_bid_S) / B_R + bid_mid_delta / B_R

            if best_ask_GB < ratio_short * acceptable_price_short_GB:
                orders_GB.append(Order('GIFT_BASKET', best_bid_GB, -best_bid_amount_GB)) # I Buy Gift Basket
                orders_C.append(Order('CHOCOLATE', best_ask_C, - best_ask_amount_C)) # I Sell 4 chocolates
                orders_S.append(Order('STRAWBERRIES', best_ask_S, - best_ask_amount_S)) # I Sell 6 strawberries
                orders_R.append(Order('ROSES', best_ask_R, - best_ask_amount_R)) # I Sell 1 rose

            elif best_bid_GB > ratio_long * acceptable_price_long_GB:
                orders_GB.append(Order('GIFT_BASKET', best_ask_GB, -best_ask_amount_GB)) # I Sell Gift Basket
                orders_C.append(Order('CHOCOLATE', best_bid_C, - best_bid_amount_C)) # I Buy 4 chocolates
                orders_S.append(Order('STRAWBERRIES', best_bid_S, - best_bid_amount_S)) # I Buy 6 strawberries
                orders_R.append(Order('ROSES', best_bid_R, - best_bid_amount_R)) # I Buy 1 rose
            

            elif best_ask_C < ratio_short * acceptable_price_short_C:
                orders_C.append(Order('CHOCOLATE', best_bid_C, -best_bid_amount_C)) # I Buy Chocolate
                orders_GB.append(Order('GIFT_BASKET', best_ask_GB, - best_ask_amount_GB)) # I Sell Gift Basket
                orders_S.append(Order('STRAWBERRIES', best_bid_S, - best_bid_amount_S)) # I Buy 6 strawberries
                orders_R.append(Order('ROSES', best_bid_R, - best_bid_amount_R)) # I Buy 1 rose
            
            elif best_bid_C > ratio_long * acceptable_price_long_C:
                orders_C.append(Order('CHOCOLATE', best_ask_C, -best_ask_amount_C)) # I Sell Chocolate
                orders_GB.append(Order('GIFT_BASKET', best_bid_GB, - best_bid_amount_GB)) # I Buy Gift Basket
                orders_S.append(Order('STRAWBERRIES', best_ask_S, - best_ask_amount_S)) # I Sell 6 strawberries
                orders_R.append(Order('ROSES', best_ask_R, - best_ask_amount_R)) # I Sell 1 rose
            

            elif best_ask_S < ratio_short * acceptable_price_short_S:
                orders_S.append(Order('STRAWBERRIES', best_bid_S, -best_bid_amount_S)) # I Buy Strawberries
                orders_GB.append(Order('GIFT_BASKET', best_ask_GB, - best_ask_amount_GB)) # I Sell Gift Basket
                orders_C.append(Order('CHOCOLATE', best_bid_C, - best_bid_amount_C)) # I Buy 4 chocolates
                orders_R.append(Order('ROSES', best_bid_R, - best_bid_amount_R)) # I Buy 1 rose
            
            elif best_bid_S > ratio_long * acceptable_price_long_S:
                orders_S.append(Order('STRAWBERRIES', best_ask_S, -best_ask_amount_S)) # I Sell Strawberries
                orders_GB.append(Order('GIFT_BASKET', best_bid_GB, - best_bid_amount_GB)) # I Buy Gift Basket
                orders_C.append(Order('CHOCOLATE', best_ask_C, -best_ask_amount_C)) # I Sell 4 chocolates
                orders_R.append(Order('ROSES', best_ask_R, - best_ask_amount_R)) # I Sell 1 rose


            elif best_ask_R < ratio_short * acceptable_price_short_R:
                orders_R.append(Order('ROSES', best_bid_R, -best_bid_amount_R)) # I Buy Roses
                orders_GB.append(Order('GIFT_BASKET', best_ask_GB, - best_ask_amount_GB)) # I Sell Gift Basket
                orders_C.append(Order('CHOCOLATE', best_bid_C, - best_bid_amount_R)) # I Buy 4 chocolates
                orders_S.append(Order('STRAWBERRIES', best_bid_S, - best_bid_amount_S)) # I Buy 6 strawberries
            
            elif best_bid_R > ratio_long * acceptable_price_long_R:
                orders_R.append(Order('ROSES', best_ask_R, -best_ask_amount_R)) # I Sell Roses
                orders_GB.append(Order('GIFT_BASKET', best_bid_GB, - best_bid_amount_GB)) # I Buy Gift Basket
                orders_C.append(Order('CHOCOLATE', best_ask_C, - best_ask_amount_C)) # I Sell 4 chocolates
                orders_S.append(Order('STRAWBERRIES', best_ask_S, - best_ask_amount_S)) # I Sell 6 strawberries
            
            result['GIFT_BASKET'] = orders_GB
            result['CHOCOLATE'] = orders_C
            result['STRAWBERRIES'] = orders_S
            result['ROSES'] = orders_R

            traderData = 'sample'



        return result, 1, traderData

