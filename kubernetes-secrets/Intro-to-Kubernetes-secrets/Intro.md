Introduction to Kubernetes secrets:

Where is important secrets data stored in Kubernetes: It is stored is ETCD.

we can add secret in kubernetes in two ways using the imperative comnmand and yaml file:
## imperative command below

kubectl create secret generic secretname --from-literal=username1=dXNlcm5hbWU= --from-literal=password1=dXNlcm5hbWU=

kubectl create secret generic abisecret --from-literal=username1=ZGlhbW9uZGltYWdlMTU= --from-literal=password1=ZnJpeWF5bW9tZW50MDU=



## to know more about the secret created
  kubectl get secret <secretname> -o yaml


## Using yaml file below
however the yaml file can be in string data where you add the username and value

create-secret.yaml

apiVersion: v1
kind: Secret
metadata:
 name: secret-demo
type: Opaque
stringData:
 username: admin
 password: admin123

 ## now create secret but first check if there is secret
 kubectl get secret

 ## now create secret
 kubectl create secret.yaml

 # output

 ## now check if there is secret
 kubectl get secret

 ## to know more
  kubectl get secret <secretname> -o yaml

  ## to describe secret

  kubectl describe secret <secretnsme>


### To decode the encoded strings, you can use the following command:

$ echo 'YWRtaW4=' | base64 --decode

$ echo 'cGFzc3dvcmQ=' | base64 --decode

### to make it more clear

 $ echo 'YWRtaW4=' | base64 --decode : echo
### now to consume the secret