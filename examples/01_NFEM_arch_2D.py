"""
from Tr_02_Arch.xlsx
"""
# add the path to the nfem tool to the PATH.
import sys
sys.path.append('..') 
# import necessary modules
import numpy as np

from nfem import *

model = Model("Arch2D")

# --- Nodes
model.add_node(id=1,  x=-33.9411255 , y= 33.9411255, z=0)
model.add_node(id=2,  x=-35.35533906, y= 35.3553390, z=0)
model.add_node(id=3,  x=-31.17350632, y= 36.4994863, z=0)
model.add_node(id=4,  x=-32.47240242, y= 38.0202982, z=0)
model.add_node(id=5,  x=-28.21369211, y= 38.8328157, z=0)
model.add_node(id=6,  x=-29.38926261, y= 40.4508497, z=0)
model.add_node(id=7,  x=-25.07993111, y= 40.9267278, z=0)
model.add_node(id=8,  x=-26.12492824, y= 42.6320082, z=0)
model.add_node(id=9,  x=-21.79154399, y= 42.7683131, z=0)
model.add_node(id=10, x=-22.69952499, y= 44.5503262, z=0)
model.add_node(id=11, x=-18.36880475, y= 44.3462175, z=0)
model.add_node(id=12, x=-19.13417162, y= 46.1939766, z=0)
model.add_node(id=13, x=-14.83281573, y= 45.6507127, z=0)
model.add_node(id=14, x=-15.45084972, y= 47.5528258, z=0)
model.add_node(id=15, x=-11.20537747, y= 46.6737561, z=0)
model.add_node(id=16, x=-11.67226819, y= 48.6184960, z=0)
model.add_node(id=17, x=-7.508854322, y= 47.4090403, z=0)
model.add_node(id=18, x=-7.821723252, y= 49.3844170, z=0)
model.add_node(id=19, x=-3.766036595, y= 47.8520320, z=0)
model.add_node(id=20, x=-3.922954786, y= 49.8458666, z=0)
model.add_node(id=21, x= 0          , y= 48        , z=0)
model.add_node(id=22, x= 0          , y= 50        , z=0)
model.add_node(id=23, x= 3.766036595, y=47.85203202, z=0)
model.add_node(id=24, x= 3.922954786, y=49.84586669, z=0)
model.add_node(id=25, x= 7.508854322, y=47.40904035, z=0)
model.add_node(id=26, x= 7.821723252, y=49.38441703, z=0)
model.add_node(id=27, x= 11.20537747, y=46.67375618, z=0)
model.add_node(id=28, x= 11.67226819, y=48.61849602, z=0)
model.add_node(id=29, x= 14.83281573, y=45.65071278, z=0)
model.add_node(id=30, x= 15.45084972, y=47.55282581, z=0)
model.add_node(id=31, x= 18.36880475, y=44.34621756, z=0)
model.add_node(id=32, x= 19.13417162, y=46.19397663, z=0)
model.add_node(id=33, x= 21.79154399, y=42.76831316, z=0)
model.add_node(id=34, x= 22.69952499, y=44.55032621, z=0)
model.add_node(id=35, x= 25.07993111, y=40.92672789, z=0)
model.add_node(id=36, x= 26.12492824, y=42.63200822, z=0)
model.add_node(id=37, x= 28.21369211, y=38.83281573, z=0)
model.add_node(id=38, x= 29.38926261, y=40.45084972, z=0)
model.add_node(id=39, x= 31.17350632, y=36.49948635, z=0)
model.add_node(id=40, x= 32.47240242, y=38.02029828, z=0)
model.add_node(id=41, x= 33.9411255	, y=33.9411255 , z=0)
model.add_node(id=42, x= 35.35533906, y=35.35533906, z=0)

# --- Elements
model.add_truss_element(id=1, node_a=1, node_b=3, youngs_modulus=1, area=1)      
model.add_truss_element(id=2, node_a=3, node_b=5, youngs_modulus=1, area=1)
model.add_truss_element(id=3, node_a=5, node_b=7, youngs_modulus=1, area=1)
model.add_truss_element(id=4, node_a=7, node_b=9, youngs_modulus=1, area=1)
model.add_truss_element(id=5, node_a=9, node_b=11, youngs_modulus=1, area=1)
model.add_truss_element(id=6, node_a=11, node_b=13, youngs_modulus=1, area=1)
model.add_truss_element(id=7, node_a=13, node_b=15, youngs_modulus=1, area=1)
model.add_truss_element(id=8, node_a=15, node_b=17, youngs_modulus=1, area=1)
model.add_truss_element(id=9, node_a=17, node_b=19, youngs_modulus=1, area=1)
model.add_truss_element(id=10, node_a=19, node_b=21, youngs_modulus=1, area=1)
model.add_truss_element(id=11, node_a=21, node_b=23, youngs_modulus=1, area=1)
model.add_truss_element(id=12, node_a=23, node_b=25, youngs_modulus=1, area=1)
model.add_truss_element(id=13, node_a=25, node_b=27, youngs_modulus=1, area=1)
model.add_truss_element(id=14, node_a=27, node_b=29, youngs_modulus=1, area=1)
model.add_truss_element(id=15, node_a=29, node_b=31, youngs_modulus=1, area=1)
model.add_truss_element(id=16, node_a=31, node_b=33, youngs_modulus=1, area=1)
model.add_truss_element(id=17, node_a=33, node_b=35, youngs_modulus=1, area=1)
model.add_truss_element(id=18, node_a=35, node_b=37, youngs_modulus=1, area=1)
model.add_truss_element(id=19, node_a=37, node_b=39, youngs_modulus=1, area=1)
model.add_truss_element(id=20, node_a=39, node_b=41, youngs_modulus=1, area=1)
model.add_truss_element(id=21, node_a=2, node_b=4, youngs_modulus=1, area=1)
model.add_truss_element(id=22, node_a=4, node_b=6, youngs_modulus=1, area=1)
model.add_truss_element(id=23, node_a=6, node_b=8, youngs_modulus=1, area=1)
model.add_truss_element(id=24, node_a=8, node_b=10, youngs_modulus=1, area=1)
model.add_truss_element(id=25, node_a=10, node_b=12, youngs_modulus=1, area=1)
model.add_truss_element(id=26, node_a=12, node_b=14, youngs_modulus=1, area=1)
model.add_truss_element(id=27, node_a=14, node_b=16, youngs_modulus=1, area=1)
model.add_truss_element(id=28, node_a=16, node_b=18, youngs_modulus=1, area=1)
model.add_truss_element(id=29, node_a=18, node_b=20, youngs_modulus=1, area=1)
model.add_truss_element(id=30, node_a=20, node_b=22, youngs_modulus=1, area=1)
model.add_truss_element(id=31, node_a=22, node_b=24, youngs_modulus=1, area=1)
model.add_truss_element(id=32, node_a=24, node_b=26, youngs_modulus=1, area=1)
model.add_truss_element(id=33, node_a=26, node_b=28, youngs_modulus=1, area=1)
model.add_truss_element(id=34, node_a=28, node_b=30, youngs_modulus=1, area=1)
model.add_truss_element(id=35, node_a=30, node_b=32, youngs_modulus=1, area=1)
model.add_truss_element(id=36, node_a=32, node_b=34, youngs_modulus=1, area=1)
model.add_truss_element(id=37, node_a=34, node_b=36, youngs_modulus=1, area=1)
model.add_truss_element(id=38, node_a=36, node_b=38, youngs_modulus=1, area=1)
model.add_truss_element(id=39, node_a=38, node_b=40, youngs_modulus=1, area=1)
model.add_truss_element(id=40, node_a=40, node_b=42, youngs_modulus=1, area=1)
model.add_truss_element(id=41, node_a=1, node_b=4, youngs_modulus=1, area=1)
model.add_truss_element(id=42, node_a=3, node_b=6, youngs_modulus=1, area=1)
model.add_truss_element(id=43, node_a=5, node_b=8, youngs_modulus=1, area=1)
model.add_truss_element(id=44, node_a=7, node_b=10, youngs_modulus=1, area=1)
model.add_truss_element(id=45, node_a=9, node_b=12, youngs_modulus=1, area=1)
model.add_truss_element(id=46, node_a=11, node_b=14, youngs_modulus=1, area=1)
model.add_truss_element(id=47, node_a=13, node_b=16, youngs_modulus=1, area=1)
model.add_truss_element(id=48, node_a=15, node_b=18, youngs_modulus=1, area=1)
model.add_truss_element(id=49, node_a=17, node_b=20, youngs_modulus=1, area=1)
model.add_truss_element(id=50, node_a=19, node_b=22, youngs_modulus=1, area=1)
model.add_truss_element(id=51, node_a=21, node_b=24, youngs_modulus=1, area=1)
model.add_truss_element(id=52, node_a=23, node_b=26, youngs_modulus=1, area=1)
model.add_truss_element(id=53, node_a=25, node_b=28, youngs_modulus=1, area=1)
model.add_truss_element(id=54, node_a=27, node_b=30, youngs_modulus=1, area=1)
model.add_truss_element(id=55, node_a=29, node_b=32, youngs_modulus=1, area=1)
model.add_truss_element(id=56, node_a=31, node_b=34, youngs_modulus=1, area=1)
model.add_truss_element(id=57, node_a=33, node_b=36, youngs_modulus=1, area=1)
model.add_truss_element(id=58, node_a=35, node_b=38, youngs_modulus=1, area=1)
model.add_truss_element(id=59, node_a=37, node_b=40, youngs_modulus=1, area=1)
model.add_truss_element(id=60, node_a=39, node_b=42, youngs_modulus=1, area=1)
model.add_truss_element(id=61, node_a=2, node_b=3, youngs_modulus=1, area=1)
model.add_truss_element(id=62, node_a=4, node_b=5, youngs_modulus=1, area=1)
model.add_truss_element(id=63, node_a=6, node_b=7, youngs_modulus=1, area=1)
model.add_truss_element(id=64, node_a=8, node_b=9, youngs_modulus=1, area=1)
model.add_truss_element(id=65, node_a=10, node_b=11, youngs_modulus=1, area=1)
model.add_truss_element(id=66, node_a=12, node_b=13, youngs_modulus=1, area=1)
model.add_truss_element(id=67, node_a=14, node_b=15, youngs_modulus=1, area=1)
model.add_truss_element(id=68, node_a=16, node_b=17, youngs_modulus=1, area=1)
model.add_truss_element(id=69, node_a=18, node_b=19, youngs_modulus=1, area=1)
model.add_truss_element(id=70, node_a=20, node_b=21, youngs_modulus=1, area=1)
model.add_truss_element(id=71, node_a=22, node_b=23, youngs_modulus=1, area=1)
model.add_truss_element(id=72, node_a=24, node_b=25, youngs_modulus=1, area=1)
model.add_truss_element(id=73, node_a=26, node_b=27, youngs_modulus=1, area=1)
model.add_truss_element(id=74, node_a=28, node_b=29, youngs_modulus=1, area=1)
model.add_truss_element(id=75, node_a=30, node_b=31, youngs_modulus=1, area=1)
model.add_truss_element(id=76, node_a=32, node_b=33, youngs_modulus=1, area=1)
model.add_truss_element(id=77, node_a=34, node_b=35, youngs_modulus=1, area=1)
model.add_truss_element(id=78, node_a=36, node_b=37, youngs_modulus=1, area=1)
model.add_truss_element(id=79, node_a=38, node_b=39, youngs_modulus=1, area=1)
model.add_truss_element(id=80, node_a=40, node_b=41, youngs_modulus=1, area=1)
model.add_truss_element(id=81, node_a=1, node_b=2, youngs_modulus=1, area=1)
model.add_truss_element(id=82, node_a=3, node_b=4, youngs_modulus=1, area=1)
model.add_truss_element(id=83, node_a=5, node_b=6, youngs_modulus=1, area=1)
model.add_truss_element(id=84, node_a=7, node_b=8, youngs_modulus=1, area=1)
model.add_truss_element(id=85, node_a=9, node_b=10, youngs_modulus=1, area=1)
model.add_truss_element(id=86, node_a=11, node_b=12, youngs_modulus=1, area=1)
model.add_truss_element(id=87, node_a=13, node_b=14, youngs_modulus=1, area=1)
model.add_truss_element(id=88, node_a=15, node_b=16, youngs_modulus=1, area=1)
model.add_truss_element(id=89, node_a=17, node_b=18, youngs_modulus=1, area=1)
model.add_truss_element(id=90, node_a=19, node_b=20, youngs_modulus=1, area=1)
model.add_truss_element(id=91, node_a=21, node_b=22, youngs_modulus=1, area=1)
model.add_truss_element(id=92, node_a=23, node_b=24, youngs_modulus=1, area=1)
model.add_truss_element(id=93, node_a=25, node_b=26, youngs_modulus=1, area=1)
model.add_truss_element(id=94, node_a=27, node_b=28, youngs_modulus=1, area=1)
model.add_truss_element(id=95, node_a=29, node_b=30, youngs_modulus=1, area=1)
model.add_truss_element(id=96, node_a=31, node_b=32, youngs_modulus=1, area=1)
model.add_truss_element(id=97, node_a=33, node_b=34, youngs_modulus=1, area=1)
model.add_truss_element(id=98, node_a=35, node_b=36, youngs_modulus=1, area=1)
model.add_truss_element(id=99, node_a=37, node_b=38, youngs_modulus=1, area=1)
model.add_truss_element(id=100, node_a=39, node_b=40, youngs_modulus=1, area=1)
model.add_truss_element(id=101, node_a=41, node_b=42, youngs_modulus=1, area=1)

# --- Supports
model.add_dirichlet_condition(node_id= 1, dof_types='uvw', value=0)
model.add_dirichlet_condition(node_id= 2, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 3, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 4, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 5, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 6, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 7, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 8, dof_types='w', value=0)
model.add_dirichlet_condition(node_id= 9, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=10, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=11, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=12, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=13, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=14, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=15, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=16, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=17, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=18, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=19, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=20, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=21, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=22, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=23, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=24, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=25, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=26, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=27, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=28, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=29, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=30, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=31, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=32, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=33, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=34, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=35, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=36, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=37, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=38, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=39, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=40, dof_types='w', value=0)
model.add_dirichlet_condition(node_id=41, dof_types='uvw', value=0)
model.add_dirichlet_condition(node_id=42, dof_types='w', value=0)

# --- Loads
model.add_single_load(id='load center', node_id=22, fv=-1)

print("Model creation completed - start interaction.")

model = interact(model=model, dof=(22,'v'))

animation = show_animation(model, speed=1)