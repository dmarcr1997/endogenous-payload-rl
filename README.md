# Adaptation vs. Avoidance Under Endogenous Payload Dynamics

MuJoCo/MJX research scaffold for studying endogenous, time-varying payload dynamics on the Open Duck Mini V2.

## Platform

GPU-backed JAX is not supported on native Windows. Use Ubuntu 24.04 under WSL2 for development and training.

## Setup

From Ubuntu 24.04 in WSL2:

```bash
cd /mnt/c/Users/dmarc/Documents/endogenous-payload-rl
export UV_PROJECT_ENVIRONMENT=/home/mossy/.venvs/endogenous-payload-rl
uv python install 3.11
uv sync --extra cuda12 --all-groups
```

Verify the installation:

```bash
JAX_DEFAULT_MATMUL_PRECISION=highest uv run --extra cuda12 python scripts/smoke_test.py
uv run pytest
```

The smoke test must report a CUDA device and complete one jitted MJX step. The included
configuration disables JAX's default GPU-memory preallocation because this machine has 4 GB VRAM.

## Layout

```text
configs/                         Seeded experiment configuration
models/payload_slider.xml        Minimal 1-DoF endogenous payload model
scripts/smoke_test.py            MuJoCo, MJX, and GPU verification
src/endogenous_payload_rl/       Project package
tests/                           Fast model and package tests
TODO.md                          Setup-to-project roadmap
```

## Upstream baseline

The walking baseline belongs in a separate checkout until reproduction succeeds:

```bash
git clone https://github.com/google-deepmind/mujoco_playground.git ../mujoco_playground
git clone https://github.com/apirrone/Open_Duck_Mini.git ../Open_Duck_Mini
```

Do not copy upstream source into this repository. Record pinned commit SHAs in experiment metadata instead.
