Pod anti affinity:
This ensures pods are spread over the different nodes.
This allows for high availability of the application and prevents a single source of failure. 

How do you prevent wastage in Kubernetes:
1.By Introducing HVA. Kubernetes by default creates 3 worker nodes. if 3 is not required or there is a downtime with a pod, they are idle and could potentially lead to wastage. HPA is  then implemented which is auto-scaling of the pods allocated.
2.kubernetes automatically switches to the other pods if a particular pod A fails . 