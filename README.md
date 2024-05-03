# For this IMC Prosperity 2 Competition, we had a group of Wissal (France) and Oscar (Spain) from the University of Washington.

## Algo Rounds
**For the algo round 1:**
We had two assets, The first asset, Amethyst, demonstrated a relatively stable price range, oscillating around a mean of approximately 10,000 Seashells. The asset's price fluctuated between a high of 10,005 Seashells and a low of 9,995 Seashells. This narrow price range indicated low volatility, but there were noticeable clusters of volatility that presented potential profit opportunities. However, the lack of a robust data storage framework prevented us from fully capitalizing on these fluctuations. 
For the second asset, Seafruit, our initial strategy was to engage in either trend-following or market-making around the price oscillations. Trend-following would have involved identifying and capitalizing on the directions of price movements, whereas market-making would have focused on capturing the spread between buy and sell prices during oscillations. Similar to our experience with Amethyst, the absence of a comprehensive data storage framework restricted our ability to deploy these strategies effectively.
We then decided to trade Amethyst by simply market-making and stay away from Starfruit.
We made a mediocre but very consistent return of 12,956 Seashells.

**For algo round 2:**

The second round introduced a new asset, Orchids, which presented a more complex set of variables influencing its price dynamics, including Shipping Costs, Export and Import Tariffs, Sunlight, and Humidity. This round tested our ability to integrate and analyze multiple data streams in our trading strategy. Building on the lessons from the first round, we developed a simple yet effective data storage framework. This allowed us to maintain and access historical data relevant to the factors influencing Orchids' prices. We utilized linear regression analysis to predict price movements based on the stored data, focusing on whether to buy or sell the asset.
This worked very consistently and we were able to secure 6,686 Seashells.

**For algo round 3:**

The third round of the competition introduced a complex asset called the Gift Basket, which consisted of 4 Chocolates, 6 Strawberries, and a Rose. This round allowed us to trade all four components of the basket as individual assets as well as the basket itself as a combined asset. The Gift Basket's value was calculated based on the weighted sum of the prices of its individual components plus a calculated premium:
$$p_{GB} = 4 p_{C} + 6p_{S} + p_{R} + {premium} $$
This premium was derived from analyzing past data to determine how much extra customers were willing to pay for the convenience and appeal of a pre-assembled basket. Realizing the potential of our past data, we extended our pricing strategy to include market-making based on the relative costs of individual assets. Specifically, we identified opportunities to buy or sell individual items based on their comparison to the combined prices of other items. This method allowed us to exploit pricing inefficiencies within the market.

This advanced strategy led to significant profits. By dynamically adjusting our prices based on detailed historical analysis and current market conditions, we capitalized on slight price variations among the assets, culminating in a total profit of 70,356 Seashells for the round. Nonetheless, this strategy yielded more volatile returns which still behaved like a stationary time series with a positive mean and a Gaussian wave noise. 

**For algo round 4:**

In the penultimate round of the competition, we traded coconuts along with coconut coupons, which functioned similarly to options on coconuts with a 250-day expiration and a strike price of 10,000 Seashells. Building on the successful strategy from round three, we adopted a similar approach to estimate the expected option price using the Black-Scholes model, enhanced by an additional premium, to set the coupon price.
Initially, we explored more complex option pricing models and attempted to leverage the implied price derived from Black-Scholes for additional trades. However, these advanced methods introduced significant complexity, resulting in less stable code when implementing numerical methods, and they underperformed according to past data analysis. Consequently, we shifted our focus back to a simpler, more robust strategy, choosing to market-make using the Black-Scholes model exclusively.

This streamlined approach resulted in a profit of 68,069 Seashells, mirroring the successful outcomes of round three. Despite the similar financial performance, this round's strategy was characterized by a consistent application of a proven mathematical model, emphasizing stability and reliability over the incorporation of more sophisticated, yet less effective, methodologies.

**For algo round 5:**

The final round of the competition presented a unique opportunity to trade all assets with the additional insight of having access to historical data on other traders' transactions and timings. This scenario was expected to allow for potentially high returns, albeit with a corresponding risk of significant losses for some participants.
During this round, we experimented with various strategies aimed at capitalizing on the actions of other traders. Despite our efforts, we were unable to identify a single strategy that consistently yielded large returns, due to the complexities involved, including tracking the specific periods when trades occurred.
Ultimately, we decided to integrate all the successful strategies we had developed in previous rounds. This comprehensive approach combined market making, data-driven pricing adjustments, and strategic buys and sells based on predictive analytics. By leveraging our cumulative knowledge and experience, we were able to adapt dynamically to the market conditions and other traders’ behaviors.
This integrated strategy proved effective, resulting in a substantial profit of 79,979 Seashells. This round not only tested our ability to synthesize and apply diverse trading strategies but also highlighted the importance of adaptability and comprehensive analysis in achieving success in a complex trading environment.


## Now for the manual rounds:

**Manual Round 1**

In the first manual round of the competition, participants were engaged in an auction setting, where the probability distribution of the reserve prices was known beforehand. Initially, we believed the auction participation would be a singular event, prompting us to strategize our bidding process accordingly. Our first bid was calculated to have a 65% chance of success, and if necessary, a follow-up bid was set to increase the likelihood to 90%.
However, the competition structure revealed that there were thousands of such auctions to participate in, significantly altering the dynamics we had anticipated. This unexpected volume of auctions impacted our ability to manage and adapt our bidding strategy efficiently across so many instances.
As a result of this miscalculation and the scale of participation required, our returns were affected, culminating in a profit of 77,100 Seashells. This round highlighted the challenges of scaling a strategy effectively when faced with higher-than-expected operational demands and provided key insights into adapting strategies under varying competitive conditions.

**Manual Round 2**

The second round presented a complex challenge involving an unbalanced FX matrix (but with paired assets). Participants were tasked with buying and selling different asset pairs within this matrix. By effectively analyzing the discrepancies and imbalances within the pairs matrix, we were able to execute a series of trades that capitalized on these arbitrage opportunities. This strategic trading within the unbalanced matrix resulted in a substantial profit of 113,938 Seashells

**Manual Round 3**

The third round introduced a strategic challenge involving a map of various locations, each offering different potential payoffs. The complexity of this round was heightened by the dynamic that the number of traders selecting a particular location would affect the payout, as the total payoff for each location was divided among the traders present there.
To navigate this setup, we employed a layered analysis strategy to anticipate where rational traders might congregate, considering how deeply they analyzed potential outcomes. This predictive approach allowed us to strategically choose up to three locations, although selecting additional locations incurred a fee.
Ultimately, we opted for some of the most promising locations based on our analysis. This decision resulted in securing 77,938 Seashells. However, a retrospective evaluation revealed that avoiding the selection of a third location would have saved the fee and increased our profits by an additional 15,000 Seashells.

**Manual Round 4**

The fourth round was a continuation of the first, introducing an additional complexity: the probability density function (PDF) of the auction's reserve prices was now influenced by the choices of other traders. This dynamic change required an adaptation of our previous strategy to remain competitive.
Building on the layered analytical approach from earlier rounds, we continued to evaluate the likely choices of other traders to determine the optimal bidding strategy. We aimed to set our bids to maximize profit, incorporating an extra margin to our calculations, which ultimately had a negligible impact on the payoff but ensured we remained on the safer side of bid optimization.
This strategic refinement allowed us to place what turned out to be the exact optimal bids under the evolved conditions. As a result, we secured a profit of 102,212 Seashells. This round not only tested our ability to adapt and refine our strategies in response to changing market conditions but also highlighted the efficacy of our analytical approach in predicting and capitalizing on optimal economic behaviors.

**Manual Round 5**

The fifth round of the competition mimicked a stock-picking environment, where decisions to buy and sell various assets were primarily influenced by news related to them. In this round, the absence of quantitative data for prediction necessitated a reliance on intuitive, "common sense" judgments to make trading decisions.
Mindful of the investing fee that increased with the total amount invested—a lesson reinforced by our experience in the third round—we strategically limited our investment to optimize returns while mitigating fee impact. This cautious approach proved beneficial, although we encountered two out of nine positions with a negative profit and loss (P&L), attributable to the fees. Notably, these positions were directionally correct, underscoring the soundness of our market interpretations.
Our strategy of setting prudent investment limits enabled us to secure a profit of 69,727 Seashells in this final round. This outcome demonstrated our improved ability to balance investment aggressiveness with risk management, culminating in a successful conclusion to the competition
