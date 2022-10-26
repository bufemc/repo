# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHhibWNhZGRvbgp0cnk6CiAgICBmcm9tIHJlc291cmNlcy5saWIuREkgaW1wb3J0IERJCiAgICBmcm9tIHJlc291cmNlcy5saWIucGx1Z2luIGltcG9ydCBydW5faG9vaywgcmVnaXN0ZXJfcm91dGVzCmV4Y2VwdCBJbXBvcnRFcnJvcjoKICAgIGZyb20gLnJlc291cmNlcy5saWIuREkgaW1wb3J0IERJCiAgICBmcm9tIC5yZXNvdXJjZXMubGliLnBsdWdpbiBpbXBvcnQgcnVuX2hvb2ssIHJlZ2lzdGVyX3JvdXRlcwoKdHJ5OgogICAgZnJvbSByZXNvdXJjZXMubGliLnV0aWwuY29tbW9uIGltcG9ydCAqCmV4Y2VwdCBJbXBvcnRFcnJvcjoKICAgIGZyb20gLnJlc291cmNlcy5saWIudXRpbC5jb21tb24gaW1wb3J0ICoKICAgIApyb290X3htbF91cmwgPSBvd25BZGRvbi5nZXRTZXR0aW5nKCdyb290X3htbCcpIG9yICJmaWxlOi8vbWFpbi54bWwiCgpyb290X3htbF91cmwgPSAgImh0dHBzOi8vZ2l0bGFiLmNvbS90aGVhcmNoaXZlczEvbGlua3MvcmF3L21haW4vbWFpbi5qc29uIgoKcGx1Z2luID0gREkucGx1Z2luCnNob3J0X2NoZWNrZXIgPSAoWwogICAgJ0FkZi5seScsIAogICAgJ0JpdC5seScsIAogICAgJ0NoaWxwLml0JywgCiAgICAnQ2xjay5ydScsIAogICAgJ0N1dHQubHknLCAKICAgICdEYS5nZCcsIAogICAgJ0dpdC5pbycsIAogICAgJ2dvby5nbCcsIAogICAgJ'
love = '0ymYzqxWljtPvNtVPNaGaIfoSOinJ50MKVaYPNXVPNtVPqCpl5xLvpfVNbtVPNtW093Yzk5WljtPvNtVPNaHT8hp3DaYPNXVPNtVPqEpUZhpaHaYPNXVPNtVPqGnT9lqP5woFpfVNbtVPNtW1EcoaxhL2ZaYPNXVPNtVPqHnJ55IIWZYzAioFpfVNbtVPNtW0qcqP5colpfVNbtVPNtW1EcoaxhL2ZaYPNXVPNtVPOqXDbXDUOfqJqcov5lo3I0MFtvYlVcPzEyMvOlo290XPxtYG4tGz9hMGbXVPNtVTqyqS9fnKA0XUWio3EsrT1fK3IloPxXPxOjoUIanJ4hpz91qTHbVv9aMKEsoTymqP88pTS0nQc1pzj+VvxXMTIzVTqyqS9fnKA0XUIloQbtp3ElXFNgCvOBo25yBtbtVPNtV2EiK2kiMluzVvOFMJSxnJ5aVUIloPOuqPOlo3I0MFN+VPO7qKWfsFVtXDbtVPNtK2qyqS9fnKA0XUIloPxXPzEyMvOsM2I0K2kcp3DbqKWfXGbXVPNtVPAxo19fo2pbMvVtHzIuMTyhMlO1pzjtCvNtr3IloU0vVPxXVPNtVTyzVTShrFuwnTIwnl5fo3qypvtcVTyhVUIloP5fo3qypvtcVTMipvOwnTIwnlOcovOmnT9lqS9wnTIwn2IlXGbXVPNtVPNtVPO1pzjtCFORFF5mMKAmnJ9hYzqyqPu1pzjcYaIloNbtVPNtpzImpT9hp2HtCFOlqJ5snT9inltvM2I0K2kcp3DvYPO1pzjcPvNtVPOcMvOlMKAjo25mMGbtVPNtVPNtVPNtVNbtVPNtVPNtVPAxo19fo2pbMvqxMJMuqJk0VP0tpzImpT9hp2HtCFOpovO7p3ElXUWyp3Oioa'
god = 'NlKX0gJyApCiAgICAgICAgaWYgb3duQWRkb24uZ2V0U2V0dGluZ0Jvb2woInVzZV9jYWNoZSIpIGFuZCBub3QgInRtZGIvc2VhcmNoIiBpbiB1cmw6CiAgICAgICAgICAgIERJLmRiLnNldCh1cmwsIHJlc3BvbnNlKQogICAgICAgIGplbl9saXN0ID0gcnVuX2hvb2soInBhcnNlX2xpc3QiLCB1cmwsIHJlc3BvbnNlKSAKICAgICAgICAjZG9fbG9nKGYnZGVmYXVsdCAtIGplbiBsaXN0ID0gXG4ge3N0cihqZW5fbGlzdCl9ICcpCiAgICAgICAgamVuX2xpc3QgPSBbcnVuX2hvb2soInByb2Nlc3NfaXRlbSIsIGl0ZW0pIGZvciBpdGVtIGluIGplbl9saXN0XQogICAgICAgIGplbl9saXN0ID0gWwogICAgICAgIHJ1bl9ob29rKCJnZXRfbWV0YWRhdGEiLCBpdGVtLCByZXR1cm5faXRlbV9vbl9mYWlsdXJlPVRydWUpIGZvciBpdGVtIGluIGplbl9saXN0CiAgICAgICAgXQogICAgICAgIHJ1bl9ob29rKCJkaXNwbGF5X2xpc3QiLCBqZW5fbGlzdCkKICAgIGVsc2U6CiAgICAgICAgcnVuX2hvb2soImRpc3BsYXlfbGlzdCIsIFtdKQoKQHBsdWdpbi5yb3V0ZSgiL3BsYXlfdmlkZW8vPHBhdGg6dmlkZW8+IikKZGVmIHBsYXlfdmlkZW8odmlkZW86IHN0cik6CiAgICBfcGxheV92aWRlbyh2aWRlbykKCmRlZiBfcGxheV92aWRlbyh2aWRlbyk6CiAgICBpbXBvcnQgYmFzZTY0CiAgICB2aWRlb19'
destiny = 'fnJ5eVQ0tWlptPvNtVPO2nJEyolN9VTWup2H2AP51pzkmLJMyK2V2ATEyL29xMFu2nJEyolxtVPNtVPNXVPNtVTyzVPpvoTyhnlV6WlOcovOmqUVbqzyxMJ8cVQbXVPNtVPNtVPO2nJEyo19fnJ5eVQ0tpaIhK2uio2fbVaOlMI9joTS5VvjtqzyxMJ8cPvNtVPNtVPNtnJLtqzyxMJ9soTyhnlN6VNbtVPNtVPNtVPNtVPOlqJ5snT9inltvpTkurI92nJEyolVfVUMcMTIiK2kcozfcVPNtVPNtVPNXVPNtVTIfp2HtBtbtVPNtVPNtVUW1oy9bo29eXPWjoTS5K3McMTIiVvjtqzyxMJ8cPtcNpTk1M2yhYaWiqKEyXPVip2I0qTyhM3ZvXDcxMJLtp2I0qTyhM3ZbXGbXVPNtVUuvoJAuMTEiov5OMTEiovtcYz9jMJ5GMKE0nJ5apltcPtcNpTk1M2yhYaWiqKEyXPViL2kyLKWsL2SwnTHvXDcxMJLtL2kyLKWsL2SwnTHbXGbXVPNtVREWYzEvYzAfMJSlK2AuL2uyXPxXVPNtVTygpT9lqPO4Lz1wPvNtVPNwrTWgLl5moTIypPtkZQNjXDbtVPNtrTWgLl5yrTIwqKEyLaIcoUEcovtvD29hqTScozIlYyWyMaWyp2tvXDbXpzIanKA0MKWspz91qTImXUOfqJqcovxXPzEyMvOgLJyhXPx6PvNtVPOjoUIanJ4hpaIhXPxXVPNtVUWyqUIlovNjPtccMvOsK25uoJIsKlN9CFNvK19gLJyhK18vBtbtVPNtMaWioFOlMKOiK2AbMJAeVTygpT9lqPOlMKOiK2AbMJAePvNtVPOlMKOiK2AbMJAeXPxXVPNtVT1unJ4bXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))