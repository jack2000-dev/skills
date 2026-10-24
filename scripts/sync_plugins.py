#!/usr/bin/env python3
"""Copy canonical skill instructions and runtime resources into plugin packages."""

import argparse
import json
from pathlib import Path
import shutil
import sys


def runtime_files(directory):
    files = {}
    for path in directory.rglob("*"):
        relative = path.relative_to(directory)
        if relative.parts[0] == "evals" or any(
            part in {"__pycache__", ".DS_Store"} for part in relative.parts
        ) or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError(f"Use regular files in plugin skills: {path}")
        if path.is_file():
            mode = 0o755 if path.stat().st_mode & 0o111 else 0o644
            files[relative] = (path.read_bytes(), mode)
    return files


def sync_plugins(root, check):
    marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    sources = {}
    for skill in (root / "skills").glob("*/*/SKILL.md"):
        name = skill.parent.name
        if name in sources:
            raise ValueError(f"Duplicate skill folder name: {name}")
        sources[name] = skill.parent
    entries = marketplace["plugins"]
    names = [entry["name"] for entry in entries]
    if len(names) != len(set(names)) or set(names) != set(sources):
        raise ValueError("Register each canonical skill exactly once in the marketplace")

    packages = []
    for entry in entries:
        name = entry["name"]
        package = root / "plugins" / name
        if (
            name != Path(name).name
            or not package.resolve().is_relative_to(root.resolve())
            or (root / entry["source"]["path"]).resolve() != package.resolve()
        ):
            raise ValueError(f"Plugin source must be ./plugins/{name}")
        manifest = json.loads((package / ".codex-plugin/plugin.json").read_text())
        if manifest["name"] != name or manifest["skills"] != "./skills/":
            raise ValueError(f"Match plugin name and skills path in {package}")
        target = package / "skills" / name
        if package.is_symlink() or target.parent.is_symlink() or target.is_symlink():
            raise ValueError(f"Plugin output must use regular directories: {target}")
        packages.append((name, target, runtime_files(sources[name])))

    changed = False
    for name, target, expected in packages:
        if runtime_files(target) == expected:
            print(f"{name}: in sync")
            continue
        changed = True
        if check:
            print(f"{name}: out of sync; run python3 scripts/sync_plugins.py", file=sys.stderr)
            continue
        if target.exists():
            shutil.rmtree(target)
        for relative, (content, mode) in expected.items():
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            destination.chmod(mode)
        print(f"{name}: synced")
    return 1 if check and changed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale packages without writing")
    args = parser.parse_args()
    try:
        return sync_plugins(Path(__file__).resolve().parents[1], args.check)
    except (OSError, ValueError, KeyError) as error:
        print(f"Plugin sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
