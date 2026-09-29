# using imperative command to create 

## Create using kubectl:

kubectl create secret generic my-basic-auth-secret \
  --type=kubernetes.io/basic-auth \
  --from-literal=username=admin \
  --from-literal=password=t0p-Secretstore

  ============

### Creating and Managing Secrets
As we've already shown, one can use kubectl to create various types of Secrets. While this method is convenient for development and testing, it is not recommended for production environments due to security concerns. Instead, consider using manifest files, kustomize tool that provides better security and version control.

Using Secrets in Pods
Secrets can be used in Pods either as environment variables or as volume mounts.


kubectl delete secret <secret-name> -n <namespace>

==========

### How are Kubernetes Secrets used by a Pod
The following are the three main ways a Pod can use a Secret:

As container environment variables 
As files in a volume mounted on one or more of its containers.
By the kubelet when pulling images for the Pod — imagePullSecrets.
Using Secret data as container environment variables


### To decode the encoded strings, you can use the following command:

$ echo 'YWRtaW4=' | base64 --decode
$ echo 'cGFzc3dvcmQ=' | base64 --decode
After running the above commands you should see an output similar to the image below.

kubernetes secrets decode strings

==========


Spacelift platform

Why Spacelift
How it Works
Enterprise Deployment Options
Integrations

Terraform
Ansible
OpenTofu
See all integrations
Compare

vs Terraform Cloud
vs Terraform Enterprise
vs Atlantis
vs Generic CI/CD
backstage integration
Introducing Backstage Integration
Read article

Solutions
By Initiative


IaC at Scale

Scale your infrastructure safely and efficiently with an end-to-end workflow

Infrastructure Governance

Standardize and control infrastructure provisioning and configuration

Collaboration

Implement and automate secure, collaborative workflows

Developer Velocity

Make it easy for developers to provision and configure with a single workflow
By Use Case

CI/CD for Infrastructure
Drift Detection
Achieve Terraform at Scale
OpenTofu Migration

The Guide to Audit-Ready Infrastructure
Download now
Docs
Pricing

Resources
Resources


Blog

Learn more about Spacelift and infrastructure best practices

Partners

Our partners and their services

Events

See where we'll be next

Resource Library

eBooks, webinars, cheat sheets and tools to get you started

Case Studies

Spacelift customer stories
media guides iconmedia guide icon
Mission Guides

Essential content and resources to help you achieve IaC excellence
539.infra automation report
The Infrastructure Automation Report, 2025
Download now

About
Contact Us
About Us
Careers
Accessibility
Login
Free trial
Book a demo
Kubernetes
Kubernetes Secrets – How to Create, Use, and Manage

Kubernetes Secrets &#8211; How to Create, Use, and Manage
Divine Odazie
Updated 28 Jul 2025
·
19 min read
Kubernetes secrets
🚀 Level Up Your Infrastructure Skills
You focus on building. We’ll keep you updated. Get curated infrastructure insights that help you make smarter decisions.

Your email address
Table of contents
What are secrets in Kubernetes?
Are Kubernetes secrets secure?
Types of Kubernetes Secrets
Encoding and decoding data for Kubernetes Secrets
Ways to create Kubernetes Secrets
How to manage Kubernetes Secrets
How are Kubernetes Secrets used by a Pod
How to use Kubernetes External Secrets operator
Best practices to follow when using Kubernetes Secrets
Key points
Almost every software application has some secret data. This can range from database credentials to TLS certificates or access tokens to establish secure connections.

The platform you build your application on should provide a secure means for managing this secret data. This is why Kubernetes provides an object called a Secret to store sensitive data you might otherwise put in a Pod specification or your application container image. 

In this article,you will learn what a Kubernetes Secret is; its built-in types; ways to create, view, decode, and edit them; and how to use them in Pods. It concludes with the best practices for using Secrets.

What we will cover:

What are Kubernetes Secrets?
Are Kubernetes Secrets secure?
Types of Kubernetes Secrets
Encoding and decoding data for Kubernetes Secrets
Ways to create Kubernetes Secrets
How to manage Kubernetes Secrets
How are Kubernetes Secrets used by a Pod
How to use Kubernetes External Secrets operator
Best practices to follow when using Kubernetes Secrets
What are secrets in Kubernetes?
Kubernetes Secrets are objects used to store and manage sensitive information such as passwords, OAuth tokens, SSH keys, and API keys. The primary purpose of Secrets is to reduce the risk of exposing sensitive data while deploying applications on Kubernetes.

Instead of embedding sensitive data directly within Pods or configuration files, which could expose it to a wider audience than intended, Secrets allow Kubernetes to store and use sensitive data in a more secure and manageable way.

Are Kubernetes secrets secure?
While Kubernetes Secrets offer better security than storing sensitive data in ConfigMaps, they are not inherently highly secure by default. Kubernetes Secrets are base64-encoded and can be accessed through RBAC controls, mounted as volumes, or exposed as environment variables.

However, their biggest vulnerability is that they are stored in plaintext within etcd by default. To mitigate this risk, you must enable encryption at rest in the kube-apiserver. Additionally, improper RBAC configurations can lead to secret leaks, potentially causing downtime, performance degradation, and customer dissatisfaction.

For enhanced security, consider using an external secrets management service like HashiCorp Vault or AWS Secrets Manager. These solutions offer features such as automated secret rotation and stronger encryption, reducing the risk of exposure.

What is the difference between Docker secrets and Kubernetes Secrets?
Docker secrets work with either Docker Compose or Docker Swarm, while Kubernetes Secrets work with Kubernetes. Their purpose is the same, and the biggest difference between them is that Docker secrets are encrypted at rest by default, while for K8s Secrets, you will need to encrypt them manually. 

Learn more about Docker secrets.

Types of Kubernetes Secrets
Kubernetes supports several types of secrets:

Opaque Secrets: Opaque Secrets are used to store arbitrary user-defined data. Opaque is the default Secret type, meaning that when you don’t specify any type when creating a Secret, the secret will be considered Opaque.
Service account token Secrets: This Secret type stores a token credential that identifies a service account. It is important to note that when using this Secret type, you must ensure that the kubernetes.io/service-account.name annotation is set to an existing service account name.
Docker config Secrets: Docker config secret stores the credentials for accessing a container image registry. You use Docker config secret with one of the following type values:
kubernetes.io/dockercfg
kubernetes.io/dockerconfigjson
Basic authentication Secret: Basic authentication type stores credentials needed for basic authentication.  When using this type of Secret, the data field must contain at least one of the following keys:
username: the user name for authentication
password: the password or token for authentication
SSH authentication secrets: This Secret type stores data used in SSH authentication. When using an SSH authentication, you must specify a ssh-privatekey key-value pair in the data (or stringData) field as the SSH credential to use.
TLS Secrets: You use this Secret type to store a certificate and its associated key typically used for TLS. When using a TLS secret, you must provide the tls.key and the tls.crt key in the configuration’s data (or stringData) field. 
Bootstrap token Secrets: Youuse this Secret type to store bootstrap token data during the node bootstrap process. You typically create a bootstrap token Secret in the kube-system namespace and named it in the form bootstrap-token-<token-id>.
To learn more about these Secret types, check out their documentation.

Encoding and decoding data for Kubernetes Secrets
Let’s add the following secret to our Kubernetes cluster: “my-awesome-password”. We’ve defined a K8s manifest for creating this secret:

apiVersion: v1
kind: Secret
metadata:
 name: my-secret
type: Opaque
data:
 password: my-awesome-password
kubectl apply -f secret.yaml  
 
Error from server (BadRequest): error when creating "secret.yaml": Secret in version "v1" cannot be handled as a Secret: illegal base64 data at input byte 2
As you can see, we cannot create the secret in our cluster directly, as we need to first base64 encode it. Let’s do that before adding the password there. I will show you how to do it for Linux and MacOS:

echo -n "my-awesome-password" | base64               
bXktYXdlc29tZS1wYXNzd29yZA==
Now, we will replace the text in our Secret with its base64 option:

apiVersion: v1
kind: Secret
metadata:
 name: my-secret
type: Opaque
data:
 password: bXktYXdlc29tZS1wYXNzd29yZA==
kubectl apply -f secret.yaml         
secret/my-secret created

We can get the Secret from Kubernetes by running the following command:

kubectl get secret my-secret -o jsonpath='{.data.password}'
bXktYXdlc29tZS1wYXNzd29yZA==%
To decode the Secret, we can easily use base64 again:

kubectl get secret my-secret -o jsonpath='{.data.password}' | base64 --decode

my-awesome-password%

If you don’t want to encode the data manually as shown before, you have an alternative, by creating the secret imperatively:

kubectl create secret generic my-other-secret --from-literal=password=secret
secret/my-other-secret created
To get the base64 encoded value, we can run:

kubectl get secret my-other-secret -o jsonpath='{.data.password}'
c2VjcmV0%
Also, to get the decoded value, we can run:

kubectl get secret my-other-secret -o jsonpath='{.data.password}' | base64 --decode
secret%
Ways to create Kubernetes Secrets
To create Kubernetes Secrets, you can use one of the following methods:

Use kubectl
Use a manifest file
Use a generator like Kustomize
The following are key points about creating Kubernetes Secrets:

You create Secrets outside of pods — you create a Secret before any pod can use it.
When you create a Secret, it is stored inside the Kubernetes data store (i.e., an etcd database) on the Kubernetes control plane. 

When creating a Secret, you specify the data and/or stringData fields. The values for all the data field keys must be base64-encoded strings. Suppose you don’t want to convert to base64. In that case, you can choose to specify the stringData field instead, which accepts arbitrary strings as values.
When creating Secrets, you are limited to 1MB per Secret. This is to discourage the creation of very large Secrets that could exhaust the kube-apiserver and kubelet memory. 
Also, when creating Secrets, you can mark them as immutable with immutable: true. Preventing changes to the Secret data after creation. Marking a Secret as immutable protects from accidental or unwanted updates that could cause application outages.
After creating a Secret, you inject it into a Pod either by mounting it as data volumes, exposing it as environment variables, or as imagePullSecrets. You will learn more about this later in this article. Kubernetes imagePullPolicy contains more information.
Prerequisites
Before you learn how to use each of the above methods, ensure you have the following prerequisites:

A Kubernetes cluster: The demos in this article were done using minikube — a single Node Kubernetes cluster.
The kubectl command-line tool configured to communicate with the cluster.
For demo purposes, the Secrets you will create below will store hypothetical credentials (username — admin and password — paassword) required by Pods to access a database. 

Also, create a namespace to store the demo resources for easy cleanup:

$ kubectl create namespace secrets-demo
1. Create Kubernetes Secrets using kubectl
kubectl create secret is a command used to generate Kubernetes Secret objects that store sensitive data such as passwords, tokens, or keys. It allows administrators to securely inject confidential information into containers without hardcoding it in configurations or images.

This method ensures sensitive data is stored base64-encoded in etcd and accessible to pods via environment variables or mounted volumes. Proper RBAC and encryption policies should be in place to safeguard access.

There are two ways of providing the Secret data to kubectl when creating Secrets using Kubectl, and there are:

Providing the secret data through a file using the --from-file=<filename> tag or
Providing the literal secret data using the --from-literal=<key>=<value> tag
This article will use the file method.

It is important to note that when providing the secret data --from-literal=<key>=<value> tag, special characters such as $, \, *, =, and ! require escaping. However, you can easily escape in most shells with single quotes (‘).

To start creating a Secret with kubectl providing the Secret data from a file in any directory of your choice. Create files to store the hypothetical user credentials with the following command:

$ echo -n 'admin' > username.txt
$ echo -n 'password' > password.txt
The -n flag in the above command ensures that no newline character is added at the end of the text. This is crucial since kubectl will encode the extra newline character if present when it reads the file and turns the content into a base64 string.

After running the above commands, you can verify that the password and username were written to the file with the cat command, as in the image below.

kubernetes secrets verify password
Now, create the Kubernetes Secret with the files using the kubectl command below:

$ kubectl create secret generic database-credentials \  
    --from-file=username.txt \ 
    --from-file=password.txt \
    --namespace=secrets-demo
    
The generic subcommand tells kubectl to create the Secret with Opaque type. The above command will output the following:

kubernetes secrets Opaque type
Note: When using the above command, the key of your secret data will be the filename (username.txt and password.txt) by default.  To provide keys for the Secret data, use the following syntax --from-file=[key=]source, for example:

kubectl create secret generic database-credentials \
--from-file=username=username.txt \
--from-file=password=password.txt \
--namespace=secrets-demo
To verify the Secret creation, run the following command:

$ kubectl -n secrets-demo get secrets
The above command will show an output similar to the image below.

kubernetes secrets opaque type verify
2. Create Kubernetes Secrets from a YAML manifest file
Before you create a Secret using a manifest file, you must first decide how you want to add the Secret data using the data field and/or the stringData field.

Using the data field, you must encode the secret data using base64.  To convert the username and password to base64, run the following command:

echo -n 'admin' | base64
echo -n 'password' | base64
After running the above command, you will get an output similar to the image below. Copy the base64 values and store them to put in your manifest file.

kubernetes secrets base64
Now create a demo-secret.yaml manifest file using your preferred method (text editor, vim or nano, etc.) and add the following configuration.

apiVersion: v1
kind: Secret
metadata:
  name: demo-secret
type: Opaque
data:
  username: YWRtaW4=
  password: cGFzc3dvcmQ=
In the above manifest file, the username and password values in the data field are the base64 encoded values of the original credentials. 

When using the stringData field, the manifest file will be:

apiVersion: v1
kind: Secret
metadata:
  name: demo-secret
type: Opaque
stringData:
  username: admin
  password: password
To create the Secret, run the following command:

$ kubectl -n secrets-demo apply -f demo-secret.yaml
After running the above command, you should get an output similar to the image below.

create kubernetes secrets manifest file
💡 You might also like:

26 Top Kubernetes Tools for Your K8s Ecosystem
15 Kubernetes Best Practices to Follow
How to Maintain Operations Around Kubernetes Cluster
3. Create Kubernetes Secrets with a generator like Kustomize
Using a resource Generator like Kustomize can help you create Kubernetes Secrets quickly.

To create a Secret using Kustomize, first create a kustomization.yaml file. In that file, define a secretGenerator to reference one of the following:

Files that store the secret data,
The unencrypted literal version of the secret data values,
Environment variable (.env) files.
You don’t need to base64 encode the values with all these methods.

When referencing Secret data files, you define the secretGenerator like this:

secretGenerator:
- name: database-credentials
  files:
  - username.txt
  - password.txt
When using the literal version of the data values, you define the secretGenerator like this:

secretGenerator:
- name: database-credentials
  literals:
  - username=admin
  - password=password
When using .env files, you define the secretGenerator like:

secretGenerator:
- name: database-credentials
  envs:
  - .env.secret
Create the kustomization.yaml file, and paste either of the first two options.

Then in the same directory as the file, generate the Secret with the following kubectl command:

$ kubectl -n secrets-demo apply -k .
After running the above command, you should see an output similar to the image below.

create kubernetes secrets with kustomize
So far, you’ve learned what Kubernetes secrets are, its built-in types, and the methods you can use to create them. Next, you will learn how to describe a Secret, decode a Secret, edit Secret values, and finally, how to use a Secret in Pods. 

Check out our Kustomize vs. Helm comparison.

How to manage Kubernetes Secrets
Here’s an overview of the main actions you can perform with Kubernetes Secrets.

List existing Kubernetes Secrets
To list Secrets we can simply run the following command:

kubectl get secrets                                                               
NAME              TYPE     DATA   AGE
my-other-secret   Opaque   1      2m23s
my-secret         Opaque   1      5m39s
To get more details about the Secrets, we can use the describe option for kubectl:

kubectl describe secrets
Name:         my-other-secret
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
password:  6 bytes


Name:         my-secret
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
password:  19 bytes
Secrets are namespaced resources, so you can use the -n option to get the Secrets from a specific namespace, or you can use –all-namespaces to get the secrets from all the namespaces. By default, the default namespace will be used.

kubectl get secrets -n space       
NAME             TYPE     DATA   AGE
awesome-secret   Opaque   1      26s

kubectl get secrets --all-namespaces
NAMESPACE   NAME              TYPE     DATA   AGE
default     my-other-secret   Opaque   1      5m22s
default     my-secret         Opaque   1      8m38s
space       awesome-secret    Opaque   1      32s
View a Kubernetes Secret value with kubectl describe
Using the kubectl describe, you can view some basic information about Kubernetes objects. To use it to view the description of one of the Secrets you’ve created in the article, run:

$ kubectl -n secrets-demo describe secrets/database-credentials

After running the above command, you will get an output similar to the image below.

kubernetes secret kubectl describe
As you can see, the above output doesn’t show the Secret’s contents. This is to protect the Secret from being exposed or logged in the terminal.

To view the Secret data, you will need to decode the secret. 

Decode a Kubernetes Secret
To view the data of the Secret you created, run the following command:

$ kubectl -n secrets-demo get secret database-credentials -o jsonpath='{.data}'
After running the above commands, it will output the encoded key-value pairs of the secret data as in the image below. 

kubernetes secrets encoded key-value pairs
To decode the encoded strings, you can use the following command:

$ echo 'YWRtaW4=' | base64 --decode
$ echo 'cGFzc3dvcmQ=' | base64 --decode
After running the above commands you should see an output similar to the image below.

kubernetes secrets decode strings
Note: If you do the above, you could store the Secret data in your shell history. To avoid that, combine the previous two steps into one command like the one below.

$ kubectl get secret database-credentials -o jsonpath='{.data.password}' | base64 --decode
Edit a Kubernetes Secret
To edit the content of the Secret you created, run the following kubectl command:

$ kubectl -n secrets-demo edit secrets database-credentials
The above command will open your terminal’s default editor to allow you to update the base64 encoded Secret data in the data field as in the image below.

editing kubernetes secrets
Note: It is important to note that when you set a Secret as immutable upon creation, you can’t edit it. Nonetheless, you can edit any existing mutable Secret to make it immutable by adding immutable: true in the manifest file like the following:

apiVersion: v1
kind: Secret
metadata:
  ...
data:
  ...
immutable: true
Delete a Kubernetes Secret
Clean up the entire setup by deleting the namespace, which deletes all the secrets and Pods you created with the following command:

kubectl delete secret <secret-name> -n <namespace>
How are Kubernetes Secrets used by a Pod
The following are the three main ways a Pod can use a Secret:

As container environment variables 
As files in a volume mounted on one or more of its containers.
By the kubelet when pulling images for the Pod — imagePullSecrets.
Using Secret data as container environment variables
For demo purposes, below is a Pod manifest with the Kubernetes Secret data you created exposed as environment variables. Create a secret-test-env-pod.yaml and paste the configuration in it.

apiVersion: v1
kind: Pod
metadata:
  name: env-pod
spec:
  containers:
    - name: secret-test
      image: nginx
      command: ['sh', '-c', 'echo "Username: $USER" "Password: $PASSWORD"']
      env:
        - name: USER
          valueFrom:
            secretKeyRef:
              name: database-credentials
              key: username.txt
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              name: database-credentials
              key: password.txt




kubectl -n secrets-demo apply -f secret-test-evn-pod.yaml

$ kubectl -n secrets-demo describe pod env-pod



After running the above command, you should see an output similar to the image below.

kubernetes secrets env-pod


Also, seeing the echo command in the Pod manifest file, you can verify by checking the logs of the Pod with:

$ kubectl -n secrets-demo logs env-pod

===========