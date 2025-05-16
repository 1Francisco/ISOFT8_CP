# Architectural Decision Record

## Context
The development team identified a need to improve the operation of the timer within the game. The current implementation lacks appropriate synchronization, which may lead to race conditions when accessed concurrently by multiple threads. This can cause unexpected behavior or inaccuracies in the game’s timing mechanics.

