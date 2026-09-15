#### Task 1 (Buds are ephemeral, how do we preserve the data):

Steps below:
1.Deploy a pod called nginx-pod with the image nginx and 
2.inside the pod create a file text1.txt  inside one of the directories(tmp) saying 
“i love devops” and inside file text.txt echo  “am into cloud computing”
3.Kill this pod nginx-pod
4.Create the pod back and check if the files are still there inside that directory

### Solution:
1.Create the pod using the command below:
k run nginx-pod --image=nginx

2. Type:
k get pods

3.To go inside the pods, type the command below:
k exec nginx-pod -it -- bash

4.Type ls

5.Type cd tmp

6.Type  echo "I love DevOps, and I am into Cloud computing" > text.txt

7.Type ls

8.cat text.txt

9.Type exit

10.k delete pod nginx-pod

11.Create the pod all over again and check the data has been removed.

Task 2:
In a volume mount; the data can be preserved in the volume mount in a command.
BUT THE ABOVE SOLUTION WILL NOT WORK IN PROPER COMPANY SETTINGS BC THE DEVELOPERS MAY NOT BE AWARE OF THE FILESE SYSTEM IN THE KUBERNETES CLUSTERS SO WHAT IS USED IS CALL PERSISTENT VOLUME AND PERSISTENT VOLUME CLAIMS.


