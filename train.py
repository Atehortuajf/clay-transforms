# Main training loop for the dynamic training

# For each Gaussian Splat object, we will optimize a number (TBD) of clay-transformations at each timestep.
# Each transform has learnable center of action, action matrix weights, and drop-off matrix weights