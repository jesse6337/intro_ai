import partical
import plotly.express as px
import random
import numpy as np

# a side view of the map of a geographical region
# 150 columns (length) and 10 rows (height)
map1 = ['                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '                                                                                                                                                      ',
        '          ^^  ^^                      ^^                                                 ^^^                   ^^^^^               ^^^                ',
        '    ^^  ^^^^^^^^^^       ^^   ^^     ^^^^                                           ^^  ^^^^^     ^^          ^^^^^^^^           ^^^^^^^    ^^^       ',
        '  ^^^^^^^^^^^^^^^^^^   ^^^^^^^^^^   ^^^^^^  ^^  ^^                                 ^^^^^^^^^^^   ^^^^^  ^^  ^^^^^^^^^^^^  ^^  ^^^^^^^^^^^^^^^^^^^^    ',
        '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ',
        '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^_________________________^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^']
p = partical.partical(map1, 5)

print(p)
p.move(-6)
print(p)
parts = [partical.partical(map1, random.randint(0, len(map1[0]))) for i in range(1000)]
print(parts)

