### [\*] Notes

* List of some simple points & QnA's.

1. Stack grows downwards.
2. When the program starts, the OS initially allocates some heap space to it, and after that as per the requirements the OS allocates it more and more heap space depending on the `malloc/calloc/new` call, (this call future heap memory requirements adds to the latency - `sbrk` syscall).

**Ques 2:** Difference between CPU Cache and TLB(Translation Lookaside Buffers) ?
**Ans :**  
1. **CPU Cache** is the fastest accessible memory which reduces the latency for fetching from RAM , and provides some storage in CPU registers itself.
  * I-Cache : CPU Cache used to store instruction.
  * D-Cache : CPU Cache used to store Data.
    * D-cache is further categorised as L1 D-cache, L2 D-cache etc.

2. **TLB (Translation lookaside buffers)** : These are used to speed up the translation of virtual address to physical address by storing page-table in faster memory(RAM only).
  * Only required if the OS uses the concept of virtual memory.(Almost all OS does use virtual memory - Linux does for sure).
  * TLB is used by MMU (Memory Management Unit) when physical address is needed to be translated to virtual address (uses page table).
  * It simply acts as a cache for page-table.
  * Note : Page table (stored in RAM) keeps track of where virtual pages are stoed in physical memory. (Swapping time) So if a process does context switching then the TLB is flushed and when the kernel does context switching again and re-load that process the it's TLB is again formed from the page-table (which is always up-to-date.)

* **Difference :** 
  * TLB : Speeds up the process of address translation for virtual memory. : speeds up RAM access time.
  * CPU Cache : It stores some part of data on CPU itself so that it doesn't have to query RAM.
