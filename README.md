# multicloud-gitops

aka gitops for testing ODF Regional-DR

## Hub

The hub cluster needs to be configured with items in `acm-gitops/` directory.

| File | Purpose |
| ---- | ------- |
| argocd.yaml | Changes to the OpenShift GitOps cluster install of Argo CD |
| gitopscluster.yaml, placement.yaml | Sets up the link between ACM and openshift-gitops |

Once the links are made, ACM will populate the clusters based on the placement rule in the Argo CD instance in the openshift-gitops namespace.

## ApplicationSet

ApplicationSets are from Argo CD and are used to template out Applications which deploy manifests to a Kubernetes cluster.

The web interface for the Cluster Argo CD can be accessed from the top ribbon of the OpenShift Console:

![](images/cluster-argocd.png)

The ApplicationSets are in the `applications/` directory.

| File | Purpose |
| ---- | ------- |
| placement.yaml | Describes the custom resources that are used by the ApplicationSet to get a list of clusters to create Applications from it's template |
| cert-manager.yaml | Deploys cert-manager with upstream Helm chart (needed because we need v1.9.1) from `cert-manager/` |
| cluster-certificates.yaml | Uses cert-manager to get signed certificates for cluster default ingress controller from `cluster-certificates/` |
| odf-operator.yaml | Deploys ODF from `odf/` |