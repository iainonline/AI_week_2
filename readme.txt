"""
Problem statement
- We have units of cargo to be moved from location start to location end, via a network of nodes.
- There is a cost for each unit of cargo to ship product between each node
- There are also capacity constraints of units per time unit which need to be considered
- The goal is to solve the network to meet a minimum capacity requirement and at the lowest cost

Definitions
- The nodes represent warehouses
- The node or edge value represents the capacity limit for that node
- The edges represent the ability to ship between nodes
- The edge value represent the cost to move units per unit
- The movement is one directional
- The network can be defined by a list of warehouses and the cost and capacity limits for each edge

i.e.

Warehouse 1, Warehouse 2, 100, 100

"""