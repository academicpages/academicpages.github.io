---
title:  "Some Space Stations in Fiction and Reality"
date:   2024-09-29 14:30:00
categories:
  - Large Space Stations
  - Space Exploration
---
{% newthought "An earlier post in my teaching resources for" %} a final
year undergraduate project had a pretty helpful
AI-generated{%sidenote 'thankclaude' 'thanks to [Claude](claude.ai)'%}
[table](https://www.angadhn.com/online_textbooks/UG_final_year_project/#large-space-stations-modular-or-monolithic).
This is a quick post about Wernher von Braun's 1950's
[conceptual rotating wheel station](https://www.youtube.com/watch?v=5JJL8CUfF-o) with some basic comparisons
to the ISS (1998-present) and 1968's Space Station V from 2001: A Space
Odyssey{%sidenote 'spaceOdyssey' 'Watch this as homework!'%}.

## Von Braun's Rotating Wheel Space Station
Wernher von Braun's [video](https://www.youtube.com/watch?v=5JJL8CUfF-o) envisioned a rotating wheel
space station with 9 sections for:
1. Headquarters and Communications
2. Earth Weather Observation/Prediction
3. Military Reconnaissance using Optical and Radar Telescopes
4. Emergency Hospital Section
5. Astronomy
6. Calculation Machines and a lower/outer deck with maintenance facilities
7. A/C equipment
8. Living quarters
9. Botanical and Zoological Laboratory
The video shows two decks per section, which I assume is 6 $m$ in heigh (i.e. the habitable portion between the
outer rim and inner rim). Wikipedia says the concept had 3 decks but as I haven't looked that up, I will stick to two
6 $m$ decks for now.

The system is powered by an atomic reactor attached on one side of its central hub; its heat will drive a
turbo generator to power the station. Radio and radar antennas sit atop the reactor. The other side of the hub has
an airlock for astronauts to access/exit the space station via smaller spacecraft. Like a bicycle wheel, the system
had thin spokes are condensers for the turbo generator and air-conditioning plant. Three larger tubes are elevator
shafts that connect the hub to the main habitable sections of the wheel station. The station would:
- host 50 astronauts though [Wikipedia](https://en.wikipedia.org/wiki/Rotating_wheel_space_station#History) states 80 people.
- rotate at roughly 3 rpm to produce artificial gravity on the rim; and
- be a torus of 250 $ft$ (76  $m$) diameter. The distance from the center of the tube to the center of the torus is $R = 70/2 = 35 \, m$ and the minor radius of the tube is $r = 6/2 = 3 \, m$. The volume of this torus is then the station's total pressurized volume, which is given by $$(V_{tot})_{vB} = 2 {\pi^2} R {r^2}$$.

So, we can estimate that the von Braun space station has a:
- Total Pressurized Volume: = 6217.85 $m^3$
- Habitable Volume = 3730.71 $m^3$ 

Here, I assumed that 60% of the pressurized volume is habitable. This is a considerably more optimistic percentage
compared to the 42% of ISS.

### How did von Braun imagine its realisation?
{% marginfigure 'mf-id-1' 'assets/imgs/AssemblyOfRim.png' 'Assembly of the Modular Rotating Wheel Space Station.'  %}
{% marginfigure 'mf-id-2' 'assets/imgs/CondenserPipesInstallation.png' 'Condenser pipes being unwound for installation.'  %}

The short-version is that he assumed predominantly modular robotic assembly and a minor reliance on inflatables
for the airlock. First, the hub is inflated using compressed air from built-in tanks. Protection from meteors
is ensured by putting thin metal plates; this is unnecessary today as we have developed high-strength textiles
that are used on inflatable space stations. A second launch brings with it an airlock, which is again attached
by robots; this allows the pressurized hub to be used as a temporary quarters as the station assembly continues
with astronaut-robot teams.
Pre-fabricated and tested on the ground after which it is dismantled and assembled robotically in-orbit.
A number successive launches (he says) ensure the "parts of the station  are assembled in the correct order".
Nylon tethers prevent parts from drifting away. The reactor appears to be the next big piece that is installed
so I assume this is the third launch. This is followed by the elevator shafts and the rim sections being brought
together. We can assume a single launch for each module: $3$ elevator tubes and 9 rim modules (assuming one per
section). Assuming condenser pipes are installed from one launch (but the structure itself needs to be unwound robotically, which seems unreasonable/unreal at the moment as a robotic task.


Lastly, the installation of instruments/equipment (a simple catch-all term for imaging antennas and
the lab facilities compute for astronomical/Earth Observation data analysis, I think) and two small
rocket motors on the rim. These rocket motors "blast for a few seconds" to revolve the station at about
$3 \, RPM$. 

## Comparing to ISS and Space Station V (2001: A Space Odyssey)
{% marginnote 'table-1-id' '*Table 1*:  Comparing the ISS to fictional ideas.' %}

|                                              | ISS    | von Braun              | Space Station V |
| -------------------------------------------- | ------ | ---------------------- | --------------- |
| crew size (# of astronauts)                  | 7-13   | 50-80                  | 2               |
| diameter of the station (m)                  | n/a    | 75                     | 300             |
| total volume $m^3$                           | 916    | 6217.85                | 26647.93        |
| habitable %                                  | 42.35% | 60% (assumed)          | ?               |
| Max. volume per crew $(\frac{m^3}{person})$  | 64.66  | 52.67 assuming 50 crew | 13223.46        |
| Rotational speed for artificial gravity (RPM)|  -     | 3                      | 2.44            |
| Gravity on-board  ($m/s^2$)                  |  -     | 1.655                  | 9.81            |

## Some gaps in von Braun design
1. Assumes a launch every 24 hours- not close to it then and not really close to that kind of cadence today. What could we do today?
2. Doesn't really say how many launches are needed to realize assembly in the video. This can probably be found elsewhere but my estimate from watching the video is 15-18 launches.
3. The process involves a number of assembly robots but we barely have one of these today. And whatever is there not autonomous.
4. Materials used in assembly are unknown.
5. Telescope sizes for reconnaisance and astronomy are unknown.
6. Power requirements are unknown.
7. What else?
