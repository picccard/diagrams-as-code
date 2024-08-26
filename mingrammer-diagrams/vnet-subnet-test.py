from diagrams import Diagram, Cluster, Edge

from diagrams.azure.compute import VM
from diagrams.azure.network import LoadBalancers, VirtualNetworks, Subnets

graph_attr = {
    "splines": "spline",
}

with Diagram(
    "test vnet",
    show=False,
    direction="LR",
    graph_attr=graph_attr
):
    with Cluster("sub-prod-service1"):
        with Cluster("10.20.0.0/16"):
            vnet = VirtualNetworks("vnet-prod-service1", height="0.5", width="0.5", imagescale="false")
            with Cluster("snet - 10.20.30.0/24"):
                # snet1 = Subnets("snet1", height="0.5", width="0.5", imagescale="false")
                vnet_vm1 = [VM("vmm"), VM("vm")]
                vnet_lb1 = LoadBalancers("lb")
            with Cluster("snet - 10.20.40.0/24"):
                # snet2 = Subnets("snet - 10.20.40.0/24", height="0.5", width="0.5", imagescale="false")
                vnet_vm2 = [VM("vmm"), VM("vm")]
                vnet_lb2 = LoadBalancers("lb")
    
    vnet_lb1 >> vnet_vm1
    vnet_lb2 >> vnet_vm2