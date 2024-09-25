In this repo, you can find deep reinforcement learning exercises to learn how to apply code in this field.

# Introduction to Deep Reinforcement Learning #
Reinforcement learning (RL) is a branch of the machine learning paradigm where an agent learns by interacting with its environment through trial and error, receiving feedback in the form of rewards or penalties to optimize its future actions.

Imagine you're playing a video game where you control a robot to explore a maze. The robot doesn't know where the  exit's location is, but each time it moves closer to the that, it gets a small reward. If it hits a wall or moves away from the exit, it gets a penalty. Over time, the robot learns which paths are beneficial based on the rewards and penalties it has received, eventually figuring out the optimal route to the exit. This process of learning from actions and feedback is the core idea of RL. Now let's talk about the basic concepts of RL:

 ## Agent ##
The agent is like the robot in the maze. It acts as the determining agent attempting to fulfill a defined aim. The agent decides what to do based on what it knows about its surroundings.

__Example:__ The robot is your agent, navigating the maze by making decisions at every turn.

## State ##
It is everything the agent interacts with, including all external factors affecting the agent's decisions. The environment reacts to the agent's actions and returns feedback.

__Example:__ The maze itself, with its walls, corridors, and hidden exit, depicts the environment. Every movement the robot makes affects how it navigates this space.

## Environment ##
A state is a snapshot of the environment at any given moment. It tells the agent where it is in the environment.

__Example:__ At any time, the robot knows its current position within the maze, whether near a wall, at an intersection, or close to the exit. This is its current state.

## Action ##
An action is a decision the agent makes to change its state. Each action directs the agent to a new state

__Example:__ Our maze robot might have four possible actions: move _left_, _right_, _forward_, or _backward_. It picks one of these based on its current state and what it assumes will lead to the best result.

## Reward ##
It is the feedback that the agent receives after taking an action. A positive reward makes the agent take similar actions in the future, while a negative one discourages certain actions.

__Example:__ Each time the robot gets closer to the maze's exit, it receives a reward ( or points in some concepts). If it hits a dead-end or wall, it gets a penalty (loses points).

## Policy ##
The policy could be considered the agent's strategy or _game plan_ for choosing actions based on the current state.

__Example:__ Over time, the maze robot learns a policy that helps it navigate through the maze more effectively, avoiding dead-ends & taking the fastest path to the exit.

