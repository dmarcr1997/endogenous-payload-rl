from pathlib import Path

import mujoco


def test_payload_slider_model_loads() -> None:
    model_path = Path(__file__).parents[1] / "models" / "payload_slider.xml"
    model = mujoco.MjModel.from_xml_path(str(model_path))

    assert model.nq == 1
    assert model.nv == 1
    assert model.joint("pay_slide").range.tolist() == [-0.05, 0.05]

