# kubernetes-projects
automates container deployment, scaling, and management. It serves as the core platform for modern cloud infrastructure, multi-cloud setups, and microservices.

To statrt the project - i.e. kick start the kubernetes cluster. Use minikube
Minikube is the singular node cluster.
1. Log into Docker desktop
2. # Run the command: minikube start
3. Minikube cluster is a single node  cluster - this is usually used for development but never in production.
# Make sure you are int he nginx folder for this project.
4. In the minikube file folder; the nginx-folder - paste the deployment.yaml file, which has the defined pods.
5. In the minikube file folder, paste the service.yaml file.
6. In the terminal, define the alias using alias k=kubectl 
7. Type k get nodes
8. Next create the namespace, type k create namespace test
9. To see it has been created, type k get namespace.
10. Then type  k apply -f deployment.yaml -n test
11. Then type k get pods -n test to create name space. Always ensure the name space is included in the command once its defined.
12. Then type k describe pod nginx-deployment-77bc6bd484-24snm -n test
13. Type k get events - this allows you to know more about the health of the cluster.
14. Next, using the service.yaml file, to allow the cluster to be seen from the outside world type the command below:
15. k apply -f service.yaml -n test
16. Then type, k get svc -n test
17. Below is the result:
$ k get svc -n test
NAME    TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
nginx   LoadBalancer   10.96.84.249   <pending>     80:30772/TCP   86s

18. # to run nginx on the browser run the command within the test namespace
Type the command:  minikube service nginx -n test