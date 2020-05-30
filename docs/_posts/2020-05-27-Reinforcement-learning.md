---
title: "Reinforcement Learning"
excerpt: ""

sidebar:
  nav: "docs"

toc: true
toc_label: "TOC installation"
toc_icon: "cog"


categories:
- GSoC
tags:
- Jderobot

author: Diego Charrez
pinned: false
---

# Objectives

* Brief introduction to Reinforcement Learning

# Introduction

As one of the main task in the project is to benchmark Deep Reinforcement Learning, with other approaches that are present in the Behavior Studio. In this post I will give a brief explanation about Reinforcement Learning .

## Concepts

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/mdp.png" | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Figure the book, Reinforcement Learning: An Introduction by Andrew Barto and Richard S. Sutton</figcaption>
</figure>
  
  Markov Decision Process framework models mathematically the Reinforcement Learning problem which comprehends the interaction between agent and environment [\[4\]](https://spinningup.openai.com/en/latest/) [\[9\]](http://incompleteideas.net/book/the-book-2nd.html).

### Environment 

The environment in this project is the whole track, here the agent will act using a camera.

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/environment.png" | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Figure from JdeRobot Assets</figcaption>
</figure>
  

### Agent

The agent would be the Formula 1 car, which will drive autonomously in the track following the red line.

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/agent.png" | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Figure from JdeRobot Assets</figcaption>
</figure>
  

### Actions

In the project actions are going to be considered deterministic, for example an action would be a medium throttle and 30 degrees to the left, if the action space is too large it could take longer to find the right policies (the best action for each state).

### State

Given that we are going to use a camera as perception, the states would be the images from the camera which could appended in succession to give a sense of recurrence. 

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/state_2.png" | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Figure from JdeRobot Robotics Academy Follow Line</figcaption>
</figure>

### Reward

The reward signal $r$ is given by the environment after the agent has taken an action $a$ in a particular state $s$.

### Episode

An episode starts from an initial state $s_{0}$ until a terminal state which in our case would be when the Formula 1 car leaves the lane.


## Goals

The main goal of the reinforcement learning algorithms is to get the maximum discounted reward over an episode, also known as expected return denoted by $G_{t}$, the discount factor $\gamma, 0 \leq \gamma \leq 1$ controls the value of immediate rewards and long term rewards [\[4\]](https://spinningup.openai.com/en/latest/) [\[9\]](http://incompleteideas.net/book/the-book-2nd.html).

$$G_{t}=\sum_{t=0}^{\infty} \gamma^{t} r_{t}$$



## References


[1] Medium, [Simple Reinforcement Learning: Q-learning](https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56)

[2] [Q-learning in Python](https://www.geeksforgeeks.org/q-learning-in-python/)

[3] [Deep Q-learning](https://www.analyticsvidhya.com/blog/2019/04/introduction-deep-q-learning-python/)

[4] OpenAI Spinning Up, [Intro to RL OpenAI](https://spinningup.openai.com/en/latest/)

[5] [Intro to RL algorithms](https://towardsdatascience.com/introduction-to-various-reinforcement-learning-algorithms-i-q-learning-sarsa-dqn-ddpg-72a5e0cb6287)

[6] Deepmind, [Human-level control through deep reinforcement
learning](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)

[7] Deepmind, [Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)

[8] B Ravi Kiran, et al. [Deep RL for Autonomous Driving survey](https://arxiv.org/abs/2002.00444)

[9] Andrew Barto and Richard S. Sutton, [Reinforcement Learning: An introduction](http://incompleteideas.net/book/the-book-2nd.html), MIT Press, 2018.