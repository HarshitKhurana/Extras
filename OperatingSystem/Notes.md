### [\*] Notes

* List of some simple points & QnA's.

1. Stack grows downwards.
2. When the program starts, the OS initially allocates some heap space to it, and after that as per the requirements the OS allocates it more and more heap space depending on the `malloc/calloc/new` call, (this call future heap memory requirements adds to the latency - `sbrk` syscall).

</br>
</br>

**Ques 1:** Difference between CPU Cache and TLB(Translation Lookaside Buffers) ? </br>
**Ans :**  
**1. CPU Cache** is the fastest accessible memory which reduces the latency for fetching from RAM , and provides some storage in CPU registers itself.
  * I-Cache : CPU Cache used to store instruction.
  * D-Cache : CPU Cache used to store Data.
    * D-cache is further categorised as L1 D-cache, L2 D-cache ,L3 D-cache etc.
    * Speed of fetching and cost of the hardware for that type of cache is as : `L1` > `L2` > `L3`
  * 1 cache miss results in fetching from a slower version of memory/cache, which adds to latency.

**2. TLB (Translation lookaside buffers)** : These are used to speed up the translation of virtual address to physical address by storing page-table in faster memory(RAM only).
  * Only required if the OS uses the concept of virtual memory.(Almost all OS does use virtual memory - Linux does for sure).
  * TLB is used by MMU (Memory Management Unit) when physical address is needed to be translated to virtual address (uses page table).
  * It simply acts as a cache for page-table.
  * Note : Page table (stored in RAM) keeps track of where virtual pages are stoed in physical memory. (Swapping time) So if a process does context switching then the TLB is flushed and when the kernel does context switching again and re-load that process the it's TLB is again formed from the page-table (which is always up-to-date.)

* **Difference :** 
  * TLB : Speeds up the process of address translation for virtual memory. : speeds up RAM access time.
  * CPU Cache : It stores some part of data on CPU itself so that it doesn't have to query RAM.

</br>
</br>

**Ques 2:** Difference between spinlock , mutex , semaphore and conditional variables.</br>
**Ans :**  All three of them are used for process syncronisation :

**1. Mutex :** For mutual exclustion , it allows multiple programs/threads to access a common resource 1 at a time.
  * It is a locking mechanism.
  * A process/thread acquires a mutex lock on an object before using it and once used , it releases the lock.
  * If a process requires a resource which is currently been locked by other resource then the process which requires the lock waits and is queued by the system untill the mutex object is unlocked.
  * Dis-adv : When a mutex is already locked and the process needs it , then the process is queued by the OS and we cannot exactly determine when will the OS schedule it and it will be executed.

**2. Semaphore :** It typically uses an integer variable 'S' initialised with number of resources present.
  * It is a signalling mechanism.
  * The value of semaphore can be modified either via `wait() (decrements the value)` or `signal() (increments the value)` after initialised.
  * Semaphore could be `binary` or `Counting` depending upon the resource availability.
  * Both `wait()` and `signal()` are atomic instructions.

**3. Spinlock :** It is a lock which causes a thread trying to acquire it to simply wait in a loop("spin") while repeatedly checking if the lock is available.
  * It is a basically a mechanism for busy-waiting.
  * The thread which waits for it makes sure that no other thread acquires it before this thread does , but the OS could still context switch it once the CPU runtime quantum for current thread is exceeded(for round robin scheduling).
  * Don't use spinlocks on single core as it's obv waste.
  * It uses atomic instructions.

> **Note :** Use mutex when the waiting time is not very less as in that case the time to put thread/process to sleep and wake it up will be much more as these are exxpensive operation , whereas the waiting time is very less it's better to use spinlock and poll for the resource though it would waste some CPU cycles but the entire execution would still take lesser time than using mutex and sending process to sleep and then waking it up eventually.

**3. Conditional Variable :** It is a high-level form of syncronisation which combines *locking* and *signalling* mechanisms.
  * It is a synchronization primitive that can be used to block a thread, or multiple threads at the same time, until another thread both modifies a shared variable (the condition), and notifies the `condition_variable`.
  * It requires a mutex for it's implementation.
  * It also should signal to modify the `conditional_variable`.

</br>
</br>

**Ques 3:** Note on Cache friendly code . </br>
**Ans :** Cache friendly code in simpler terms means writing code in which accessing the data is present in the cache itself and doesn't have to query andy upper level memory/cache, which would increase the latency i.e if the code is running in CPU and the data to access is present in L1 cache it's best else it will query L2 cache, then L3 and so on and correspondingly the latency will also increase.
  * An imp. aspect of Cache friendly code is *Principle of Locality* (It is the tendency of a processor to access the same set of memory locations repetitively over a short period of time) :
  * 2 Types of locality : 


  **1. Temporal locality:** when a given memory location was accessed, it is likely that the same location is accessed again in the near future. Ideally, this information will still be cached at that point.
</br>
  **2. Spatial locality:** this refers to placing related data close to each other. Caching happens on many levels, not just in the CPU. For example, when you read from RAM, typically a larger chunk of memory is fetched than what was specifically asked for because very often the program will require that data soon. HDD caches follow the same line of thought. Specifically for CPU caches, the notion of cache lines is important.
  * **Cache Lines :** These are the unit of data transfered between the main memory and the cache.
    * Usually the size of cache line is 64bits i.e 8bytes for modern systems.

  * Virtual functions in C++ induces cache misses during look up if the specific funciton in not called often (else it would already be cached)

</br>
</br>
