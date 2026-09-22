Following on from Pods-creation, where data can be preserved using volume mounts when a pod is killed. 
However, this is not the acceptable process. The acceptable process is using persistent volume. 

Pods are ephemeral dies easily but Persist volume as the name suggest persist the data.

Task 2:

In namespace mct create a persistence volume  mct-pv.It should have capacity 100MI with access mode ReadWriteOnce and hostpath /tmp/data, no storage class named defined.
In the same namespace create  a PersistentVolumeClaim  called mct-pvc, it should request 100MI and access mode ReadWriteOnce.

N/B the PVC should be bound to the PV correctly.

In the same namespace create a pod called nginx-mct using the image nginx while the container name is mct-container, which mounts the volume at /tmp/project data

Solution:

1.Create namespace using: k create namespace mct
2.Create a yaml file using the code, mct-pv.yaml -n mct. This to have the persistent volume created.
3.Next, the persistent volume claim needs to be created which will  only exist if the persistent volume is in place.
4.Apply the persistent volume claim.yaml file. The purpose is to ensure the date will  persist when the pod dies. K apply -f mct-pvc-claim.yaml -n  mct
5.Next, create the pod which will house the project data. Run nginx-pod.yaml -n mct
6.Check the pod is created using k get pods -n mct
7.Exec into the pod using:
k exec nginx-mct -n mct  -it -- bash or k exec nginx-mct -n mct  -it -- sh
Then ls
Then cd to tmp
Then ls
The project data file will appear
cd to projectdata
To create a file in projectdata, type  echo  "I love deveOps" >cloud.txt
Then ls
Then cat cloud.txt
type exit.