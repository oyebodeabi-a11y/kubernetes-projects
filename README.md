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
a. When Kubernetes is trying to pull the image specified in the deployment file, caused by wrong image tagging e.g. 1.14.2. When Kubernetes is trying to pull the image from Docker hub, the correct image is not availabe. This is the error generated.

b. Wrong image name e.g nginx spelt as ngix which is the image name.
c. Wrong command start. e.g in the docker file where the app.py is incorrectly written. 
d. Wrong tag version e.g. 1.14.3 instead of 1.14.2


To fix the image pullbackoff error:
1. Type: k delete deployment nginx-deployment ###to check the deployment has been removed.
2. Type: k get deployment ###to check that the resources have been removed.
3. Type: k get pods ###to check if the pods are gone.
4. Go back to the deployment.yaml file and correct the image name.

2. Error: Pod in pending state
E0818 10:33:49.050360   19992 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
Unable to connect to the server: dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it.

Causes:
1. This means the nodes to accomodate the pod is not ready. 
A Pod in Pending state is usually a scheduling problem: Kubernetes has created the Pod, but the scheduler cannot currently find a suitable worker node where it can place the Pod.

Diagnosis:
1. Run k get nodes

2. minikube status
This is to show the status of the single node cluster and to see if the node(s)

solution: 
Ensure the node and pods have a status as running when the k get status is checked.


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
2. Then type: k delete deployment jenkins -n abi or k delete -f deployment.yaml
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

1. To delete the deployemnt, Type:k get deployment -n abi
2. Then type: k delete deployment apache2-deployment -n abi
3. To delete to delete the namespace, Type: k delete namespace abi


### Challenges:

Minikube start error:

💣  Exiting due to PROVIDER_DOCKER_VERSION_EXIT_1: "docker version --format <no value>-<no value>:<no value>" exit status 1: failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
📘  Documentation: https://minikube.sigs.k8s.io/docs/drivers/docker/

Docker desktop was not up and running.

Solution:

Sign into Docker desktop.
Re run minikube start.
Issue resolved.

## Imperative commands

A faster way of generating the yaml file based on specific spec provided.

This is another method to launch the manifest scripts for server applications. 

### Dry Run

This is the process of running the kubernetes file without the corresponding object i.e. image or image name being created.

### Task
Using Dry Run imperative command (because I did not want to create the pods automatically)
Create 2 pods with a Dry run command to create the .yaml file. Run the yaml file and show that 2 pods have been created.

Solution:
Log into minikube start and log into docker desktop
Create k alias first
Run the dry run command to create abimbola.yaml file:
k run nginx --image=nginx:1.14.2 --dry-run=client -o yaml >abimbola.yaml

Run k apply -f abimbola.yaml

Run k get pods

Result: A single pod was created.

Challenge : 2 pods are not created in the dry run yaml file.

Reason:
The kind: Pod resource does not support replicas: A standard Kubernetes Pod creates a single, isolated instance. If you want multiple managed instances, you should use a Deployment instead. Hence, the kind:Pod will only generated a single pod.

Duplicate spec: keys: Your YAML currently has two separate spec: blocks. In YAML, a later key overwrites the earlier one, which is why your replicas: 2 is being ignored.

Solution:

To create multiple pods automatically, change the kind to Deployment, include the replicas: 2 setting inside the deployment's template spec, and add a selector.

For a desired state pod, the kind must be deployment and not pod. 

See command below:

apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: nginx
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      run: nginx
  template:
    metadata:
      labels:
        run: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        name: nginx
        resources: {}
      dnsPolicy: ClusterFirst
      restartPolicy: Always

### Task 2: Expose the application in the pod which is nginx
Another dry run is exceuted as shown below: This is to create the dry run for the service.yaml file
kubectl expose pod nginx --type=LoadBalancer --port=80 --target-port=80 --name=abimbolaservice --dry-run=client -o yaml > abimbolaservice.yaml

Then run the command for to service.yaml file:
k apply -f abimbola service

Then run the command k get svc to show the services running.

Then run the command minikube service abimbolaservice

<img width="499" height="232" alt="Image" src="https://github.com/user-attachments/assets/a609b8f1-41a6-4380-b2f0-6d2313b4e52e" />


Assignment:

I. Create a single pod of image httpd:alpine3.20 in namespace application (check if namespace exist or not)
Pls the pod should be name web1 and the container should be name web-container

Ii. Write  a shell script to output the status of the pod

Solution:
First, create the dry run that will produce the yaml file with the command below:

k run web1 --namespace=application --image=httpd:alpine3.20 --dry-run=client -o yaml >task.yaml

Note: 
1. A single pod is created
2. pod name is web1
3. Include namespace --namespace=application
4. Include the image name, --image=httpd:alpine3.20
5. Create the yaml file name, which is task.yaml
5. Run the command above.



k -n application get pod web1  -o jsonpath={.status}
kubectl -n application  get pod web1  -o jsonpath={.status.phase

#!/bin/bash
kubectl -n application get pod web1  -o jsonpath={.status.phase}


#make it executable

chmod +x web1-status.sh
