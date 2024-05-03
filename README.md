For this IMC Prosperity 2 Competition, we had a group of Wissal and Oscar.
We will first explain the algorithmic rounds and then the manual rounds.

For the algo round 1:
We had two assets, The first asset, Amethyst, demonstrated a relatively stable price range, oscillating around a mean of approximately 10,000 Seashells. The asset's price fluctuated between a high of 10,005 Seashells and a low of 9,995 Seashells. This narrow price range indicated low volatility, but there were noticeable clusters of volatility that presented potential profit opportunities. However, the lack of a robust data storage framework prevented us from fully capitalizing on these fluctuations. 
For the second asset, Seafruit, our initial strategy was to engage in either trend-following or market-making around the price oscillations. Trend-following would have involved identifying and capitalizing on the directions of price movements, whereas market-making would have focused on capturing the spread between buy and sell prices during oscillations. Similar to our experience with Amethyst, the absence of a comprehensive data storage framework restricted our ability to deploy these strategies effectively.
We then decided to trade Amethyst by simply market-making and stay away from Starfruit.
We made a mediocre but very consistent return of 12,956 Seashells.

For algo round 2:
The second round introduced a new asset, Orchids, which presented a more complex set of variables influencing its price dynamics, including Shipping Costs, Export and Import Tariffs, Sunlight, and Humidity. This round tested our ability to integrate and analyze multiple data streams in our trading strategy. Building on the lessons from the first round, we developed a simple yet effective data storage framework. This allowed us to maintain and access historical data relevant to the factors influencing Orchids' prices. We utilized linear regression analysis to predict price movements based on the stored data, focusing on whether to buy or sell the asset.
This worked very consistently and we were able to secure 6,686 Seashells.

For algo round 3:
The third round of the competition introduced a complex asset called the Gift Basket, which consisted of 4 Chocolates, 6 Strawberries, and a Rose. This round allowed us to trade all four components of the basket as individual assets as well as the basket itself as a combined asset. The Gift Basket's value was calculated based on the weighted sum of the prices of its individual components plus a calculated premium:
$$p_{GB} = 4 p_{C} + 6p_{S} + p_{R} + {premium} $$
This premium was derived from analyzing past data to determine how much extra customers were willing to pay for the convenience and appeal of a pre-assembled basket.Realizing the potential of our past data, we extended our pricing strategy to include market-making based on the relative costs of individual assets. Specifically, we identified opportunities to buy or sell individual items based on their comparison to the combined prices of other items. This method allowed us to exploit pricing inefficiencies within the market.

This advanced strategy led to significant profits. By dynamically adjusting our prices based on detailed historical analysis and current market conditions, we capitalized on slight price variations among the assets, culminating in a total profit of 70,356 Seashells for the round. Nonetheless, this strategy yielded more volatile returns which still behaved like a stationary time series with a positive mean and a Gaussian wave noise. 

For algo round 4:
In the penultimate round of the competition, we traded coconuts along with coconut coupons, which functioned similarly to options on coconuts with a 250-day expiration and a strike price of 10,000 Seashells. Building on the successful strategy from round three, we adopted a similar approach to estimate the expected option price using the Black-Scholes model, enhanced by an additional premium, to set the coupon price.
Initially, we explored more complex option pricing models and attempted to leverage the implied price derived from Black-Scholes for additional trades. However, these advanced methods introduced significant complexity, resulting in less stable code when implementing numerical methods, and they underperformed according to past data analysis. Consequently, we shifted our focus back to a simpler, more robust strategy, choosing to market-make using the Black-Scholes model exclusively.
This streamlined approach resulted in a profit of 68,069 Seashells, mirroring the successful outcomes of round three. Despite the similar financial performance, this round's strategy was characterized by a consistent application of a proven mathematical model, emphasizing stability and reliability over the incorporation of more sophisticated, yet less effective, methodologies.

