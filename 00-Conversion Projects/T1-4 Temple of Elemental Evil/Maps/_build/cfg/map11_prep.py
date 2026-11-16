"""Map 11 The Temple: deskew the scan (sv=+0.0025, sh=-0.0025) and remove the printed grid -> maps/raw/map11_clean.png"""
import subprocess, os
env = dict(os.environ, SKEW='0.0025,-0.0025', SAVE_I='maps/raw/map11_I.png')
subprocess.run(['python3', 'scripts/raw_degrid.py', 'maps/raw/pg-007.jpg', '40,85,1075,1330', '28.54,9.0,28.82,14.25',
                'maps/raw/map11_clean.png', '175', '1.8', '4', '2', '9', '3'], check=True, env=env)
