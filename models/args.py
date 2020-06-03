import argparse

def dqn_args_train():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=0, type=int)  # Seeds for numpy and tensorflow
    parser.add_argument("--num_iterations", default=20000, type=int) # Training will end after n number of interations
    parser.add_argument("--initial_collect_steps", default=1000, type=int) # Exploratory steps
    parser.add_argument("--collect_steps_per_iteration", default=1, type=int) # 
    parser.add_argument("--replay_buffer_max_length", default=100000, type=int) # Size of the replay buffer
    parser.add_argument("--batch_size", default=64, type=int) #
    parser.add_argument("--learning_rate", default=1e-3, type=int) # alpha
    parser.add_argument("--log_interval", default=200, type=int) # Output logs after n steps
    parser.add_argument("--num_eval_episodes", default=10, type=int) #
    parser.add_argument("--eval_interval", default=1000, type=int) # 
    return parser.parse_args()

    