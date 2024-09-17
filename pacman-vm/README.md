# Pacman in VM

## configuration in vm

```
podman pod create -p 8080:8080 --name pacman
podman run -dt -v /srv:/bitnami/mongodb --name mongodb --pod pacman bitnami/mongodb:5.0.9
podman run -dt --name pacman-app --pod pacman quay.io/jpacker/nodejs-pacman-app:latest
```

## old config, now not needed with source.yaml
- Get latest CentOS Stream 9 VM image

```
curl -LO https://cloud.centos.org/centos/9-stream/x86_64/images/CentOS-Stream-GenericCloud-x86_64-9-latest.x86_64.qcow2
```

- Upload as a PVC with `virtctl`

```
$ virtctl image-upload -n testing pvc centos-test --size=50Gi --image-path CentOS-Stream-GenericCloud-x86_64-9-latest.x86_64.qcow2 --storage-class ocs-storagecluster-ceph-rbd-virtualization
PVC testing/centos-test not found
PersistentVolumeClaim testing/centos-test created
Waiting for PVC centos-test upload pod to be ready...
Pod now ready
Uploading data to https://cdi-uploadproxy-openshift-cnv.apps.cluster-west.sandbox347.opentlc.com

 1.14 GiB / 1.14 GiB [===============================================================] 100.00% 47s

Uploading data completed successfully, waiting for processing to complete, you can hit ctrl-c without interrupting the progress
Processing completed successfully
Uploading CentOS-Stream-GenericCloud-x86_64-9-latest.x86_64.qcow2 completed successfully
```

## Resources

- https://github.com/RamenDR/ocm-ramen-samples/blob/98ffce56163ad38b5ec0eb0a771c0bd2fbdc381f/workloads/kubevirt/vm-pvc/base/pvc.yaml
- https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.16/html-single/configuring_openshift_data_foundation_disaster_recovery_for_openshift_workloads/index
- https://access.redhat.com/articles/7041594#6-using-openshift-gitops-with-openshift-virtualization-in-dr-scenarios-24
