from diagrams import Diagram, Cluster, Edge

from diagrams.onprem.client import Client
from diagrams.azure.compute import VM
from diagrams.azure.network import PublicIpAddresses, ApplicationGateway, LoadBalancers, VirtualNetworks
from diagrams.azure.analytics import LogAnalyticsWorkspaces


graph_attr = {
    "splines": "curved", # https://graphviz.org/docs/attrs/splines/
}

with Diagram("3-tier-architecture", show=False, direction="LR", graph_attr=graph_attr):
    client = Client("client")
    pip = PublicIpAddresses("pip")
    log = LogAnalyticsWorkspaces("log")

    tcp80 = Edge(label="tcp/80 (http)")
    tcp443 = Edge(label="tcp/443 (https)")
    tcp1433 = Edge(color="blue", style="dotted", label="tcp/1433")


    with Cluster("vnet"):
        with Cluster("snet-agw-tier"):
            agw = ApplicationGateway("agw")

        with Cluster("snet-web-tier"):
            vm_group_web_tier = [VM("vm"), VM("vm")]

        with Cluster("snet-app-tier"):
            lb_app = LoadBalancers("lb")
            vm_group_app_tier = [VM("vmm"), VM("vm")]

        with Cluster("snet-db-tier"):
            lb_db = LoadBalancers("lb")
            vm_group_db_tier = [VM("vm"), VM("vm")]
    
    # outside
    client >> tcp443 >> pip

    # pip to agw
    pip - Edge(style="dotted") - agw

    # inside vnet
    agw >> tcp80 >> vm_group_web_tier >> tcp80 >> lb_app >> tcp80 >> vm_group_app_tier >> tcp80 >> lb_db >> tcp1433 >> vm_group_db_tier
    
    # log collector
    agw << Edge(label="collect") << log



