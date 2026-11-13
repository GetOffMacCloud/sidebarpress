"""Regenerate every token: portraits (tokens.py), crocodiles (tokens2.py), other creatures (tokens3.py)."""
import runpy,os
H=os.path.dirname(os.path.abspath(__file__))
for f in ('tokens.py','tokens2.py','tokens3.py'): runpy.run_path(os.path.join(H,f),run_name='__main__')
