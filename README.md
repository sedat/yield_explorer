# Introduction

## Yield explorer is a WIP!

I needed a tool that would show me historical data and performance of my staked crypto but was unable to find a tool that I liked. I was finding my self going to [yieldwatch](https://yieldwatch.net/)
a couple of times during the day and this wasn't cool because it was only showing me information on my stake at that particular time. There wasn't any historical data that would be charted, analyzed
, or show the increase/decrease of the performance in percentage in daily-weekly times etc. I thought that rather than going to yieldwatch every hour or so, let me write a code to automate this.
Not only it would show me what's up with my investment at a particular time. It would save the data in the database so that I can have historical data on my investment as well. And with this data that I saved, I can use the frontend application to see my data in informational graphs.
Please feel free to use this. But don't send many requests because that wouldn't be nice to the folks at yieldwatch. I send one request every hour.

## What to come

The priority was to add a frontend that shows graphs of the data in the database. As of now I added this feature. In the future I plan to add enhancements to the frontend to shows a couple more graphs and some utilies. If you have an idea let me know. Also currently only Autofarm and PancakeSwap are tested. If you use any of the other providers below and it's not working correctly, let me know.

## How to use

Add your wallet address, deposit, and AAM provider as environment variables like

```
export WALLET_ADDRESS=<crypto wallet address>
export DEPOSIT=300 (as in 300 dollars, every time you buy more you should update this to figure out if you're losing or not)
export PROVIDER=<provider>
```
Options for provider, currently supporting only one provider at a time. If you use multiple providers, run the script for each of them.
"Acryptos", "Autofarm", "StreetSwap", "PancakeSwap", "BeefyFinance", "Jetfuel", "CreamFinance", "Venus", "bDollar"

Install the required dependencies such as `requests, schedule` etc.

Run the `database.py` script to initialize the `yield_db`(create this before) database.
You can then run the `yield_explorer.py` script's `main` method to get the current information on your investment. This will print out the information and also save it in the database.
If you like to you can run a cron job every hour using the `cron.py` script. I use pm2 tool to run my processes automatically in my server.

## How to use the frontend application

To run the frontend application you need to run both the server that takes the data from the database and the frontend application itself.

First you need to have `nodejs` and `npm` available in your system. You can look at it online.
First, go to the `backend` folder and run the command `npm install` to download all dependencies. After this change the mysql name and password in `app.js` according to your mysql credentials. Now you can run `npm run start` to start your server.

After starting your server go to the `frontend` folder. Like last time run the command `npm install`. After installing the dependencies you can run the command 
`npm run dev`. This command will open the frontend application in `http://localhost:5000/`. Use your browser to go to this URL and your graphs will be there.

### If you find this work useful you can tip me here BSC address: 0x878BC5bC7cBc369dffC00cdc6e1718478dc1D639. You can also contact me if you want a new feature.
