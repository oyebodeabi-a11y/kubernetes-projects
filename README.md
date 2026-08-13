# kubernetes-projects
Automates container deployment, scaling, and management. It serves as the core platform for modern cloud infrastructure, multi-cloud setups, and microservices.

To start the project - i.e. kick start the kubernetes cluster. Use minikube
Minikube is the singular node cluster.
1. Log into Docker desktop
2. Run the command: Minikube start
3. Minikube cluster is a single node  cluster - this is usually used for development but never in production.

## NGINX Deployment
### Make sure you are in the nginx folder for this project.
4. In the minikube file folder; the nginx-folder - paste the deployment.yaml file, which has the defined pods.(if not done already)
5. In the minikube file folder, paste the service.yaml file.(f not one already)
6. In the terminal, define the alias using:
alias k=kubectl
7. Type: k get nodes
8. Next create the namespace, type: k create namespace test
9. To see it has been created, type k get namespace.
### 10. Then type  (This is my desired state file) 
k apply -f deployment.yaml -n test 

11. Then type: k get pods -n test to create name space. Always ensure the name space is included in the command once its defined. (this checks the pods created in the namespace -n test)
12. Then type k describe pod nginx-deployment-77bc6bd484-24snm -n test (use the applicable pod name)
13. Type: k get events - this allows you to know more about the health of the cluster.
14. Next, using the service.yaml file, to allow the cluster to be seen from the outside world (because of the loadbalancer node type), type the command below:
15. k apply -f service.yaml -n test
16. Then type, k get svc -n test 
17. Below is the result:
$ k get svc -n test
NAME    TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
nginx   LoadBalancer   10.96.84.249   <pending>     80:30772/TCP   86s

18. To run nginx on the browser run the command within the test namespace
Type the command:  minikube service nginx -n test

To terminate the name space: type k delete namespace test. Then check the namespace is gone, type k get namespace. Then to  check the deployment   file is gone, type k get deployment.yaml -n test.

## MINI TASK:
You have been asked by your team lead to use a single node cluster that is installed on my local machine to deploy an nginx webserver in Kubernetes using the relevant manuscript files. 
Remember to create a namespace called "dev". The deployment.yaml file should only have 2 pods. 

<img width="581" height="134" alt="Image" src="https://github.com/user-attachments/assets/efb59254-41c1-4320-aba1-639df8cb2b5f" />

<img width="611" height="215" alt="Image" src="https://github.com/user-attachments/assets/94205c16-6c71-4bc6-9c45-73bb22738c0b" />


Note: To delete the deployment file, type k delete deployment nginx-deployment -n dev. Note deployment name is nginx-deployment

Challenge: 
I have an imagepullbackoff error in kubernetes during the course of the project.

<img width="569" height="79" alt="Image" src="https://github.com/user-attachments/assets/230df887-6dbe-4913-984e-b28d6cc89b85" />

Solution:
1. k describe pods <podname>. This gave the description backoff.
2. Edited the deployment.yaml file with the appropriate image name.
3. Deleted the deplyment.yaml file, type k delete deployment nginx-deployment
4. Then check the pods, type k get pods.
5. Then apply the correct the correct deployment file. k apply -f deployment.yaml The result should be deployment.apps/nginx-deployment created.
6. Check the pods, using k get pods
7. The image below is restored. 
<img width="553" height="59" alt="Image" src="https://github.com/user-attachments/assets/5fdbdd89-53be-4503-a162-f03e566ef54a" />

### Kubernetes troubleshooting:
1. Imagepulledbackoff error:
Possible causes:
a. When Kubernetes is trying to pull the image specified in the deployment file, caused by wrong  image tagging e.g. 1.14.2. When Kubernetes is trying to pull the image from Docker hub, the correct image is not availabe. This is the error generated.

b. Wrong image name.
c. Wrong command start.


To fix the image pullback error:
1. Type: k delete deployment nginx-deployment ###to check the deployment has been removed.
2. Type: k get deployment ###to check that the resources have been removed.
3. Type: k get pods ###to check if the pods are gone.
4. Go back to the deployment.yaml file and correct the image name.



## Jenkins Deployment
1. In the minikube file folder; the jenkins-folder - paste the deployment.yaml file, which has the defined pods.(if not done already)
5. In the minikube file folder, paste the service.yaml file.(f not one already)
### Ensure any previous deployment folders have been removed.
To check Type: k delete deployment with any existing deployment files 
e.g k delete deployment-nginx deployment.

6. In the terminal, define the alias using:
alias k=kubectl. Alias does not need to be repeated if done already. 
7. Type: k get nodes
8. Next create the namespace, type: k create namespace abi
9. To see it has been created, type k get namespace.
### 10. Then type  (This is my desired state file) 
k apply -f jenkins-deployment.yaml -n abi 

11. Then type: k get pods -n abi to see the pods. 
Always ensure the name space is included in the command once its defined. (this checks the pods created in the namespace -n abi)
12. Then type k describe pod nginx-deployment-77bc6bd484-24snm -n test (use the applicable pod name)
13. Type: k get events - this allows you to know more about the health of the cluster.
14. Next, using the service.yaml file, to allow the cluster to be seen from the outside world (because of the loadbalancer node type), type the command below:
15. k apply -f jenkins-service.yaml -n abi
16. Then type: k get svc -n abi


Below is the results:
k get svc -n abi

NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
jenkins        NodePort    10.111.238.74   <none>        8080:30000/TCP   37s
jenkins-jnlp   ClusterIP   10.98.229.159   <none>        50000/TCP        37s

18. To run jenkins on the browser run the command within the test namespace
Type the command:  minikube service jenkins -n abi

<img width="740" height="409" alt="Image" src="https://github.com/user-attachments/assets/a409ccce-314c-48b2-af34-cdc7c9d58787" />

1. To delete the deployemnt, Type:k get deployment -n abi
2. Then type: k delete deployment jenkins -n abi
3. To delete to delete the namespace, Type: k delete namespace abi



## Apache2 deployment
1. In the minikube file folder; the apache2-folder - paste the deployment.yaml file, which has the defined pods.(if not done already)
5. In the minikube file folder, paste the service.yaml file.(f not one already)
### Ensure any previous deployment folders have been removed.
To check Type: k delete deployment with any existing deployment files 
e.g k delete deployment-apache2 deployment.

6. In the terminal, define the alias using:
alias k=kubectl. Alias does not need to be repeated if done already. 
7. Type: k get nodes
8. Next create the namespace, type: k create namespace abi
9. To see it has been created, type k get namespace.
10. Then type  (This is my desired state file) 
k apply -f deployment.yaml -n abi 

11. Then type: k get pods -n abi to see the pods. 
Always ensure the name space is included in the command once its defined. (this checks the pods created in the namespace -n abi)
12. Then type k describe pod nginx-deployment-77bc6bd484-24snm -n test (use the applicable pod name)
13. Type: k get events - this allows you to know more about the health of the cluster.
14. Next, using the service.yaml file, to allow the cluster to be seen from the outside world (because of the loadbalancer node type), type the command below:
15. k apply -f jenkins-service.yaml -n abi
16. Then type: k get svc -n abi

Result below:
 k get svc -n abi
NAME      TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
apache2   LoadBalancer   10.104.246.197   <pending>     80:31892/TCP   12s

17.To run jenkins on the browser run the command within the test namespace
Type the command:  minikube service apache2 -n abi


<img width="413" height="77" alt="Image" src="https://github.com/user-attachments/assets/2d6caae1-3ea5-48ae-a146-5286635f9ab6" />

<img width="598" height="431" alt="Image" src="https://github.com/user-attachments/assets/d335b58d-12be-4cf5-a4a2-206895b5d058" />