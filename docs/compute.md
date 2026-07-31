# Compute Plan

## Decision

IsaacLab training will run on an NVIDIA Brev GPU instance. Local development and
MuJoCo/MJX validation will remain on the existing Windows/WSL2 workstation.

This separation is intentional:

- Local MuJoCo environment: Python 3.11, JAX CUDA, MuJoCo, MJX, and Brax.
- Remote Isaac environment: Python 3.12 with a compatible Isaac Sim and IsaacLab stack.
- W&B: experiment metrics and selected artifacts from both environments.

The Isaac dependencies must not be added to the root `pyproject.toml` or installed in
the local MuJoCo virtual environment.

## Step 4: Research and document the compute target

Step 4 is complete when the provider and operating rules are decided. It does not
require starting a paid instance.

Selected target:

- Provider: NVIDIA Brev.
- Instance type: stoppable Linux GPU instance.
- GPU: at least 24 GB VRAM.
- Storage: at least 200 GB persistent storage.
- Persistent working directory: `/home/ubuntu/workspace`.
- Cost rule: stop the instance whenever active work ends.
- Durability rule: push source and small reproducibility artifacts to GitHub before
  stopping; upload selected training artifacts through W&B.
- Deletion rule: never delete an instance until all required files are copied elsewhere.

Exact GPU type, region, and hourly price will be selected when capacity is needed.

## Step 5: Provision and validate IsaacLab

Step 5 begins when work reaches the Isaac baseline. At that point:

1. Preview available stoppable Brev instances with at least 24 GB VRAM.
2. Provision the selected instance and confirm `nvidia-smi` works.
3. Clone this repository into `/home/ubuntu/workspace`.
4. Create a separate Python 3.12 environment.
5. Install a mutually compatible Isaac Sim, IsaacLab, PyTorch, CUDA, and RSL-RL stack.
6. Accept the NVIDIA EULA where required.
7. Run an empty-scene or Cartpole smoke test before installing project environments.
8. Authenticate W&B on the Brev instance.
9. Clone and validate SteadyTray before modifying its environment or robot assets.
10. Record the GPU type, provider, region, package versions, image or container digest,
    and upstream commit SHAs.

Step 5 is complete only when the Isaac smoke test and one untouched upstream example
run successfully.

## Suggested Brev preview

Run this only when preparing to provision compute:

```bash
brev create duck-isaac --min-vram 24 --min-disk 200 --stoppable --dry-run
```

Remove `--dry-run` only after reviewing the selected GPU and hourly price.

