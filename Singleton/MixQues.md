C++ :
 - OOPS
 - reference
	* something like a pointer.
 - memory allocators
	* new is wrapper over malloc
	* malloc works by gettting continous block of memory (of specified size) from the heap, when the program runs depending on OS, it assigns some heap to it, if the requirement exceeds that then **sbrk** system call is used to get more memory from OS, if malloc asks for more memory than reqd to avoid future sbrk calls.
    * Before calling syscall, malloc checks if memory is available in the free-store.
    * sbrk/brk (now mmap is used) works by simple increasing the break address of heap in the data segment (stack <-> heap<-> data <-> text, as store in memory)
        - malloc then creates a header/footer around memory block returned by sbrk/brk with size/permission next/prev node pointer.
        - brk(10):set end of data segment to 10.
        - sbrk(10): increment data segment by 10.
    * For assigning huge memory(128Kb etc) instead of sbrk it uses mmap
    * How free works?  
        - free doesn't actually return memory to OS, rather store it in a free-store for future requirements.
        - It also ensures that there are no gaps in the heap memory(if you return a heap object residing in middle)
        - free also tries to merge adjacent memory blocks in the free store(free block is just circular link list with headers, headers take up some size too)
 - Template and generic programming
	* Resolved at compile time by the compiler, it creates seperate function instance for every type.
	* Since done at compile time can also be used to pass constant values
```bash
template<int N>
class A{
	int a[N];
	static int get_size()	{	return N;	}
}
int main()	{
	A<5> a;	
	a.get_size();	// returns 5
}
```
 - SFINAE
	* Substitution failure is not an erro
	*  related to template programming when substituting values, something like when using specialised templating if type-deducing fails it's discarded instead of throwing compile time error.
 - exceptions
	* Makes code simpler,readable etc
	* Helps in segregating normal-code and abnormalities
	* Guess, how would you feel handling errors in constructor calls.
	* Exceptions should always be caught by references

 - move semantics
	* std::move
	* Used to transfer ownership of objects
	* Always called on r-values reference and never on l-values.
	* Helps in avoiding un-necessary copies
 - std::forward:
	* Returns an rvalue reference to arg if arg is not an lvalue reference,if arg is an lvalue reference, the function returns arg without modifying its type.
- std::forward vs std::move: 
	* std::move takes an object and casts it as an rvalue reference, which indicates that resources can be "stolen" from this object.
	* std::forward has a single use case: to cast a templated function parameter of type forwarding reference (T&&) to the value category (lvalue or rvalue) the caller used to pass it. This allows rvalue arguments to be passed on as rvalues, and lvalues to be passed on as lvalues. This scheme is known as perfect forwarding.

 - compilation process : 
	1. pre-procesing 
	2. Compiling
	3. Assembly
	4. Linking
 - polymorphims internals in C++ 
	* It uses vtable and vptr to store which function to call from which object.
 - functors
	* class object which can be used as function pointers), ex: overloading **operator()** is a functor
 - lambda:
	* Sugar around functors
 - atomic:
	* std::atomic tries to convert the variable/object into atomic type(depending on platform), there can never be race condtn b/w 2 atomic objects.
 - how std::thread internally works OR how does pthread(c-level) works ?
	* In linux both pthread and fork uses same syscall *clone()* diff is that pthread ensures that both process use the same memory mapping. for syncronisatio pthread relies on futexes (which are user-space fast locking mechanisms via syscall for locking/semaphore etc)
 - auto works ?
	* The compiler simply deduce the types.
 - RAII
	* Resource allocation is initialisation
	* Basically if any object goes out of scope, it's destructor will be called.
 - dangling pointer:
	* A pointer which points to a memory location which is already deleted.
 - async/callback
	* Internally can be made using function/lambda/function pointer.
 - smart pointers:
	* https://github.com/HarshitKhurana/Extras/blob/master/C%7CC%2B%2B/SmartPointers.md
 - virtual functions (and default parameter to them), constructor/destructor ordering, virtual destructor
	* To call child class function in case of inheritance 
	* Uses vptable(per class) and vptr(per object) for storing which function should be called from which object.
	* destructor should be virtual bcoz if it's not then we might miss resource-cleaning in child object's destructiion(stored in base class pointer)
	* virtua constructor doesn't make any sense, bcoz constructor creates the object.
 - decltype vs auto
	* decltype: gives declared type of expression passed to it(no need to write & for references)
	* auto : simply for type deduction(need to write & for references)
 - thread safety in C++
	* use mutex
	* avoid global and static
 - override ? final ? diff b/w the two.
	* override: This keyword specifies that this function will over-ride parent class function.
	* final: This keyword specifies that this function cannot be over-rided by any child.
 - perfect-forwarding function ?
	* function template can pass its arguments through to another function whilst retaining the lvalue/rvalue nature of the function arguments by using std::forward. This is called "perfect forwarding", avoids excessive copying, and avoids the template author having to write multiple overloads for lvalue and rvalue references.
 - placement new ?
	* Simply pre-allocation of memory to speed up process.
 - dynamic cast vs static cast ? dynamic_cast in slow
	* static_cast: when you know types 
	* dynamic_cast: when you don't know types but still want to convert.
		* It is slow bcoz it needs to verify the types at run-time.

OS: 
- hyperThreading:
    * It is a process where a CPU splits each of its physical cores into virtual cores, which are known as threads, Hyper-Threading allows each core to do two things simultaneously. It increases CPU performance by improving the processor’s efficiency.
    * Use cpu_affinity to specify process on cpu core, otherwise cpu might context switch 
- cpu_affinity:
    * Improves cache performance, if multiple threads access same memory then better to put them on same cpu. 
 - epoll
    * linux syscall/API to monitor multiple FD's for any I/O activity, uses O(1) time (poll/select/kqueue uses O(n)), by simply storing the FD on which the event occur.
    * Supports level and edge triggered(read till epoll_wait() is called, next time starts from next data, prev data might not be read).
    * Dis-adv:
        * Needs more memory to prove O(1) lookup
 - user-space vs kernel-space
    * User-space: system memory where user space processes run
    * kernel-space: system memory where kernel processes run(init,memory management etc)
    * syscalls are used as interface to call kernel-level functionality from user-space.
 - syscalls , diff and how do they work ?
    * fork: Creates copy of the entire process with same memory layout with COW(copy-on-write) i.e memory layout changes as valeus differ b/w 2 processes.
    * vfork: same as fork(now), earlier fork() use to copy entire memory so vfork was created. it did so by sharing the same process address-space the stack-pointer etc was shared and the execution of parent was put on hold untill child calls *exec()* or *_exit()*
    * clone: Creates a new child process (fork/vfork all call this syscall now) with various parameters, it can create child process in same as well as other memory address-space
    * exec: Reset all memory, loads new binary, setup it's stack and passes control to new entrypoint of new executable.
 - Explain, down to the _hardware level_ what is a SIGSEGV, what causes it, how is it generated, etc.  
    * interrupt handling (interrupts triggered by CPU) from kernel space (bcoz thats where all the checks are done)
 - Signals:
    * signal is an asynchronous notification sent to a process or to a specific thread within the same process in order to notify it of an event that occurred
- multithreading
    * Being able to run multiple threads on a machine
 - cache, cache coherency , cache locality 
    - How does multi-core OS ensure their cache's are in sync ?
    * Each core has it's own L1 cache, for L2 cache they do dirty data of the entire cacheline if any part of that cacheline is modified (write back cache for sync)
    * The data in the cache is called dirty data , if it is modified within cache but not modified in main memory. Whereas,dirty bit (modify bit) is a cache line condition(status) identifier ,its purpose is to indicatewhether contents of a particular cache line are different to what is stored in operating memory.
- why signals slow? why context switching bad ?
    * generated from kernel space move all the way up to user-space.
    * context switching is slow bcoz the entire process table needs to be swapped into the memory, which also flushes the TLB
- semaphore vs mutex vs conditional variable:  https://github.com/HarshitKhurana/Extras/blob/master/OperatingSystem/Notes.md
- Memory management 
- segmentation, paging , page fault
- stack/heap , how much memory is pre-allocatted , sbrk syscall  malloc ? (malloc always allocates continous memory)
Note: In linux kernel you can over-commit, i.e you can ask for 8Gb ram on 4gb system and it will allocate bcoz of virtual memory ,
 (part of it will be used from RAM and rest from swap/paging), but when you try to access more than the free ram then the OS will need to kill 
other processes consumin ram  in order to make space for this process. (https://www.kernel.org/doc/Documentation/vm/overcommit-accounting)
- TLB:
    * It is a cache memory used to store page address of most recently used page table entries, if not in TLB and memory then page fault occurs and reqd page is swapped in and stored in TLB as well.
- process synchronisation
    * Use mutex/semaphores:
- thread migration:
    * Thread migration in operating system terminology actually means moving the thread from one core's run queue to another. This is done by the operating system scheduler (or libpthread scheduler in case of PTHREAD_SCOPE_PROCESS threads) to load balance the run queues of different cores available. This can be avoided by setting core affinity to the thread.
- kernel tuning for low latency & micro-second level timers
    * In linux, per cpu there is a migration daemon to do migration related stuff.
- instruction pipelining in CPU: 
    * Pipelining in its basic sense is running multiple instructions at the same time through the CPU at the same time.


Open Futures : 
Achieve Low latency: 
- Prefer not to context switch,  for locking use spin lock instead of sleeping 
- set cpu affinity
- set interrupt affinity
- isolate core from general OS (CPU pinning)
- multi-threading increase latency
- concurrency even on diff cores thrashes cpu cache above L1, memory bus, I/O
- AVOID these on hotpath:
  - shared_ptr etc which compromise performance for usability  (shared_ptr issues more memory reqd, checks thread safety )
  - exceptions
  - dynamic polymorphism
  - multiple inheritence (virtual functions)
  - dynamic memory allocation
- C++ exception if thrown can take more time , if not thrown improve performance
- virtual functions always means data cache miss bcoz it needs to load the vtable first, whereas instruction cache miss is independent of virtual,
 bcoz cpu may pick the function from cache which doesnt match with reqd function.
- number of threads = physical cores , seperate thread for business logic
- use lock free queues and busy spin to pass data b/w thread
- Memory barrier : Since CPU tries to everything parallely, A memory fence/barrier is a class of instructions that mean memory read/writes 
occur in the order you expect.
 For example a 'full fence' means all read/writes before the fence are comitted before those after the fence.

Imp:
- zero copy : socket programming:
    * "Zero-copy" describes computer operations in which the CPU does not perform the task of copying data from one memory area to another. This is frequently used to save CPU cycles and memory bandwidth when transmitting a file over a network. In socker programming generally our user space data buffer is copied to kernel space before being sent over wire and similarly for recieving which adds to latency.
- kernel bypass: solarflare/mellanox
    * The kernel bypass is when you manage yourself, in the user-space, the network stack and hardware stuff. It is hard, but you will gain a lot of performance (there is zero copy, since all the data are in the user-space). http://lukego.github.io/blog/2013/01/04/kernel-bypass-networking/
    * solarflare provides high performance user-space network stack.

- linux kernel parameter optimisation
    * using sysctl parameters such as 
        1. swapiness
        2. SHM_MAX(max size of single shared memory block)
        3. huge pages, 
        4. ASLR
        etc
- Huge pages:
    * Default linux page size is 4K (page = chunk of ram allocated to a process)
    * process with more memory requirement will require more pages
    * pages are stored in a page table for kernel to look-up
    * Huge pages helps in - faster lookup(small search space), less page fault, faster read/write 
        * Downsides:
            1. page fault takes more time
            2. more memory wasted
            3. more chances for fragmentation(not ennough continous memory available)
- fragmentation
    * Internal fragmentation: 10KB reqd but size available was 12KB , so 2KB internal fragmentation
    * External fragmentation: Although the amount of memory reqd is available but not available in contigous manner
        * Fix via : best-fit, worst-fit, good-fit
- paging vs segmentation
    * paging: 
        1. Fixed size   
        2. logical address can be contigoues without physical being cotinous
        3. use page number and offset to find page in page table.
    * Segmentation
        1. Variable size
        2. use segment number and offset to find segment in segment table.
- shared memory 
    * A common block of memory is shared b/w 2 processes for IPC, use spin_lock always for mutex.
    * mmap:
        - It maps files into memory (works via demand paging)
        - Used for allocating shared memory
    * shmset/shmget
- disruptor pattern:
    * Lock free alternative to exchange data b/w diff threads/processes in a producer-consumer manner without the use(traditional) of queue. 
    * Works on memory barrier: The processes will only access memory(pre-allocate) to the ring buffer
    * It uses ring buffer and counters (per ring-buffer for most recent write, per slot(buffer) inside ring for producer/consumer)
    * Each producer/consumer works on a sequencing for interaction with ring buffer.
    * Every write can be parallely consumed by all the consumers.    (no need to lock read-only data structures)
    * http://lmax-exchange.github.io/disruptor/files/Disruptor-1.0.pdf
    * https://news.ycombinator.com/item?id=12054503
    * https://softwareengineering.stackexchange.com/questions/244826/can-someone-explain-in-simple-terms-what-is-the-disruptor-pattern
- multicast internals
    * multicast is a way to send data from 1 sender to multiple recievers at the same time.
    * 2 or more services can listen on same multicast port.
    * A service subscribed to a multicast group, will recieve udpates from it.
    * PIM is a multicast protocol used for communication.
    * Each multicast Ip address is a unique group and only it's subscribers can listen to it.
- linux memory model
- NUMA:
    * non-uniform memory architecture
    * basically memory closer to cpu is much faster (L1, L2 and so on)

Networking: 
 - socket programming C++
    - how to get max performance from socket ?
 - buffer storing and flushing
    * data is sent as soon as send is called from sender (not gauranteed)
    * In reciever it only recieves the data once sufficient chunk(buffer size) of data is recieved.
    * NAGLE Algo: 
        * it combines the small data packets  in a bigger chunk size so as to reduce the overhead of sending multiple small size packets.
        * The Nagle algorithm only has an effect when a second write() call is made while the previous data is still unacknowledged. In the normal case, this data will be left buffered until either: a) there is no unacknowledged data; or b) enough data is available to dispatch a full-sized segment. The delay cannot be indefinite, since condition (a) must become true within the retransmit timeout or the connection dies.
    * TCP_NODELAY is used to disable the Nagle buffering algorithm. It should only be set for applications that send frequent small bursts of information without getting an immediate response, where timely delivery of data is required (the canonical example is mouse movements).
    
 - OSI model and TCP/IP model:
    * OSI:  
        1. Physical layer(Ethernet) : Bit-steam, topology, 
        2. Data Link layer(MAC address) : stream of bits=frames, Does Error/flow control  using header (physical address)
        3. Network Layer : Source to destination packet delivery b/w networks, adds header for logical addressing
        4. Trasport Layer : Process to process packet delivery, does segmentation and re-assembly of packet i.e deviding packet and assembling back using sequence number.
        5. Session Layer : syncronisation and checks (Ex: when downloading 1GB file, if breaks at 156MB, then continues from same)
        6. Presentation Layer  : Translation, Encryption, Compression 
        7. Application Layer : Provides access to n/w resources via UI.
    *  TCP:
        1. Physical & Data link layer
        2. Network Layer
        3. Transport Layer
        4. Application Layer
 - diff b/w tcp and udp , packet size and format
    * TCP - big packet size, error control, sequencing of packets, connection-oriented, slow speed bcoz of all pf this, 3way handshake, can't multicast/broadcast.
        1. Header: source port, destination port, length, seq number, ack number, flags, window, checksum ,UPTR, Padding, options 
        2. TCP header size = 20bytes
    * UDP - Opp of above , can't check packet loss, no congestion/flow control
        1. Header: source port, destination port, length, checksum , data
        2. UDP headaer size: 8 bytes
 - How does a packet reaches from hardware to application program or how recv syscall works ?
    1. Packet arrives at ring buffer in Network Card.
    2. NIC Hard Interrupts(hard bcoz triggered by hardware), kernel stops a running process, and context switches(store it's state, build new stack etc) .
    3. Kernel runs an Interrupt Handler to turn the interrupt off.
    4. Kernel schedules the SoftIRQ(software interrupt handler) to do the actual recieve.
    5. Then the packet is moved through the protocol stack for getting the actual data.
    6. Then the actual data payload is stored in the application buffer, which is then recieved by application using the recv() syscall.
    7. The SoftIRQ continues NAPI polling(NIC polling) untill data is there.
 - What does it mean to have 10Gig NIC ?
    * It means that there are multiple queues(ideally 1 per h/w cpu not hyperthread) inside the NIC, for huge recv power.
