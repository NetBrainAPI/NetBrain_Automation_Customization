# Compare Prefix Set Between Multiple Pair of Routers  

**Version: NetBrain v7.x, v8.x**

## Use Case
Managing network and want to make sure that your network devices are up to date correctly with configuration. If there are many pairs of redundancy devices in the network, we might forget to updaate the configure on prefix, access list, hsrp, etc 

This runbook will identify the different between two devices prefix set. If the configuration are the same, 'diff' is False in the report. If the configuration are not the same, 'diff' column is True in the report and both devices will be put into the map for change management.  


## Solution
![](images/compare_prefix_set_two_devices.gif)

There are many configuration parsers available by default in NetBrain to be developed in similar way. 


### *Disclaimer*
*The solution provided above is developed by testing environment so may not suit to every scenario, please feel free to contact NetBrain Support <Support@netbraintech.com> if any questions related to the solution.*