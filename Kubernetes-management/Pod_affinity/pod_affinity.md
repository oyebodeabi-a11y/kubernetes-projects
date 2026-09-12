Pod Affinity:
This is also used to manage kubernetes.

Affinity means likeness or closeness.

Pod affinity is coahibiting a particular pod to a node. But there is a condition.
For this to happen, there must be close latency or cohabitation of 2 pods with similar pod labels for pod affinity to work.

why is pod affinity required in a use case:
1.When pod A and pod B are cohabitated on the same node so that latency and networking 
This is the act of colocating or cohabiting similar pods around themselves within the kubernetes cluster nodes. This allows the scheduler to determine when a particular pod is assigned, in ths case it does not depend on the nodes but on similar pod labels. 

This enables the scheduler to schedule pods based on the labels of other pods running on the nodes. 

Instead of looking at node characteristics, the scheduler can look at other pods to determine where a pod is assigned or make  decisions based on which pods are already present.

This scenario provides a fine grain control over pod placements in relation to other worker nodes within the kubernetes ecosystem.

Benefits of Pod affinity - why must a Team apply this.
1.This reduces latency.  Where the pods are close to each other in proximity, latency is reduced which then allows for pod affinity to be effective.
2.Networking. Where pods are cohabiliting and latency is reduced, the network will be improved. Communication is improved between the pods.
3.Performance is improved. 
4.Data locality is improved. With pods in the same node, the data is easily accessible because it is close to the data source.
5.Manages and helps dependences: For example when logging into AWS acc, if the authentication engine does not complete the required processes, meaning these stages are in the pods in the same node, co habiting together, then it makes it the process difficult.
6.Provides cost efficiency by optimising network transfer cost within the cluster.

Requirements and conditions:
Hard Rule and Preferred Rule.
Hard Rule:
By all means, Pods must be placed on matching node else it wont be scheduled at all. 

Preferred Rule:
This also known as soft Rule, where it specifies the pods as preferred to the node and schduling takes place at all cost but ignored during execution.

This is where the scheduler tries it best to place the pods according to preference which is pods with similar labels.
If it cannot, it places the pods and schedules it elsewhere.
There are 3 key concepts to follow:
1.Label selector: The pods having similar labels. This determines the pods to cohabit in a node.
2.Topology key: This determines the scope of coallocation of whether the pods should be in the same node or region.
3.Namespace: Pods existing in the same namespace. For example they have to be namespace Abi.