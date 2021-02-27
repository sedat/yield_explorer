# Introduction

## Yield explorer is a WIP!

I needed a tool that would show me historical data and performance of my staked crypto but was unable to find a tool that I liked. I was finding my self going to [yieldwatch](https://yieldwatch.net/)
a couple of times during the day and this wasn't cool because it was only showing me information on my stake at that particular time. There wasn't any historical data that would be charted, analyzed
, or show the increase/decrease of the performance in percentage in daily-weekly times etc. I thought that rather than going to yieldwatch every hour or so, let me write a code to automate this.
Not only it would show me what's up with my investment at a particular time. It would save the data in the database so that I can have historical data on my investment as well.
Please feel free to use this. But don't send many requests because that wouldn't be nice to the folks at yieldwatch. I send one request every hour.

## What to come

I'm thinking about adding a frontend to the project that would automatically fetch the current data from the database and show it to me in charts and other visual forms. Like a portfolio.

## How to use

Add your wallet address, deposit, and AAM provider as environment variables like

```
export WALLET_ADDRESS=<crypto wallet address>
export DEPOSIT=300 (as in 300 dollars, every time you buy more you should update this to figure out if you're losing or not)
export PROVIDER=<provider>
```
Options for provider, currently supporting only one provider at a time.
"Acryptos", "Autofarm", "StreetSwap", "PancakeSwap", "BeefyFinance", "Jetfuel", "CreamFinance", "Venus", "bDollar"

Install the required dependencies such as `requests, schedule` etc.

Run the `database.py` script to initialize the `yield_db`(create this before) database.
You can then run the `yield_explorer.py` script's `main` method to get the current information on your investment. This will print out the information and also save it in the database.
If you like to you can run a cron job every hour using the `cron.py` script. I use pm2 tool to run my processes automatically in my server.
