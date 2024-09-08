# Questions #
In this exercise, we want to use importance sampling to calculate the probability that a random variable with normal distribution has a value greater than 5.
![image](https://github.com/user-attachments/assets/fdd6e02e-24c1-4490-95d0-459c880176ea)

A) Using the indicator function, we can rewrite the desired probability in the form of mathematical expectation:

![image](https://github.com/user-attachments/assets/96b0a86a-b3ef-4a2a-a4e6-54213660a6ed)

in which the mathematical expectation for the standard normal random variable is taken as:

![image](https://github.com/user-attachments/assets/5166702d-1554-45f3-bcb5-d31b42dd8a40)

In other words, we can approximate the value P(x > 5) with Monte Carlo method averaging:

![image](https://github.com/user-attachments/assets/bb05161b-19e6-480a-b8d2-6757181be462)

Explain why this method doesn't work.

