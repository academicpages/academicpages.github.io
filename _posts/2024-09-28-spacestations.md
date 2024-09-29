---
title:  "Larger Space Stations"
date:   2024-10-10 22:33:30
comments: true
categories:
  - Large Space Stations
  - Space Exploration
---
# Capacity Comparison: 100-Person Space Station vs. ISS
## Known aspects of the ISS (or Data)
The volume of the ISS is:
- Total Pressurized Volume, $(V_{tot})_{ISS}$: $916 \,m^3$
- Habitable Volume, $(V_{hab})_{ISS}$: $388 \,m^3$

This means about $42\%$ of the ISS's total volume is habitable. It typically hosts a:
- Standard crew, $n_{std}$ of $6$-$7$ astronauts.
- Maximum crew of,$n_{max}$ : Up to $13$ astronauts (short-term).

Not sure when this will matter in my analysis but the ISS mass is $420,000 \, kg$.


```python
ISS_Pressurized_Volume = 916 #m^3
ISS_Habitable_Volume = 388 #m^3
ISS_min_crew = 6 #astronauts
ISS_max_crew = 13 #astronauts
max_volume_per_crew_ISS = ISS_Habitable_Volume/ISS_min_crew
min_volume_per_crew_ISS = ISS_Habitable_Volume/ISS_max_crew
ideal_volume_per_crew_ISS = ISS_Pressurized_Volume/ISS_min_crew
print("max volume per crew", max_volume_per_crew_ISS)
print("min volume per crew", min_volume_per_crew_ISS)
print("ideal volume per crew", ideal_volume_per_crew_ISS)
print("habitable percentage", 100*ISS_Habitable_Volume/ISS_Pressurized_Volume)
```

    max volume per crew 64.66666666666667
    min volume per crew 29.846153846153847
    ideal volume per crew 152.66666666666666
    habitable percentage 42.35807860262009


## Known aspects of Von Braun's Rotating Wheel Space Station
Wernher von Braun's [video](https://www.youtube.com/watch?v=5JJL8CUfF-o) says that a rotating wheel space station would:
- host 50 astronauts though [Wikipedia](https://en.wikipedia.org/wiki/Rotating_wheel_space_station#History) states 80 people.
- be a torus of 250 $ft$ (76  $m$) diameter. The video shows two decks (in most cases) which I assume is 6 $m$ height in total. Again wikipedia says 3 decks, but I will stick to two 6  $m$ decks for now.

This implies that the distance from the center of the tube to the center of the torus is $R = 70/2 = 35 \, m$ and the minor radius of the tube is $r = 6/2 = 3 \, m$. The volume of this torus is then the station's total pressurized volume, which is given by:
$(V_{tot})_{vB} = 2 \pi^2 R r^2$

So, we can estimate the volume of the the von Braun space station as:
- Total Pressurized Volume: 916 $m^3$
- Habitable Volume: 388 $m^3$


```python
from math import pi
vb_wheel_dia = 70 #m
vb_wheel_height = 6 #m

vb_wheel_Pressurized_Volume = 2 * pi**2 * (vb_wheel_dia/2) * (vb_wheel_height/2)**2 #m^3
habitable_factor_ISS = ISS_Habitable_Volume/ISS_Pressurized_Volume
habitable_factor_targeted = 0.6
vb_wheel_Habitable_Volume = vb_wheel_Pressurized_Volume * habitable_factor_targeted  #m^3

vb_wheel_std_crew = 50 #astronauts
vb_wheel_max_crew = 100 #astronauts
max_volume_per_crew_vb = vb_wheel_Habitable_Volume/vb_wheel_std_crew
min_volume_per_crew_vb = vb_wheel_Habitable_Volume/vb_wheel_max_crew
ideal_volume_per_crew_vb = vb_wheel_Pressurized_Volume/vb_wheel_std_crew
print("vb_wheel_Pressurized_Volume", vb_wheel_Pressurized_Volume)
print("max volume per crew", max_volume_per_crew_vb)
print("min volume per crew", min_volume_per_crew_vb)
print("ideal volume per crew", ideal_volume_per_crew_vb)
```

    vb_wheel_Pressurized_Volume 6217.850772686295
    max volume per crew 74.61420927223554
    min volume per crew 37.30710463611777
    ideal volume per crew 124.35701545372591



```python
habitable_ratios = vb_wheel_Habitable_Volume/ISS_Habitable_Volume
Pressurized_ratios = vb_wheel_Pressurized_Volume/ISS_Pressurized_Volume
print("habitable_ratios", habitable_ratios)
print("Pressurized_ratios", Pressurized_ratios)
```

    habitable_ratios 9.6152331536386
    Pressurized_ratios 6.788046695072375


### Question: How can we double the total volume of the von Braun wheel?
To double the wheel's pressurized volume to 12435.7 $m^3$, one option is to increase the tube's height to 8.48 $m$. 


```python
from math import sqrt
vb_wheel_height_for_doubled_volume = 6 * sqrt(2) #m
vb_wheel_Pressurized_Volume_doubled = 2 * pi**2 * (vb_wheel_dia/2) * (vb_wheel_height_for_doubled_volume/2)**2 #m^3
print("doubled vb_wheel_Pressurized_Volume", vb_wheel_Pressurized_Volume_doubled, "when tube dia is", vb_wheel_height_for_doubled_volume)
```

    doubled vb_wheel_Pressurized_Volume 12435.701545372594 when tube dia is 8.485281374238571


The other option is to increase the torus's diameter altogether, which we discuss later.

### Question: Are there reasons to increase the radius of the wheel as opposed to the height of the tube?
One benefit might be that you need to rotate the tube slower to generate artificial gravity.


```python
vb_wheel_radius = vb_wheel_dia / 2
earth_g = 9.81 #m/s^2
rot_speed_vb = sqrt(1/3*earth_g/vb_wheel_radius)
print("rot speed of von Braun wheel to generate a third of Earth g is", rot_speed_vb, "rad/s or", rot_speed_vb/0.10472, "RPM")
```

    rot speed of von Braun wheel to generate a third of Earth g is 0.30566087650952556 rad/s or 2.918839538861016 RPM


Comparing my calculations to [2001: A Space Odyssey's Space Staiton V](https://youtu.be/im-JM0f_J7s?t=136)


```python
SSV_wheel_radius = 150 #m
moon_g = 1.655 #m/s^2
rot_speed_SSV_for_moon_g = sqrt(moon_g/SSV_wheel_radius)
print("2001's wheel generates Moon's gravity by rotating at", rot_speed_SSV_for_moon_g, "rad/s or", rot_speed_SSV_for_moon_g/0.10472, "RPM")
rot_speed_SSV_for_earth_g = sqrt(1/3*earth_g/SSV_wheel_radius)
print("2001's wheel generates third of Earth's gravity by rotating at", rot_speed_SSV_for_earth_g, "rad/s or", rot_speed_SSV_for_earth_g/0.10472, "RPM")
rot_speed_SSV_for_earth_g = sqrt(earth_g/SSV_wheel_radius)
print("2001's wheel generates third of Earth's gravity by rotating at", rot_speed_SSV_for_earth_g, "rad/s or", rot_speed_SSV_for_earth_g/0.10472, "RPM")
```

    2001's wheel generates Moon's gravity by rotating at 0.10503967504392488 rad/s or 1.003052664666968 RPM
    2001's wheel generates third of Earth's gravity by rotating at 0.147648230602334 rad/s or 1.4099334473102942 RPM
    2001's wheel generates third of Earth's gravity by rotating at 0.25573423705088844 rad/s or 2.442076366032166 RPM


This shows that lower spin rates (needed to prevent motion sickness and acceleration differentials between that push blood to the feet) result in accelerations closer to Earth's but are achievable only with structures larger in diameter than the von Braun wheel. But building larger structures carries the benefit of more pressurized volumes; Space Station V is a little over 4 times the volume of the von Braun wheel and 29 times the ISS.


```python
SSV_Pressurized_Volume = 2 * pi**2 * (SSV_wheel_radius) * (vb_wheel_height/2)**2 #m^3
print("SSV volume is", SSV_Pressurized_Volume/vb_wheel_Pressurized_Volume, "time the von Braun wheel's and", SSV_Pressurized_Volume/ISS_Pressurized_Volume, "times that of ISS.")
```

    SSV volume is 4.285714285714286 time the von Braun wheel's and 29.09162869316732 times that of ISS.


SSV volume is 4.285714285714286 time the von Braun wheel's and 29.09162869316732 times that of ISS.

## So how can we get to this in one launch- that's the question!
Are inflatables the answer....?


```python

```
