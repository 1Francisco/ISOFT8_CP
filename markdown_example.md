# ADR

## ARCHITECTURAL DECISION RECORD (ADR)

**Los DELL Pancho**

---

### ● DECISION TITLE:

Time out - video game

---

### ● STATUS:

Proposed

---

### ● CONTEXT:

We seek to resolve and improve the counter within the game as is its initial operation, this will help  
to better understand the game.

---

### ● DECISION:

We decided to implement a lock in the back-end of the game.

---

### ● JUSTIFICATION:

A Lock, in programming this is a synchronization mechanism that is used to control access to  
shared resources by multiple threads. Its main purpose in this proposal is to prevent race conditions  
and ensure that the timing process executes correctly. This solution is the most effective and simple  
way to reach the desired solution and will be implemented in Python.

---

### ● CONSEQUENCES:

There are risks such as loss of information or bad syntax between old elements with the new Lock.  
Our proposed solution is based on improving the operation of the game without compromising the  
understanding and familiarity of the game.
