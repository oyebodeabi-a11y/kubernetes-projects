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
2.Create a yaml file using the code, mct-pv.yaml