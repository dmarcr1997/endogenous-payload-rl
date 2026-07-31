# TODO

## Setup gate

- [x] Confirm WSL2 can see the NVIDIA GPU.
- [x] Confirm `scripts/smoke_test.py` reports a CUDA JAX device.
- [x] Run the test suite.
- [ ] Authenticate W&B with `wandb login`.
- [x] Create and push the GitHub repository.

## Compute gate

### Step 4: research and document

- [x] Select NVIDIA Brev as the IsaacLab compute provider.
- [x] Document the target GPU, storage, persistence, cost, and shutdown policy.
- [x] Keep the local MuJoCo Python 3.11 and remote Isaac Python 3.12 environments separate.

### Step 5: provision and validate

- [ ] Preview Brev capacity and choose the exact 24 GB+ GPU and hourly price.
- [ ] Provision a stoppable Brev instance with persistent storage.
- [ ] Create the separate Python 3.12 Isaac environment.
- [ ] Install compatible Isaac Sim, IsaacLab, PyTorch, CUDA, and RSL-RL versions.
- [ ] Pass an Isaac smoke test before adding project code.
- [ ] Authenticate W&B on the Brev instance.
- [ ] Clone SteadyTray and run one untouched upstream example.

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
