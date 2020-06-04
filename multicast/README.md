# Multicast Infraestructure Mapping Solution

## Background

This Mulicast mapping Qapp give users the possibility of identifying all devices within their domain that have a specific multicast state present and to map and visualize that Shared / SPT (shortest path tree).

**NOTE:** _This solution will work on VPN and non VPN environments, depending on the deployment and design of the network._


## Multicast terminology and information

Extensive information regarding Multicast terminology and concepts can be found here:

[Cisco Multicast Documentation](https://www.cisco.com/en/US/tech/tk828/tech_digest09186a00801a64a3.html)

## Use Cases

Troubleshooting multicast environments (specially large ones) can be time consuming and challenging, specially if there are multiple strings or if there are customer and provider multicast involved.
The solution has been thought and designed around the possibility of potentially dealing with this kind of mVPN / non-mVPN environments that use most commonly deployed methodology Rosen VPN / SSM / ASM Models, which could also involve the use of default multicast distribution tress for signalling.

## Testing Topology

See below the testing topology for the proposed solution:



**Note:** _In order for this to be able to be tested properly, sources must be generating the multicast traffic to their respective groups. There is a static join from each destination that always query for the traffic._

- Source 10.100.0.1 must ping to 225.1.1.1 (can also ping 226.1.1.1)
- Source 10.100.0.3 must ping to 226.1.1.1


## Solution and Support

The reference solution provides support for multi-vendor platform including:

- Cisco IOS Switch
- Cisco Router
- Cisco IOS XR
- Cisco Nexus Switch
- Arista Switch
- Juniper EX
- Juniper Router

## How does this solution work and what manual tasks does it help expedite?

This solution basically consists in 2 different Qapp executable files, Multicast Infra report MVS.xapp and Draw Multicast Tree Topology for SG.xapp.

In order for this solution to provide accurate results, the first Qapp needs to run on the **ENTIRE** multicast infrastructure base (this means, on a device group that contains all the multicast enabled devices).
That being said, if such group does not exists, it is required to be created.

PICTURE 1 through 4 HERE

Once the device group has been created, now the base for this solution to work has been set.






