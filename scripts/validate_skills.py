"""Convenience entry point for the AION Skill System validator."""
from pathlib import Path
import sys

package_dir = Path(__file__).resolve().parents[1] / "packages" / "skill-system"
sys.path.insert(0, str(package_dir))

from validator import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
