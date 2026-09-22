Task:

In namespace dev create a persistence volume  mct-pv-dev.It should have capacity 100MI with access mode ReadWriteOnce and hostpath /tmp/data, no storage class named defined.
In the same namespace create  a PersistentVolumeClaim  called mct-pvc-dev-claim, it should request 100MI and access mode ReadWriteOnce.

N/B the PVC should be bound to the PV correctly.

In the same namespace create a pod called nginx-mct-dev using the image nginx while the container name is mct-container, which mounts the volume at /tmp/devdata

Solution:
1.Create namespace dev
2.create the persistent volume using k apply -f mct-pv-dev.yaml -n dev
3.check the pv is created using k get pv -n dev
4.Next create the persistent volume claim using k apply -f mct-pvc-dev-claim.yaml -n dev
5.check the pvc is created using k get pvc -n dev
6.Next, create the pod using the nginx-mct-dev.yaml file which will house the date. Type: k apply -f nginx-mct-dev.yaml -n dev
7.check the pod is created using k get pod -n dev
8.Pod nginx-mct-dev is successfully running.
9.Exec into the pod using: k exec nginx-mct-dev -n dev -it -- sh
10.Once successfully in the pod, then ls to get to the tmp folder
11.cd to the tmp folder
12.then ls into the tmp folder
13.this should take me to the devdata folder
14.cd in devdata
15.In the devdata folder, create an echo "I now understand some parts of kubernetes" > cloud.txt
16.cat cloud.txt to see if the create echo statement is there
17.confirm that the statement above is on the cat  cloud.txt
18.Then delete the nginx yaml file, type: k delete -f nginx-mct-dev.yaml -n dev. This is to remove the folder that contains the data created with the echo statement which should be removed when the pod is deleted since pods are ephemeral. 
19.check the pod has been removed, type: k get pod -n dev
20.Now repeat, steps 6-14. This is to check that the data in the file and folder in the pod persisted/was retained even when the pod was previously deleted.
21.type ls
22.once in cloud.txt
23.cat into cloud.txt
24.the data "I now understand some parts of kubernetes" should be displayed.
