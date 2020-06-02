# Create Fiber Connection Map
This is a solution for the customization connection by using NetBrain Dynamic Map and Topology Manager.

*Version: NetBrain v8.x*

## Use Case

Topology is critical for network, but it is really hard to have a central place to update the topology or map. L3 and L2 topology can be detected by using IP address and Neighbor Discover Protocol, but hard to acknowledge the connections like fiber, transparent firewall, etc.

## Solution

### 1. Create Generic Devices

![](images/create_generic_devices.png)
* Click the `Generic Device` under `Domain Management`.
* Create the device and add links.

*refer link: https://www.netbraintech.com/docs/ie80/help/index.html?undiscoverable-devices.htm*

### 2. Add Connections in Topology Manager

![](images/click_topo_manager.png)
* Click the `Topology Link Manager` under `Domain Management`.
* Click the `Total Topology Link` based on the `Topology Type`.

![](images/add_topo_links.png)
* `Add Topology Link` to create customized links.

![](images/topo_links_added.png)
* Verify added customized links.

*refer link: https://www.netbraintech.com/docs/ie80/help/index.html?adding-a-topology-link.htm*

## Results

![](images/map_generic_device.gif)
* Once the domain topology rebuild, the map will update automatically.
* The map can be used for future documentation and troubleshooting.


### *Disclaimer*
*The solution provided above is developed by testing environment so may not suit to every scenario, please feel free to contact NetBrain Support <Support@netbraintech.com> if any questions related to the solution.* 