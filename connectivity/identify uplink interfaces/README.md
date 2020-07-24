# Identify all Uplink interfaces (Cisco only)

Note:
This guide is meant only for Cisco devices as it relies on CDP, but could be adapted to other hardware using the same methodology.

## Use Case

For customers who don't have their uplinks clearly labelled or defined, or suspect that their uplinks are not clearly labelled and defined. The resulting report can be used to assist in properly labelling all uplink interfaces.

## Solution

1. Building the Parser

If there is not already a parser for the cdp neighbors command, it will have to be built. This guide assumes a basic understanding of building parsers. For information on building parsers, please visit the help page [here](https://www.netbraintech.com/docs/ie80/help/index.html?creating-a-cli-command-parser.htm)

- In the "Node Type" dropdown, select "Traditional Devices", then select all Cisco device types which support CDP 

- Set the "Parser Type" to "CLI Command", enter the `show cdp neighbors` command and click "Retrieve"

- This will bring up a menu of devices, select one as the sample device, ideally one known to have multiple neighbors as that will make a more thorough sample

- Highlight the output table and select "Define Table", then verify the results as shown below:

![creating parser](connectivity/identify uplink interfaces/resources/createparser.gif)

- Save the parser and name it appropriately

2. Building the Qapp

While the following steps will be detailed, some basic understanding of how to build Qapps will be assumed. For information on building Qapps, please visit the help page [here](https://www.netbraintech.com/docs/ie80/help/index.html?qapp.htm)

- Start by creating a Canvas

- Enter the Canvas by double-clicking on it

- From the *Device Queue* extend to "Device(this)" and from there extend a CLI command

- Enter `show cdp neighbors` into the command field and the appropriate parser and variable tree should appear (shown below):

![parser and variable tree](connectivity/identify uplink interfaces/resources/qapp_parservariabletree.png)

- Extend to a "Device Data Table" then further extend that to a *single table operator sub-table*

- Select the "Operator" node and filter the table as shown below to remove devices that are not routers or switches:

![filter sub-table](connectivity/identify uplink interfaces/resources/qapp_filtersubtable.gif)

- Extend to a *single table operator sub-table* once more and apply the following filter to remove all columns except the interface ID:

![filter interfaces](connectivity/identify uplink interfaces/resources/qapp_filterinterfacesonly.png)

- Extend to the *single table operator*, *convert* and convert to a CSV then extend to a *basic output* and finally extend to a *CSV Export*(shown below):

![extend to a CSV export](connectivity/identify uplink interfaces/resources/convertcsv.gif)

- Save the Qapp and name it appropriately

3. Creating and running the Report

- Navigate to the "Inventory Reports" section

- Select "Go To Manage Reports Page" then "New Inventory Report"

- Setup the new report as shown below:

![create a report](connectivity/identify uplink interfaces/resources/createreport.gif)

- Click "Back to Previous Page" and select the new report, it should automatically start running

- Once it has ran, click the "Export" button at the top to export the report in the desired format (.xlsx or .csv)

## Results

There is now a report that shows the uplink ports detected on each device. Note that the information that appears in the report can be easily modified in the Qapp. For instance, if the device name on the other end of the uplink is desired, simply add that to the filter in the *sub-table operation*.

As mentioned at the beginning of the document, this can be modified for other similar protocols that are supported by other devices. Only a different parser would be required, as the Qapp logic would largely remain the same.
