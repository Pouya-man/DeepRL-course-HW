# Question #
Implement value iteration for the **gambler’s problem** and solve it for ph = 0.25 and ph = 0.55. In programming, you may ﬁnd it convenient to introduce two dummy states corresponding to termination with capital of 0 and 100, giving them values of 0 and 1 respectively. Show your results graphically, as in Figure 4.3. Are your results stable as θ→0?


## gambler’s problem ##

A gambler is presented with the possibility of engaging in wagers concerning the results of a series of coin tosses. If the coin comes up heads, he wins as many dollars as he has staked on that flip; if it is tails, he loses his stake. The game ends when the gambler wins by reaching his goal of $n (E.G. $100) or loses by running out of money. On each flip, the gambler must decide what portion of his capital to stake, in integer numbers of dollars. This problem can be formulated as an undiscounted, episodic, finite MDP.
