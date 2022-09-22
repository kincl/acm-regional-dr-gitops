function(cluster, domain) [
  {
    apiVersion: 'cert-manager.io/v1',
    kind: 'Certificate',
    metadata: {
      name: 'letsencrypt-ingress',
      namespace: 'openshift-ingress',
    },
    spec: {
      secretName: 'letsencrypt-ingress',
      duration: '2160h0m0s',
      renewBefore: '360h0m0s',
      commonName: '*.apps.' + cluster + '.' + domain,
      usages: [
        'server auth',
        'client auth',
      ],
      dnsNames: [
        '*.apps.' + cluster + '.' + domain,
      ],
      issuerRef: {
        name: 'letsencrypt',
        kind: 'ClusterIssuer',
      },
    },
  },
]