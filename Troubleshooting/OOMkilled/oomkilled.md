OOM Killed error:
This occurs when a memory limit specified in the yaml file is below the memory size of the required docker image being pulled. 

Demo:
1.Create a yaml file, where the a limit on the memory for the image to be pulled from Docker.
2.Run the yaml file, type:
k apply -f oom-killed.yaml
k get pods

The error "oomkilled" should appear in the pod status.

k get pods:

NAME              READY   STATUS      RESTARTS      AGE
oom-killed-demo   0/1     OOMKilled   2 (20s ago)   32s

k get events:
 Warning  BackOff    27s (x4 over 65s)  kubelet            Back-off restarting failed container memory-hog in pod oom-killed-demo_default(d5da5f52-36a3-43ec-b0cc-3c8a29512354)

Solution:
1.In the yaml file, the required memory limit should be specified to apply to the file.
2.Correct the specified limit in the yaml file to reflect the memory limit.
3.Rerun the yaml file.
