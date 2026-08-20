Imagepulledbackoff error

Possible causes:
a. When Kubernetes is trying to pull the image specified in the deployment file, caused by wrong image tagging e.g. 1.14.2. When Kubernetes is trying to pull the image from Docker hub, the correct image is not availabe. This is the error generated.

b. Wrong image name e.g nginx spelt as ngix which is the image name.
c. Wrong command start. e.g in the docker file where the app.py is incorrectly written. 
d. Wrong tag version e.g. 1.14.3 instead of 1.14.2


To fix the image pullbackoff error:
1. Type: k delete deployment nginx-deployment ###to check the deployment has been removed.
2. Type: k get deployment ###to check that the resources have been removed.
3. Type: k get pods ###to check if the pods are gone.
4. Go back to the deployment.yaml file and correct the image name.