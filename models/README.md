# Tensorflow agents - DQN

## Getting started

### 1. Create a virtual environment (Optional)

Create a virtual environment in the directory `.dqn_agent`, the directory name can be changed.

```bash
virtualenv --system-site-packages -p python3 .dqn_agent
```

Activate the virtual environment from the directory `.dqn_agent`.

```bash
source .dqn_agent/bin/activate
```

To exit the virtual environment.

```bash
deactivate
```

### 2. Install python requirements

Python dependencies can be installed with the following command.

```bash
pip install -r requirements.txt
```

## Usage

### Hyperparameters

Information about hyperparameters can be shown by running.

```bash
python dqn.py --help
```

### Training

To train the DQN model

```bash
python dqn.py --seed 123
```

### Evaluation

TO-DO