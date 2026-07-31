# TODO

## Setup gate

- [x] Confirm WSL2 can see the NVIDIA GPU.
- [ ] Confirm `scripts/smoke_test.py` reports a CUDA JAX device.
- [ ] Run the test suite.
- [ ] Authenticate W&B with `wandb login`.
- [x] Create and push the GitHub repository.

## Baseline gate

- [ ] Clone MuJoCo Playground and Open Duck Mini beside this repository.
- [ ] Pin the exact upstream commit SHAs used for reproduction.
- [ ] Train the unmodified Open Duck Mini walking policy from scratch.
- [ ] Record the seed, config hash, git SHA, W&B run ID, and hardware for every run.

## Payload environment

- [ ] Integrate `models/payload_slider.xml` into the Open Duck Mini torso/tray model.
- [ ] Keep the first payload model to one sliding degree of freedom.
- [ ] Randomize payload mass, initial position, friction loss, and tray height.
- [ ] Assert that policy observations exclude payload position, velocity, mass, and friction.
- [ ] Verify the payload visibly slides under commanded acceleration.

## Research phases

- [ ] Implement Blind+DR, published RMA, fast-latent method, and oracle conditions.
- [ ] Train at least three seeds per condition with equal environment steps.
- [ ] Evaluate retention, falls, adaptation time, and velocity tracking error.
- [ ] Produce the friction sweep and adaptation-versus-avoidance analysis.
- [ ] Complete the sim-only writeup before considering hardware or 2-DoF payloads.
