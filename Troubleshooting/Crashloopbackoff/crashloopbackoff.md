Task 1:
I have just been recently employed as a Kubernetes engineer 1. I have been asked to deploy a yaml file. This deployment file has been created and applied.
On running the command, k get pods, the pod has a status error of "crashloopbackoff".
Question:
What is the cause of the error and how can it be resolved?

Crashloopbackoff error occurs when a docker image full of codes or bugs is stored. When kubernetes tries to run the image/code which is full of bugs - the command crashes.

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
docker build -t <imagename> .
3.Type: docker images
4.docker build -t bim15/imagename .
5.To push to dockerhub, type:
docker push bims15/imagename:latest
6.Check the docker image has been pushed to docker hub.

7.Then create a dry run file to produce a yaml file with the corrupt docker image.
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
K get events
K describe pods

