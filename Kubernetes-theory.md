KUBERNETES BACKGROUND
What is Kubernetes?
It is a comtainer orchestration tool that deploys containerised applications to end users.

What is Kubernetes clusters?
These are a set of networked containers called nodes that run containerised applications.

For a developer, putting applicationsin a container is significant so that the libraries remain intact. 
Docker and containerisation allow this,  hence kubernetes containers.
For example - building source code into a Docker image.

What are Nodes?
A node is a physical server or virtual machine that hosts the kubernetes control plane software and/or kubernetes pods. 

Kubernetes runs your workload by placing containers into Pods to run on nodes.

One of the ways kubernetes reduces low downtime is to have mulitple nodes.

Nodes can be single or multiple.  

When automating an infrastructure process - It does not require manual intervention.

Infrastructure as code is the desired state.

1. Application (Jave, node.js,Python etc)
2. Build Docker Image (To build Docker image requires Docker files and docker).
3. Store Docker image (Docker images are stored in Docker hub or ECR).
4. ECR is preferred because its safer and security is enhanced.
5. Docker hub is usually used for the development stage.

An application that has been dockerised into an image through a Kubernetes cluster, must be put in a container.

The containerised application is placed in a pod. 

What is a Pod?
A pod is a small deployment and manageable object in kubernetes.

Pods sit on top of a layer called nodes.

Containers are put into pods and assigned to different worker nodes by the scheduler.

Kuberetes clusters are a set of nodes that houses each of the pods.

Kubernetes clusters (set of nodes).

Yaml file is the desired state which states the type of file needed. This is known as the deployment.yaml file. Also known as the manuscript configuration file.

Kubernetes clusters are usually housed in multiple pods, 3 or more. 

Kubernetes will ensure there are 3 pods alive at all times.

Pods are ephemeral in kubernetes and they die very easily, which means the ip address dies wuth it.

The 3 pods communicate with themselves using a cluster ip.

For pods to be able to communicate within themselves and not the outside world = cluster ip is used.

For pods to be able to communicate with the outside world = node ip is used.

To avoid multiple ip address changing, a load balancer is implemented. This prevents to ip address from changing.

1. How does kubernetes not experience no low downtime?
Kubernetes does not experience low downtime because the engineers configuring the desired state in the deployment.yaml file ensures 2 or 3 pods are stated in the deployment.yaml file.

Also, the applications is evenly spread in the pods. This means if anything happens to the applications housing the pods, the 

### Images in a container, a container is in a pod and a pod is assigned to a node by a scheduler.
