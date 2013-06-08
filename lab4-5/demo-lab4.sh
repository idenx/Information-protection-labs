python ./rsa_gen.py && cat rsa.py | md5sum && cat rsa.py | python rsa_main.py encipher public.key | python rsa_main.py decipher private.key | md5sum
