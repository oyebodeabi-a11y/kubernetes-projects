Task 1:
I have just been recently employed as a Kubernetes engineer 1. I have been asked to deploy a yaml file. This deployment file has been created and applied.
On running the command, k get pods, the pod has a status error of "crashloopbackoff".
Question:
What is the cause of the error and how can it be resolved?

Crashloopbackoff error occurs :
1.when a docker image full of codes or bugs is stored. When kubernetes tries to run the image/code which is full of bugs - the command crashes.
As the docker image is in a container, when ran, and there are existing bugs/errors in the code - a crash occurs and the pods dies/ephemral.
Kubernetes steps in and springs up another pod. This causes another crash and the loop continues. 
As we know that in the deployment file, we start the presence of 3 more pods.

2.A wrong command line exists in the docker file or in the container e.g.  appp.py instead of app.py.

error displayed: 
python: can't open file '/app/appp.py': [Errno 2] No such file or directory

3.A wrong CPU limit. Every docker image requires a certain CPU limit. If the cpu limit required is 100MB but the yaml file has 50MB, this can also cause a crashloopbackoff.

As the docker image is in a container, when ran, and there are existing bugs/errors in the code - a crash occurs and the pods dies/ephemeral.
Kubernetes steps in and springs up another pod. This causes another crash and the loop continues. 

As we know that in the deployment file, we start the presence of 3 more pods. 

This is why security is important through out all the stages.

Solution:
Run the appy.py file
Press the play button and copy the http link
The python page is displayed. This shows that the python app is working.

To corrupt the python file:
edit the python appy.py file - let it create an error. put a # at the start of the python file.

Next:
1.Create a docker image and push to DockerHub.
2.To do this, type:
3.docker build -t bim15/imagename .
4.Type: docker images
5.To push to dockerhub, type:
docker push bims15/imagename:latest
6.Check the docker image has been pushed to docker hub.
7.Log into Docker hub via google to check the image created is in docker hub.
because an image in docker desktop may not necessary be in docker hub.

8.Then create a dry run file to produce a yaml file with the corrupt docker image.
Type:
k run dialog3 --image=bims15/dialog3:latest --dry-run=client -o yaml >pythonerror1.yaml

Type:
k apply -f yaml pythonerror1.yaml

Type:
K get pods.

The result is as shown below: The status of dialog 3 pod is CrashLoopBackoff.
NAME      READY   STATUS             RESTARTS     AGE
dialog    1/1     Running            0            16m
dialog3   0/1     CrashLoopBackOff   1 (3s ago)   9s

k run dialog --image=bims15/dialog3:latest --dry-run=client -o yaml >pythonerror1.yaml

To see the container, type:
k exec -it dialog -- sh

To troubleshoot this issue:
1.K get event.

The below shows kubernetes trying to restart the pod which is corrupt and full of bugs. The pod dies (ephemeral) and kubernetes tries to run the pod again.

Note where there is a kind:Pod - only 1 Pods is defined in the manifest script.
There must be a pod running.

9m42s       Normal    Starting                  node/minikube   
6d22h       Normal    Killing                   pod/nginx       Stopping container nginx
6d22h       Normal    Killing                   pod/nginx1      Stopping container nginx1

2.K describe pod dialog3
3.k logs dialog3
4.k logs dialog3 --previous
5.kubectl logs --tail=100  dialog3





