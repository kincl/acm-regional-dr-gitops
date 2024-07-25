# Pacman in VM

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
