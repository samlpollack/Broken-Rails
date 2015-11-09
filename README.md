# Broken-Rails

[Mapping Visualization](https://rawgit.com/samlpollack/Broken-Rails/master/index.html)

The files required to run the visualization are:
* index.html
* interactive_map_resources/filter_dict.js
* interactive_map_resources/d3.v3.min.js
* interactive_map_resources/flot

This visualization maps serious rail defects in MTA subways from 2005-2015. Depending on the zoom level the map shows either a heat map or a cluster map. The user can filter the data by pressing the '+filter' button on the top right. Statistics of the current map are shown in the panel on the left as well as filters. Filters can be added or removed and the map updates automatically. Once the map is zoomed in enough the user can click on a station to see the statistics for that station alone. This popup appears next to the stats panel so you can compare values. 
