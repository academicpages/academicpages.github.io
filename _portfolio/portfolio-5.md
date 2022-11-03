---
title: "Multi-agent simulation made with mesa"
excerpt: "<br/>This project is a multi-agent simulation of the prey and predator game <br/> <img src='/images/portfolio/mesa_prey_predator.png' width='70%' height='70%'>"
collection: portfolio
---
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open in Visual Studio Code](https://img.shields.io/badge/Editor-VSCode-blue?style=flat-square&logo=visual-studio-code&logoColor=white)](https://github.dev/ArianeDlns/MAS-practice/tree/master)
[![GitHub commit](https://badgen.net/github/last-commit/ArianeDlns/MAS-practice/master)](https://GitHub.com/ArianeDlns/MAS-practice/commits/master)


**Watch out!** WIP
{: .notice}

This project is a multi-agent simulation of the prey and predator game
The implementation is based on the [mesa](https://mesa.readthedocs.io/en/stable/) example that we can find in this [repository](https://github.com/projectmesa/mesa/tree/main/examples/wolf_sheep). Equilibrium is based on the equations of the [Lotka-Volterra model](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations).

#### Summary 
A simple ecological model, consisting of three agent types: wolves, sheep, and grass. The wolves and the sheep wander around the grid at random. Wolves and sheep both expend energy moving around, and replenish it by eating. Sheep eat grass, and wolves eat sheep if they end up on the same grid cell.

If wolves and sheep have enough energy, they reproduce, creating a new wolf or sheep (in this simplified model, only one parent is needed for reproduction). The grass on each cell regrows at a constant rate. If any wolves and sheep run out of energy, they die.

To evaluate the knowledge acquired in this course on Multi-Agent Based Simulations, we suggest you model the Wolf Sheep Predation model which is a variation of the prey predator model. The description of the ABM is as follows:

- Wolves and sheep wander randomly around the landscape, while the wolves look for sheep to prey on.
- Each step costs energy. Wolves must eat sheep in order to replenish their energy. Sheep must eat grass in order to maintain their energy. When sheep and wolves run out of energy they die.
- To allow the population to continue, each wolf or sheep has a fixed probability of reproducing at each time step.
- Grass is also explicitly modeled. Once grass is eaten it will only regrow after a fixed amount of time.

<p align=center>
<img src='/images/portfolio/mesa_prey_predator.png' width='70%' height='70%'>
</p>

#### References
[1] Ferber, J. (1995), Les Systèmes Multi-Agents, InterEditions. (French version)    
[2] Ferber, J. (1999), Multi-agent systems: An introduction to distributed artificial intelligence, Addison Wesley. (English version)  
[3] Michael Wooldridge (2002), An Introduction to MultiAgent Systems, John Wiley & Sons Ltd.  
[4] The AgentLink roadmap 
[5] Robert E. Shannon (1977), Simulation modeling and methodology, SIGSIM Simulation Digital.  
[6] Robert E. Shannon (1998), Introduction to the art and science of simulation, IEEE Computer Society Press.  
[7] Bernard P. Zeigler (2000), Theory of Modeling and Simulation, Academic Press, Inc.  
[8] Rahwan, Iyad (2009), Argumentation in Artificial Intelligence,Springer.  
[9] Lopes, Fernando & Coelho, Helder. (2014). Negotiation and Argumentation in Multi-Agent Systems: Fundamentals, Theories, Systems and Applications. Bentham Science Publishers.  
[10] Argumentation in Multi-Agent Systems (ArgMAS) Workshop Series