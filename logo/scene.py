#! /usr/bin/python

import random

header="""
#version 3.7;

global_settings {
   assumed_gamma 1
   radiosity{
     pretrace_start 0.08
     pretrace_end   0.001
     count 150
     error_bound 0.2
     nearest_count 20
     recursion_limit 2
     brightness 1
   }
}

camera {
        right x*600/340
	location 1.5*<-3.2, 2.2, -3.4>
	look_at  <3.3, 0, 0>
	angle 60
}
"""

plain_plane="""
plane {
   y, 0

   pigment {
		color rgb <1,1,1>
   }
    finish { ambient 0 diffuse 0.8 }
}
"""

plane="""
plane {
   y, 0

   #declare BlurAmount = 0.15;
   #declare BlurSamples = 20;

   texture {
     average
     texture_map
     {
       #declare Ind = 0;
       #declare S = seed(0);
       #while(Ind < BlurSamples)
         [1
           pigment { color rgb 1.25 }
           finish {
             reflection {0.2, 1.0 fresnel on}
             diffuse 0.7 ambient 0
           }
           normal {
             bumps BlurAmount
             translate <rand(S),rand(S),rand(S)>*10
             scale 1000
           }
         ]
         #declare Ind = Ind+1;
       #end
     }
   }
   interior { ior 1.5 }
}
"""

sky="""
sky_sphere {
	pigment {
		gradient x
		color_map {
			[0.4 color rgb < 0.700, 0.715, 1.000>*0.5]
			[0.85 color rgb < 1.500, 1.400, 1.250>*1.7]
			
		}
		scale 2
		translate -x
		rotate 20*y
	}
}
"""



box="""
box {
  0, <0.3,  0.3,  0.3>
    texture {
    pigment {
      color rgb <0.9, 0.9, 0.9>
	}
    finish { ambient 0 diffuse 0.6 }
  }
  rotate<0, -30, 0>
}
"""

print(header)
print(plain_plane)
print(sky)

block_size = 1.0
block_spacing = 1.35

block_label = """
#declare block_{label} = union {{
  box {{
    0.5*<-1,0,-1>, 0.5*<1,2,1>
  }}
  text {{
    ttf "cmunbsr.ttf" "{label}" 1, 0

    translate <-{shift},0.2,0>
    translate <0,0,-0.501>
    texture {{
    pigment {{
      color rgb <20,20,20>/255
	}}
    finish {{ ambient 0 diffuse 0.8 }}
   }}
  }}


    texture {{

    pigment {{
      color rgb <230,230,230>/255
	}}
    finish {{ ambient 0 diffuse 0.8 }} }}


}};
"""

print(block_label.format(label=1,shift=0.175))
print(block_label.format(label=2,shift=0.2))

sequence = '12'

for reps in range(0,15):
    new_sequence = ''
    flip_flop = 0
    for x in sequence:
        if x == '1':
            new_sequence = new_sequence + str(flip_flop+1)
        if x == '2':
            new_sequence = new_sequence + str(flip_flop+1) + str(flip_flop+1)
        flip_flop = 1 - flip_flop
    sequence = new_sequence

random.seed(0)

x = -3.0
z = 0.0
for index in range(0,len(sequence)):
    x = x + block_spacing + random.uniform( -0.03, 0.03 )
    z = z + random.uniform( -0.01, 0.01 )
    print("""
    object {{ block_{label} rotate y*{angle} translate <{x},0,{z}> }}
    """.format(x=x,z=z, label=sequence[index], angle = random.uniform(4,10)))

#print(box)


slab_thickness = 0.036
slab_width = 1.9
print("""
#declare slab = box {{
  0, <{width} {thickness},  1.0>
}};
""".format(width=slab_width, thickness=slab_thickness))

total = 80

print("""union {""")

x = - 3.0
for index in range(0,total):
 #    for i in range(0,index):
 #       x = x + slab_width/(2*(total - i - 1))
    if index > 0:
        x = x + slab_width / (2*(total - index))
        x = x + (slab_width / (2*(total - index))) * random.uniform(-0.01,0)
    z = 0
    y = index * slab_thickness
    z = z + random.uniform(-0.03,0.03)
    red = random.uniform(0.65,0.95)
    green = random.uniform(0.65,0.95)
    blue = random.uniform(0.65,0.95)
    print("""
        object {{ slab rotate y*{angle} translate <{x},{y},{z}> 
    texture {{
    pigment {{
      color rgb <{red},{green},{blue}>
	}}
    finish {{ ambient 0 diffuse 0.8 }}
  }}
}}
        """.format(x=x,y=y, z=z, red=red, green=green, blue=blue, angle = random.uniform(-1.5,1.5), color= random.uniform(0.75,0.85)))

print("""rotate 270*y """)
print("""translate <1.7,0,-2.0> """)
print("""}""")
