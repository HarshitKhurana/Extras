## [\*] Overview of Trading 
* Trading/HFT is a entirely secretive area. (No github nothing)
* **BUY LOW - SELL HIGH**

### [\*] Terminology
* Liquidity : In business, economics or investment, market liquidity is a market's feature whereby an individual or firm can quickly purchase or sell an asset without causing a drastic change in the asset's price. Liquidity is about how big the trade-off is between the speed of the sale and the price it can be sold for.
* Market Makers : Trading systems and companies which offers liquidity.
* Venues : Stock Exchanges (Ex: NYSE , NSE , chicago stock exchange etc)

### [\*] Categories - Investment Banking
| Front Office |
|:------------ |
|- Traders sit in diff rooms with multiple screens and fast dialler| 
|- Typical image that come into your mind when thinking of stock market (wolf of wall street kind).| 
|- Things are very fast-paced here (manual decsicion making)| 

| Middle Office |
|:------------  |
|- In this the people looks deeper into the stratergies to make money.| 
|- People here are  Accountants, Economists, Mathematicians and that kind.| 
|- Things are very a little slower here (much thinking process)| 

| Back Office |
|:------------|
|- Maintaining the daily ledger, cash movements of the day are aggregated etc.| 

### [\*] Trading Approaches
|Theory based Investment    |
|:--------------------------|
|- Know your investments.    |
|- Research and news driven. |
|- Longer term holdings.     |

| Data driven |
|:--------------------------|
|- Statistical and trend-driven.|
|- Can be very short term, even micro-seconds.  |

### [\*] Trading Stratergies
#### Arbitration : 
* Exploiting the difference in price for the same stock in different values.
* Very latency dependent.

#### Momentum : 
* Assume that the current trend will continue.

#### Aplha (pairs) : 
* Expecting 2 companies to have the similar momentum and if 1 goes down then it should be expected same from the other one.
* Based on fundamental macro-economics statistics.

#### Composites : 
* Arb a ETF by beating it's update. Ex: A 10% change in BP value on FTSE100 may translate into a 0.2% change in the overall index.
* Very much latency sensitive as on detecting a change in BP you would have to super-fast calculate what all will be effected by it and then update.

#### Market Making : 
* Accepting an Exchange fee to provide liquidity. (very very minimal)
* Typically large spread just outside current price.
* Objects is to make money ov volume and minimize holding.

### [\*] Buying Stratergies
#### Smart Order Routing : 
* Discover/Find which venue/exchange is offering the best price.

#### Iceberg : 
* Slice a large order up into smaller orders to disguise intent and reduce market impact.	(so that it doesn't effect the overall price).

#### Sweep Order : 
* Buy only a percentage of the desired quantity and wait/pause for more liquidity to be placed, hopefully at the same price.

### [\*] Trading Protocol
* Every venue/exchange may have a seperate format for messages for market data and for orders.
* Even if 2 venues are using the same protocol they still might have differences in customized feed handlers.
* Protocols : FIX , FAST, ITCH , QuickFIX (open-source)

### [\*] Basic Requirement From/For Techinical person
* Maths, C++ programming - The good you are , the better it is.
* Handson with low-latency, low jitter.
* Packet Processing - TCP , UDP , Multicast
* Destructor threads : spin waiting for packets to arrive to avoid interrupt wakeup delay
* Minimise lock contentation
* Nanosceonds timestamping
* Direct buffer management
* Allocate and pre-allocate everything before trading
* Minimise garbage collection to avoid jitter (specially java)
* Pinning memory, cache line alignment
* CPU isolation and affinity
* Memory map files when cannot be avoided
* Low-latency network programming
	* Kernel bypass, usually pre-load libraries
	* Kernel bypass, proprietary API's
	* RDMA :  Remote direct Memory Access
		1. Hardware enabled data transfer across network

