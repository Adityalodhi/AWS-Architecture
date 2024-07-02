Put server1.html file in one instance created using Auto Scalling Group, second file in the second instance and sendTraffic.py in the Bastion Host instance.
to cheack the wheather the traffic is going on both server we can run this file to send traffic.

Commands

1. for Auto scalling instances 
~ vim index.html
to run file we will use python
~ python3 -m http.server 8000

2. For Bastion host
 ~  vim sendTraffic.py
 ~  pyhton3 sendTraffic.py
