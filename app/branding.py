"""Read a small, explicit brand brief without turning content into executable CSS."""

import json
from pathlib import Path
import re

BRAND_FILE = Path(__file__).with_name("brand.json")


def load_portfolio():
    """Read selected public coursework and résumé content, excluding private records."""
    return json.loads(Path(__file__).with_name("portfolio.json").read_text("utf-8"))


def load_brand():
    """Read saved brand choices on each request so previews reflect text edits."""
    brand = json.loads(BRAND_FILE.read_text(encoding="utf-8"))
    for key in ("ink", "paper", "accent", "surface"):
        if not re.fullmatch(r"#[0-9a-fA-F]{6}", brand["palette"][key]):
            raise ValueError(f"Use a six-digit hex color for palette.{key}")
    return brand


def stylesheet():
    """Serve validated style tokens under the same origin and CSP."""
    palette = load_brand()["palette"]
    return (
        ":root{"
        + ";".join(
            f"--{key}:{palette[key]}" for key in ("ink", "paper", "accent", "surface")
        )
        + "}"
    )
