python rsa_gen.py && cat rsa_main.py | python create_signature.py private.key >signature && cat rsa_main.py | python check_signature.py signature public.key
