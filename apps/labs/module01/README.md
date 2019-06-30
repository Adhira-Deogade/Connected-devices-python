# Read system performace - python
An app that will read basic system performance data from the device

## [System performance adaptor](apps/labs/module01/SystemPerformanceAdaptor.py)
#### Tasks:
1. **_psutil_** to obtain system performance information
2. Implement thread that runs periodically for 10 seconds to obatin the information
3. Display information on console in human-readable format

## [System performance app](apps/labs/module01/SystemPerformanceApp.py)
#### Tasks:
1. Initialize "system performance adaptor" and runs the thread.
2. Then waits indefinitely

## How to run the app:
```
cd apps/labs/module01/
python3 SystemPerformanceApp.py
```

## Sample output:
>  --------------------
>         New system performance readings:
>            scpustats(ctx_switches=494453, interrupts=894498, soft_interrupts=531871, syscalls=0)
>           svmem(total=17126346752, available=9656291328, percent=43.6, used=7428300800, free=9463189504, active=171577344,
>         inactive=161665024, buffers=34848768, cached=200007680, shared=18145280, slab=14200832)

## Diagram representation:
![alt text](apps/labs/module01/Module1.jpg)
