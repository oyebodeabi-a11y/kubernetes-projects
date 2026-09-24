### Using Secret data as files in a volume mounted on a Pod’s container(s)

For demo purposes, below is a Pod manifest with the Kubernetes Secret data you created as files in a volume mounted on the Pod’s containers. 

### Create a secret-test-volume-pod.yaml and paste the configuration in it.

apiVersion: v1
kind: Pod
metadata: 
  name: volume-test-pod
spec:
  containers:
  - name: secret-test
    image: nginx
    volumeMounts:
    - name: secret-volume
      mountPath: /etc/config/secret
  volumes:
  - name: secret-volume
    secret:
      secretName: database-credentials

kubectl -n secrets-demo apply -f secret-test-volume-pod.yaml


## To verify that the Pod can access the Secret data, connect to the container and run the following commands in the volume directory:

$ kubectl -n secrets-demo exec volume-test-pod -- cat /etc/config/secret/username.txt

$ kubectl -n secrets-demo exec volume-test-pod -- cat /etc/config/secret/password.txt

$ kubectl -n secrets-demo exec volume-test-pod -- ls /etc/config/secret
The above commands will have an output similar to the image below.

volume mounted on a Pod’s container