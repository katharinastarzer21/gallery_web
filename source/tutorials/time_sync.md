# VM Time Synchronisation

This quick overview explains how to handle VM Time Synchronisation.
Time synchronisation is a critical component, with many components relying on accurate time stamps. 
All current VM images at EODC include time synchronisation based on chrony and precision time devices.

On these VMs no action is needed to ensure accurate time synchronisation.

Our default configs ensure your VMs have consistent time even across the largest clusters.

To confirm this, the following command can be used:

```
[eodc@eodc ~]$ chronyc sourcestats
Name/IP Address            NP  NR  Span  Frequency  Freq Skew  Offset  Std Dev
==============================================================================
PHC0                        6   3    21     -0.000      0.001     -0ns     2ns
```

If instead of PHC0 as source, something else is shown, and you have not manually changed time synchronisation settings, then most likely an old image base is used.


For VMs that were created before this was included by default, this functionality can be added.
To do so, simply execute, 

`/eodc/products/.config/configure-crony-ptp_kvm.sh`

with sudo priviledges.

**Please note, acccess to NTP servers outside EODC is not typically possible. Contact us with your requirements if this is an issue.**
