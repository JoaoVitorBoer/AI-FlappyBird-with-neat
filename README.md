# AI-FlappyBird-with-NEAT

AI-FlappyBird-with-NEAT is an implementation of the Flappy Bird game controlled by a neural network using the NeuroEvolution of Augmenting Topologies (NEAT) algorithm. This project is designed to demonstrate how genetic algorithms can be used to train a game-playing AI to navigate through obstacles effectively.

## Features

- **NEAT Algorithm:** Utilizes the Python NEAT library for evolving neural networks.
- **Pygame Framework:** Built using Pygame for game development and rendering.
- **Dynamic Obstacle Avoidance:** Teaches AI to dynamically avoid pipes using learned strategies.
- **Generation Tracking:** Displays the current generation and score to monitor AI progress.
- **Visual and Auditory Feedback:** Includes visual representations of the game state and auditory feedback for events like jumping.

## Installation

To run this project, you need to have Python and Pygame installed along with the NEAT Python library. Follow these steps to set up the project environment:

1. Clone the repository:

```bash
git clone https://your-repository-url.git
cd AI-FlappyBird-with-neat
```

2. Install the libraries
```bash
pip install pygame neat-python
```

## Usage
To start the game and see the AI in action, simply run the Python script from the command line:

```bash
python flappy_bird.py
```
This will open a window displaying the game. The AI will start playing automatically, trying to score as high as possible by avoiding pipes.

## Configuration
The NEAT configuration can be adjusted in the config.txt file located in the project directory. This file contains parameters that affect the neural network and genetic algorithm, such as population size, mutation rates, and fitness thresholds.

## How It Works
The game uses the NEAT algorithm to evolve a set of neural networks, each controlling a bird. The networks receive input about their environment and output commands to either jump or not jump. The birds are scored based on how long they survive without hitting obstacles.
