# Netbrain DVT Library - VRRP on Juniper


### Qapp's Description

This Qapp scans VPLS enabled Juniper nodes on a network and locates a user specified MAC address and reports the interface it is being learned from.

### Qapp Use Case

Troubleshooting in VPLS networks can be a challenging tasks. Since the traffic is labelled switched, it can be very hard to find certain infomration about end hosts in the network core. Locating an end system's MAC address is one such use example. If you have a large VPLS domain consisting of many PE nodes and hundreds or thousands of end devices being connected to each PE, finding an end host's MAC address can be challenning.

This Qapp will help you locate the MAC address of an end host in a VPLS domain. The MAC address to locate will be specified as input to the Qapp as shown below.

### The Example Network

Below is a demo VPLS network that consits of a 4 PE routers and 4 P routers. Also shown are three CE devices.

![](images/jnpr_vrrp_map_00.png)




### Applying the DVT


Once you add the Qapp to a runbook, change the "Data Source" to "Pull live data once" and provide the MAC address to be located as the sole input to the Qapp as shown in below screenshots:

![](images/jnpr_vrrp_map_01.png)

![](images/jnpr_vrrp_map_04.png)


### Interpretting the Results

Once the Qapp runs, it will scan all the VPLS PE nodes on the map and try to locate the specified MAC address. The results are depicted using different features of NetBrain's interfaces and are described in the following sections.



#### Device Highlight

The device where the MAC address is found locally is highlighted. The "Legend" in the bottom right corner of the map will show the color the device(s) will be highlighted with. In this exmaple, PE3-MX is highlighted in blue color as the MAC address is learned locally on this device.

![](images/jnpr_vrrp_legend_device.png)




#### Interface Highlight

![](images/jnpr_vrrp_legend_interface.png)



#### Device Data Units

![](images/jnpr_vrrp_ddu_01a.png)

![](images/jnpr_vrrp_ddu_01b.png)

#### Link Data Units

None

#### Device Notes

The result of the MAC search opertaion on each node are shown as a 'Device Note' attached to each deivce. In the exmaple we see that on PE1, the given MAC address is being learned from a tunnel interface (vt-*) while on PE3, the MAC address is being learned locally via the ge-0/0/2.800 interface.


![](images/qapp_result_02.png)


#### Golden Baseline Alerts


![](images/jnpr_vrrp_map_02.png)

![](images/jnpr_vrrp_map_03.png)



### Commands Used

```
show vrrp summary
```

### Sample Command Outputs

````
admin@BR1-MX1> show vrrp summary    
Interface     State       Group   VR state       VR Mode    Type   Address 
ge-0/0/1.0    up             10   master          Active    lcl    10.172.10.252      
                                                            vip    10.172.10.254      
ge-0/0/2.0    up             20   backup          Active    lcl    10.172.20.253      
                                                            vip    10.172.20.254      

admin@BR1-MX1>
````




### Download link: [Qapp-Juniper-VPLS-find-mac.xapp](qapps/Qapp-Juniper-VPLS-find-mac.xapp)


Tags: #juniper #dvt #vrrp 


<!--

http://192.168.180.25/map.html?t=2685055b-06f1-01a7-1ea0-55db439c9288&d=9ee19f5c-5a1d-4743-ad45-ec40b91fbf07&id=71e5dade-02a6-7996-311b-3b23e9467ebe&rba=4e6b6f89-516b-f8b3-68b4-3c3608b27817


-->

