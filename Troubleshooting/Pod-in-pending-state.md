### Scenario 1: You are a cloud engineer and have deployed a pod and the pod is stuck  in pending state.

It means the pod has not been scheduled to run in the nodes.

E0818 10:33:49.050360   19992 memcache.go:265] "Unhandled Error" err="couldn't get current server API group list: Get \"http://localhost:8080/api?timeout=32s\": dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it."
Unable to connect to the server: dial tcp [::1]:8080: connectex: No connection could be made because the target machine actively refused it.

Solution:
First check for the nodes status
Kubectl get nodes

#secondly inspect the pods
Kubectl get pods
Kubectl describe  pod <podnamne>

#check resources
By checking the pods yam file to check resources allocation

#Check events
Kubectl get events

#check pv
#Check if the pod uses persistent volume then check if the request volume are not in conflicting state

#check if networking configuration is correct

