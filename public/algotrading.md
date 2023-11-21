
# Algorithmic Trading in Electric Short Term Power at EnBW Trading

The goals for the algo trading system are low decision and order latency and high throughput for [backtesting](https://de.wikipedia.org/wiki/Backtesting) .
The system is event driven and async. It has a live and a backtesting component. 
The live component is cloud-operated.
In 2024, we want to design and implement the backtesting for strategy validation and 
[hyperparameter search](https://en.wikipedia.org/wiki/Hyperparameter_optimization),
see also https://news.ycombinator.com/item?id=38120493

The job is full time for the first two quarters of 2024, with a possibility to extend the engagement.
The job is largely remote, see below. The range for compensation is 900€ to 1200€ per day.


# Requirements

* You know what energy and power is.
* You have an understanding of the wholesale markets for electrical power.
  These are 
  * auction based (once a day) [european power auction](https://www.epexspot.com/en/tradingproducts#day-ahead-trading) and 
  * limit order book based (continuous 24/7) [limit orderbook trading](https://en.wikipedia.org/wiki/Order_(exchange)#Limit_order)
* You are willing to understand our trading strategies.
* You have a firm understanding how calendar time is modelled in Rust (time offset, time zone).
* You work with git, issues, and pull requests.
* You write tests in units for business logic.
* Your language is German and English
* You are willing to spend, initially, two weeks at EnBW Headquarter in Karlsruhe
* You must be an EU citizen

# RESPONSIBILITIES

* Implement backtesting
  - Rust performance optimization
  - Research and setup Pipeline for compute and data management 
* Features
  - Implement feature requests (order placement, trading strategies) in close cooperation with front office (traders) 
* Maintain
  - Refactor Rust code
  - Operate compute on AWS
