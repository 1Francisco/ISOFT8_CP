# Architectural Decision Record

## Context
The development team identified a need to improve the operation of the timer within the game. The current implementation lacks appropriate synchronization, which may lead to race conditions when accessed concurrently by multiple threads. This can cause unexpected behavior or inaccuracies in the game’s timing mechanics.

## Decision
The team decided to implement a **Lock** mechanism in the back-end of the game using Python. The Lock will ensure that only one thread can modify the timer at a time, allowing time-related operations to execute safely and consistently.

## Justification
A Lock is a widely used synchronization mechanism in concurrent programming. It helps manage access to shared resources, preventing **race conditions** and ensuring correct execution. This solution was chosen for its effectiveness, ease of implementation in Python, and minimal disruption to the current codebase.

## Consequences

### Positive
- Improved stability and accuracy of the timer.
- Prevention of concurrency-related errors.
- Easier to maintain and understand concurrent logic.

### Negative
- Risk of unnecessary blocking if poorly implemented.
- Possible conflicts with legacy code not designed with locking in mind.
- Additional testing required to ensure correct integration.

## Assigned Teams
**Team: Los DELL Pancho**

Team responsibilities:
- Identify critical concurrency points in the game's code.
- Implement and test the Lock mechanism for the timer.
- Ensure no deadlocks or synchronization issues occur.
- Document the impact of the solution on system performance and reliability.