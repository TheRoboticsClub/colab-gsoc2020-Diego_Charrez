import argparse

def dqn_args_train():
    """Parse DQN training arguments.
    
    Returns:
        args: The parsed arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--seed',
        dest='seed',
        type=int,
        help='Seed for numpy and tensorflow.',
        default=1,
        required=True)

    parser.add_argument(
        '--num_iterations',
        dest='num_iterations',
        type=int,
        help=' Training will end after reaching the number of interations.',
        default=20000)

    parser.add_argument(
        '--initial_collect_steps',
        dest='initial_collect_steps',
        type=int,
        help='Exploratory steps.',
        default=1000)

    parser.add_argument(
        '--collect_steps_per_iteration',
        dest='collect_steps_per_iteration',
        type=int,
        help='Collected steps per iteration.',
        default=1)

    parser.add_argument(
        '--replay_buffer_max_length',
        dest='replay_buffer_max_length',
        type=int,
        help='Size of the replay buffer.',
        default=100000)

    parser.add_argument(
        '--batch_size',
        dest='batch_size',
        type=int,
        help='The assets directory.',
        default=64)

    parser.add_argument(
        '--lr',
        dest='learning_rate',
        type=float,
        help='The learning rate',
        default=1e-3)

    parser.add_argument(
        '--log_interval',
        dest='log_interval',
        type=int,
        help='Output logs after n steps.',
        default=200)

    parser.add_argument(
        '--num_eval_episodes',
        dest='num_eval_episodes',
        type=int,
        help='.',
        default=10)

    parser.add_argument(
        '--eval_interval',
        dest='eval_interval',
        type=int,
        help='.',
        default=1000)

    args = parser.parse_args()

    return args