Little - Forensics
- we need to evaluate access.logs of the hidden flag on logs by using GET|POST|PUT|DELETE|PATCH
- so i used this code. at explo.py

and i got the flag.


Raw: 182.55.172.61 - - [12/Nov/2025:23:21:50 +0700] "GET /uploads/image.php?cmd=id;echo%20Gematik2025{W3b5h3ll_d3t3ct3d_fr0m_l0g} HTTP/1.1" 200 512 "-" "curl/8.5.0"
Decoded path: /uploads/image.php?cmd=id;echo Gematik2025{W3b5h3ll_d3t3ct3d_fr0m_l0g}
