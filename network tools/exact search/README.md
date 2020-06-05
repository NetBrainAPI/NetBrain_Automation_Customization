# Exact Search [Cisco]


### Background
This Qapp allows you to search exact strings in the configuration on a group of Cisco devices. 

### Use Case
This Qapp is best utilized when the user needs to find devices with certain keyword in the configuration. For example a search for 10.0.0.1 would result in a report with  devices containing only 10.0.0.1 in the configuration not 10.0.0.11.

#### <ins><span style="color:red">Important</span></ins>:  
1. Only works for Cisco devices that support the  command <i>"show running-config | inc $input"</i>


### Demonstration:

![](images/exact_search.gif)

### Download links
Qapp: [Find exact keyword match [Cisco].xapp](resources/Find%20exact%20keyword%20match%20[Cisco].xapp)

### *Disclaimer*
*The solution provided above is developed by testing environment so may not suit to every scenario, please feel free to contact NetBrain Support <support@netbraintech.com> if any questions related to the solution.* 

<!--
Tags: #search #configuration #qapp
-->



