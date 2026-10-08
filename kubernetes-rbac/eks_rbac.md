#################### EKS Cluster RBACs #############################################################################
# kubernetes-rbac
kubernetes rbac configuration is done to help with access control and permission of any staff all done within the aws infrastructure and ecosytem

## first create the rbac-test namespace, and then install nginx into it
kubectl create namespace rbac-test

## Deploy nginx pod on clsuster
kubectl create deploy nginx --image=nginx -n rbac-test

## To verify the test pods were properly installed
kubectl get all -n rbac-test
## get status of the ngnx pod

kubectl get pods -n rbac-test 

# ==========================================
## Create IAM user and create access key
aws iam create-user --user-name rbac-user


# once user was created creates access key

aws iam create-access-key --user-name rbac-user

# now the new Iam user created does not have acess to kubernetes RBAC

### Now log into the terminal as the newly created rbac-user where u are not the admin and
 ### use the newly generated Iam accesskey and secret to authenticate into aws

aws configure
access_key:-------
secret-key:--------


# after the above run to the below to confirm if authenticated in aws for rbac-user
aws sts get-caller-identity
{
    "UserId": "",
    "Account": "",
    "Arn": "arn:aws:iam::user/rbac-user"
}

## We will use this to set another context with using above credentials
AWS configure.


# use the file below to map the rbac-user
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapUsers: |
    - userarn: arn:aws:iam::759623136685:user/rbac-user
      username: rbac-user

## MAP Rbac-user TO K8S

kubectl apply -f ./aws-auth.yaml

Warning: resource configmaps/aws-auth is missing the
 kubectl.kubernetes.io/last-applied-configuration annotation which is required by
  kubectl apply. kubectl apply should only be used on resources created declaratively 
  by either kubectl create --save-config or kubectl apply.
   The missing annotation will be patched automatically.
configmap/aws-auth configured

# now login into the terminal as rbac-user by runing the command below

aws configure
access_key:-------
secret-key:--------


# after run the below command to confirm your indenity

aws sts get-caller-identity 


## Verify newly created user after login AND it should throw below errors
kubectl get pods -n rbac-test
## error: You must be logged in to the server (Unauthorized)-----this
one use case that proves that a user without administratieve access cannot come and 
#do stuffs

# now log in with your administrative access
aws configure


# now run the aws sts-get-caller-identity

# Now run the command
kubectl get pods -n rbac-test
NAME                    READY   STATUS    RESTARTS   AGE
nginx-bf5d5cf98-gdhrp   1/1     Running   0          138m

# the above shows the point we are talking about by default 
the rbac-user gets the inheritance and get the administrative priviledge

## Create a role within the rbac-test namespace from Admin access

kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: rbac-test
  name: pod-reader
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods"]
  verbs: ["list","get","watch"]
- apiGroups: ["extensions","apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch"]

kubectl apply -f ./rbacuser-role.yaml

### Create a rolebinding within the rbac-test namespace from Admin access

kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-pods
  namespace: rbac-test
subjects:
- kind: User
  name: rbac-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io

kubectl apply -f ./rbacuser-role-binding.yaml

rolebinding.rbac.authorization.k8s.io/read-pods created

## login with Kubernetes rbac-user again
using below command and with its accesskey and secret key
 aws configure

 ## confirm it is rbac-user
 aws sts get-caller-identity


## Verify newly created user after login AND it should Not throw any errors
kubectl get pods -n rbac-test                
NAME                    READY   STATUS    RESTARTS   AGE
nginx-bf5d5cf98-gdhrp   1/1     Running   0          3h52m

## Now Verify newly created rbac-user after does not have access in another name space except that created for it  AND it should throw errors
kubectl get pods -n kube-system

kubectl get deployment -n rbac-test
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   1/1     1            1           3h54m

kubectl describe pod nginx-bf5d5

kubectl describe pod nginx-bf5d5cf98-gdhrp -n rbac-test 
Name:             nginx-bf5d5cf98-gdhrp
Namespace:        rbac-test
Priority:         0



# now if the same user tries to do anything in another namespace like kube-system he will not be permitted, 
 ### this is how we restrict users in a big kubernetes team.
This is how roles and and rolebinding are done called Role based access configuration
####################################################################################################################