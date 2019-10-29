### [\*] syscall - CheatSheet
* Pre-req : <a href="./syscall.md">Linux Syscall</a>
* For **s**yscall **trac**ing - **strace**.

```bash
$ strace ./a.out
```
* This sheet doesn't contain all but some common syscalls. 
* Location of syscalls in Linux : `/usr/include/asm/unistd_32.h`

| syscall No.	| Func Name								 | Description																																	| 
|:----------- |:-------------------------|: ---------------------------------------------------------------------------:| 
|1.				    | exit 										 | terminate the current process 																								| 
|2.				    | fork 										 | create a child process 																											| 
|3.				    | read 										 | read from a file descriptor 																									| 
|4.				    | write 									 | write to a file descriptor 																									| 
|5.				    | open 										 | open a file or device 																												| 
|6.				    | close 									 | close a file descriptor 																											| 
|11. 			    | execve									 | execute program 																															| 
|14. 			    | mknod 									 | create a special or ordinary file 																						| 
|18. 			    | stat 										 | get file status 																															| 
|26. 			    | ptrace 									 | allows a parent process to control the execution of a child process					| 
|27. 			    | alarm 									 | set an alarm clock for delivery of a signal 																	| 
|28. 			    | fstat 									 | get file status 																															| 
|30. 			    | utime 									 | set file access and modification times 																			| 
|37. 			    | kill 	 									 | send signal to a process 																										| 
|41. 			    | dup  	 									 | duplicate an open file descriptor 																						| 
|42. 			    | pipe 										 | create an interprocess channel 																							| 
|43. 			    | times 									 | get process times 																														| 
|45. 			    | brk	 										 | change the amount of space allocated for the calling process's data segment 	| 
|48. 			    | sys\_signal 						 | ANSI C signal handling 																											| 
|54. 			    | ioctl 									 | control device 																															| 
|62. 			    | ustat										 | get file system statistics  						 																			| 
|63. 			    | dup2 										 | duplicate a file descriptor 						 																			| 
|64. 			    | getppid 								 | get parent process ID 							 																					| 								
|65. 			    | getpgrp 								 | get the process group ID  						 																				| 								
|66. 			    | setsid 									 | creates a session and sets the process group ID    													| 
|67. 			    | sigaction 							 | POSIX signal handling functions   				 																		| 
|68. 			    | sgetmask 								 | ANSI C signal handling 							 																				| 								
|69. 			    | ssetmask 								 | ANSI C signal handling 							 																				| 								
|75. 			    | setrlimit 							 | set maximum system resource con sumption  		 																| 
|76. 			    | getrlimit 							 | get maximum system resource con sumption  		 																| 
|77. 			    | getrusage 							 | get maximum system resource con sumption  		 																| 
|82. 			    | old_select 							 | sync. I/O multiplexing 		 					 																				| 
|83. 			    | symlink 								 | make a symbolic link to a file 					 																		| 
|84. 			    | lstat 									 | get file status 									 																						| 
|85. 			    | readlink 								 | read the contents of a symbolic link  			 																	| 
|90. 			    | old_mmap 								 | map pages of memory 								 																					| 
|91. 			    | munmap 									 | unmap pages of memory 		  					 																				| 
|96. 			    | getpriority 						 | get program scheduling priority 					 																		| 
|97. 			    | setpriority 						 | set program scheduling priority 					 																		| 
|99. 			    | statfs 									 | get file system statistics 						 																			| 
|100. 		    | fstatfs 								 | get file system statistics 						 																			| 
|101. 		    | ioperm  								 | set port input/output permissions 				 																		| 
|102. 		    | socketcall  						 | socket system calls 						 		 																					| 
|103. 		    | syslog 	  							 | read and/or clear kernel message ring buffer  	 															| 
|104. 		    | setitimer   						 | set value of interval timer 			  			 																		| 
|105. 		    | getitimer   						 | get value of interval timer 			  			 																		| 
|106. 		    | sys_newstat 						 | get file status 	  					  			 																				| 
|110. 		    | iopl change 						 | I/O privilege level 					  			 																				| 
|111. 		    | vhangup 								 | virtually hangup the current tty  	  			 																	| 
|112. 		    | idle 										 | make process 0 idle 	  				  			 																			| 
|113. 		    | vm86old 								 | enter virtual 8086 mode 				  			 																			| 
|114. 		    | wait4 									 | wait for process termination, BSD style 			 																| 
|115. 		    | swapoff   							 | stop swapping to file/device 						 																		| 
|116. 		    | sysinfo   							 | returns information on overall system statistics   													| 
|117. 		    | ipc 										 | System V IPC system calls 						 																				| 
|119. 		    | sigreturn 							 | return from signal handler and cleanup stack frame 													| 
|120. 		    | clone 									 | create a child process 																											| 
|122. 		    | uname 									 | get name and information about current kernel 																| 
|125. 		    | mprotect 								 | set protection of memory mapping 			  																		| 
|126. 		    | sigprocmask 						 | POSIX signal handling functions  			  																		| 
|130. 		    | get_kernel_syms 				 | retrieve exported kernel and module symbols 																	| 
|131. 		    | quotactl 								 | manipulate disk quotas 					  																					| 		
|132. 		    | getpgid 								 | get process group ID   					  																					| 
|133. 		    | fchdir  								 | change working directory 					  																				| 
|134. 		    | bdflush 								 | start, flush, or tune buffer-dirty-flush daemon 															| 
|135. 		    | sysfs 				  				 | get file system type information 				 		  															| 
|136. 		    | personality   					 | set the process execution domain 				 		  															| 
|138. 		    | setfsuid 								 | set user identity used for file system checks  		  												| 
|139. 		    | setfsgid 								 | set group identity used for file system checks 		  												| 
|140. 		    | sys_llseek 							 | move extended read/write file pointer 				  															| 
|141. 		    | getdents 								 | read directory entries 								  																		| 
|142. 		    | select 									 | sync. I/O multiplexing 								  																		| 
|143. 		    | flock  									 | apply or remove an advisory lock on an open file 		  											| 
|144. 		    | msync  									 | synchronize a file with a memory map  				  															| 
|145. 		    | readv  									 | read data into multiple buffers  						  															| 
|146. 		    | writev 									 | write data into multiple buffers 						  															| 
|147. 		    | sys\_getsid 						 | get process group ID of session leader 				  														| 
|148. 		    | fdatasync  							 | synchronize a file's in-core data with that on disk     											| 
|149. 		    | sysctl  								 | read/write system parameters 							  																| 
|150. 		    | mlock 									 | lock pages in memory   								  																		| 
|151. 		    | munlock 								 | unlock pages in memory 								  																		| 
|152. 		    | mlockall 								 | disable paging for calling process  					  															| 
|153. 		    | munlockall 							 | reenable paging for calling process 					  															| 
|154. 		    | sched\_setparam					 | set scheduling parameters 		  					  																	| 
|155. 		    | sched\_getparam					 | get scheduling parameters 		  					  																	| 
|156. 		    | sched\_setscheduler			 | set scheduling algorithm parameters 					  															| 
|157. 		    | sched\_getscheduler			 | get scheduling algorithm parameters 					  															| 
|158. 		    | sched\_yield 						 | yield the processor 									  																			| 
|159. 		    | sched\_get\_priority\_max| get max static priority range 				  	  	  															| 
|160. 		    | sched\_get\_priority\_min| get min static priority range 				  	  	  															| 
|161. 		    | sched\_rr\_get\_interval | get the SCHED_RR interval for the named process 	  	  											| 
|162. 		    | nanosleep 							 | pause execution for a specified time (nano seconds) 	  											| 
|163. 		    | mremap 									 | re-map a virtual memory address 				 		  																| 
|164. 		    | setresuid 							 | set real, effective and saved user or group ID 		  												| 
|165. 		    | getresuid 							 | get real, effective and saved user or group ID 		  												| 
|166. 		    | vm86 										 | enter virtual 8086 mode 								  																		| 
|167. 		    | query_module 						 | query the kernel for various bits pertaining to modules 											| 
|168. 		    | poll 										 | wait for some event on a file descriptor  	 																	| 
|169. 		    | nfsservctl 							 | syscall interface to kernel nfs daemon 		 																	| 
|170. 		    | setresgid  							 | set real, effective and saved user or group ID 															| 
|171. 		    | getresgid  							 | get real, effective and saved user or group ID 															| 
|172. 		    | prctl 									 | operations on a process 																											| 
|180. 		    | pread 	 								 | read from a file descriptor at a given offset 																| 
|181. 		    | sys_pwrite 							 | write to a file descriptor at a given offset  																| 
|182. 		    | chown  									 | change ownership of a file 			  																					| 
|183. 		    | getcwd 									 | Get current working directory 		  																					| 
|184. 		    | capget 									 | get process capabilities 				  																					| 
|185. 		    | capset 									 | set process capabilities 	 			  																					| 
|186. 		    | sigaltstack 						 | set/get signal stack context  		  																					| 
|187. 		    | sendfile 								 | transfer data between file descriptors  																			| 
|190. 		    | vfork 									 | create a child process and block parent 																			| 
