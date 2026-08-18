## To start minikube the single node kubernetes cluster run the command below

minikube start
alias k=kubectl
k get nodes
k get pods 
k get po
k create namespace test
k apply -f deployment.yaml
k apply -f service.yaml  -n test

# when you delete a deployment file you authoumatically deletes the pods
k delete -f deployment.yaml -n test
k delete -f service.yaml -n test
## create the file in test namespace
k apply -f deployment.yaml -n test
k apply -f service.yaml -n test

#delete pods 
k delete pod <podname>

# check the pods created in that namespace
k get pods -n test

k get events

k describe svc apache2  -n test
k get svc -n test 

# # troubleshooting

k get nodes -o wide
k get pods -n test

k logs jenkins-6fb994cfc5-twnvn -n test

# to run apache2 on the browser run the command within the test namespace

 minikube service apache2 -n test


 ## =========================================================

 using the imperative command

 # if you are confused run the command
 k run --help

 # to create a pod in yaml before running it but output 

 k run apache2web1 --image apache2 -o yaml >output.yaml


 # Dry run; print the corresponding API objects without creating them
  kubectl run apache2 --image=apache2 --dry-run=client

  k run apache2web2 --image=apache2 --dry-run=client -o yaml >output3.yaml

  k get pods
NAME                                        READY   STATUS    RESTARTS       AGE
flask-app-deployment-7899dfddf8-6qm6m       1/1     Running   0              70m
flask-app-deployment-7899dfddf8-zprwn       1/1     Running   0              69m
nginxweb1                                   1/1     Running   0              20m
nginxweb2                                   1/1     Running   0              20s
prometheus-alertmanager-0                   1/1     Running   6 (3d3h ago)   49d
prometheus-prometheus-node-exporter-rs4fd   1/1     Running   7 (3d3h ago)   49d

# since the pod is running go inside the pod aND SHOW THE FOLDERS INSIDE IT

k exec -it nginxweb2 -- sh 

# show the folders

ls
cd dev 
ls


# Now carry out this above task in test namespace
kubectl run nginxweb2 --image=nginx -ns test --dry-run=client -o yaml >output4.yaml


   # Start a busybox pod and keep it in the foreground, don't restart it if it exits
  kubectl run -i -t busybox --image=busybox --restart=Never

  # To delete namespace
  k delete namespace test

 # To run imperative command
  k run nginx --image nginx:1.14.2 -o yaml >abi.yaml

# Dry run command
k run nginx --image=nginx:1.14.2 --dry-run=client -o yaml >abirun.yaml

### since the pod is running go inside the pod aND SHOW THE FOLDERS INSIDE IT
k exec -it nginx -- sh