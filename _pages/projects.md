---
layout: archive
title: "Posters"
permalink: /projects/
author_profile: true
redirect_from:
  - /projects
---

<head>
<style>
a.rec:link {
  color: #003CA4;
  background-color: transparent;
  text-decoration: underline;
  font-weight:bold;
}
a.rec:visited {
  color: #003CA4;
  background-color: transparent;
  text-decoration: underline;
  font-weight:bold;
}
</style>
</head>

{% include base_path %}

## Hybrid artificial neural network modelling predicts behaviour and neural activity in a solution for Buridan’s ass.

{: style="text-align: justify" }
<img src="/images/foragingposter.png" alt="pretty picture" width="35%" style="padding-right: 2%; padding-top: 0.5%; float: left;">
Prefrontal cortex has been implicated in planning, decision making, sequence working memory, and many other cognitive functions requiring contemplations of the future.
However, little is known about the neural computations underlying these high-level processes.
Recent work by Xie et al. (2022), El-Gaby et al. (2023), and others have demonstrated a conjunctive representation of space and time in PFC during sequence working memory tasks, whereby separate neural subspaces encode the desired state of the world at different times into the future.
Together with Tim Behrens, we are now investigating whether similar conjunctive spacetime representations could form a neural substrate of _planning_ in frontal cortex, by developing neural networks with attractor dynamics that converge to valid plans through space and time.
These ideas were recently presented at a conference in Rome, a recording of which can be found <a class="rec" href="https://www.youtube.com/watch?v=EIu_OmNFQaA">online</a>.



# Talks 

## Meta-learning to plan with recurrent neural networks

{: style="text-align: justify" }
<img src="https://krisjensen.github.io/images/metaRL.png" alt="pretty picture" width="35%" style="padding-right: 1%; padding-top: 0.5%; float: left;">
Humans can rapidly adapt to new information and flexibly change their behavior in dynamic environments.
It has previously been suggested that this flexibility is facilitated by fast network dynamics in the prefrontal network, acquired through a process of ‘meta-reinforcement learning’.
However, a notable feature of human behaviour that these models fail to capture is the ability to perform temporally extended planning using an internal model of the environment.
Together with Marcelo Mattar and Guilllaume Hennequin, we investigate how such ‘simulation-based planning’ can help reinforcement learning agents adapt to new environments.
We also demonstrate substantial similarities bewtween this model and both human behaviour and rodent hippocampal replays recorded by John Widloski during a spatial navigation task.
<a class="rec" href="https://github.com/KrisJensen/planning_code">Code</a><br>
