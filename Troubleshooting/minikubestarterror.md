Minikube start error:

💣  Exiting due to PROVIDER_DOCKER_VERSION_EXIT_1: "docker version --format <no value>-<no value>:<no value>" exit status 1: failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
📘  Documentation: https://minikube.sigs.k8s.io/docs/drivers/docker/

Docker desktop was not up and running.

Solution:

Sign into Docker desktop.
Re run minikube start.
Issue resolved.