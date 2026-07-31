import os
from pathlib import Path

os.environ.setdefault("JAX_DEFAULT_MATMUL_PRECISION", "highest")
os.environ.setdefault("XLA_PYTHON_CLIENT_PREALLOCATE", "false")

import jax
import mujoco
from mujoco import mjx


def main() -> None:
    model_path = Path(__file__).parents[1] / "models" / "payload_slider.xml"
    model = mujoco.MjModel.from_xml_path(str(model_path))
    data = mujoco.MjData(model)
    mujoco.mj_step(model, data)

    mjx_model = mjx.put_model(model)
    mjx_data = mjx.put_data(model, data)
    step = jax.jit(mjx.step)
    stepped_data = step(mjx_model, mjx_data)
    jax.block_until_ready(stepped_data.qpos)

    devices = jax.devices()
    if not any(device.platform == "gpu" for device in devices):
        raise RuntimeError(f"Expected a CUDA device, found: {devices}")

    print(f"MuJoCo: {mujoco.__version__}")
    print(f"JAX devices: {devices}")
    print("MJX jitted step: OK")


if __name__ == "__main__":
    main()
