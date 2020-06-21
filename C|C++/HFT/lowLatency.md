## Low Latency

### [\*] Basic Requirement 
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
* Special hardwares - FPGA , ASIC

### Latency Reduction Techniques
* Proximity & Co-location
* WAN Route optimsation
* Os kernel-bypass NICs
* Low latency networking
* Application level, low latency

### Types of Latency

* Network Latency
  * Inter-server latency
  * Latency b/w discrete network components
    * Servers, switches, routers, firewalls etc

* Application Latency
  * Intra-server latency
  * Latency b/w software components within a server
    * Processes, threads, functions, code blocks

### Latency Numbers
| Request                            | latency time    | comparison										 			|
|:-----------------------------------|:----------------|:-----------------------------------| 
| L1 cache reference                 |          0.5 ns |															 			|
| Branch mispredict                  |          5   ns |															 			|			
| L2 cache reference                 |          7   ns | 14x L1 cache									 			|				
| Mutex lock/unlock                  |         25   ns |															 			|			
| Main memory reference              |        100   ns | 20x L2 cache, 200x L1 cache 	 			|
| Round trip within same datacenter  |    500,000   ns | 500 us												 			|				
| disk seek                          | 10,000,000   ns | 10 ms  20x datacenter roundtrip	  |

