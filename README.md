## orbit-sim
A 2D N-body gravity simulator built from scratch using Python with pygame 

## What it does

Simulates a galaxy with 3 planets and a sun with realistic gravity and orbital patterns, each planet has a unique color and able to tell apart by trail color and planet color. 

## How it Works

Using Newtonian gravity we have every body attracting one another, with the inverse square law. I also used a velocity verlet integration so we could ahve energy-stable orbits(compred to the before Euler energy-drift orbit). You can zoom in and out using arrow keys(up and down). 

## Installation 

```pip install pygame```
```python main.py```

## Personal Reflection
This is a beginner project to help me combine the worlds of astrophysics and coding, recently this year I learned about Laws of Gravitations and basic physics so I thought it would be cool incorporating my previous coding experience with that. Throughout the project I saw first hand how the Kepler laws emerged and I had to shift everything into a dict format because it was getting too messy with 3 bodies. Everything was done by hand(no AI) so I could learn as much as I could. 
