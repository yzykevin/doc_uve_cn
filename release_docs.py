#!/usr/bin/env python3
import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent


def run(cmd: list[str], dry_run: bool = False) -> None:
    print(f"  $ {' '.join(cmd)}")
    if dry_run:
        return
    result = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if result.stdout.strip():
        print(f"    {result.stdout.strip()}")
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)


def get_output(cmd: list[str]) -> str:
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Tag and publish a versioned doc release.")
    parser.add_argument("version", help="Version tag to create, e.g. v2.8")
    parser.add_argument("-m", "--message", default="", help="Tag annotation message (optional)")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    args = parser.parse_args()

    version: str = args.version
    if not version.startswith("v"):
        print(f"ERROR: version should start with 'v', got: {version}", file=sys.stderr)
        sys.exit(1)

    tag_message = args.message or f"Release {version}"
    dry_run: bool = args.dry_run

    prefix = "[DRY RUN] " if dry_run else ""
    print(f"{prefix}Releasing {version} in {REPO.name}\n")

    if not dry_run:
        status = get_output(["git", "status", "--porcelain"])
        if status:
            print("WARNING: uncommitted changes detected.")
            answer = input("Stage and commit all changes before tagging? [y/N] ").strip().lower()
            if answer == "y":
                run(["git", "add", "-A"])
                run(["git", "commit", "-m", f"docs: prepare {version} release"])
            else:
                print("Aborting — please commit or stash changes first.", file=sys.stderr)
                sys.exit(1)

        existing_tags = get_output(["git", "tag"]).splitlines()
        if version in existing_tags:
            print(f"ERROR: tag {version} already exists.", file=sys.stderr)
            sys.exit(1)

    run(["git", "push", "origin", "main"], dry_run)
    run(["git", "tag", "-a", version, "-m", tag_message], dry_run)
    run(["git", "push", "origin", version], dry_run)

    print(f"\nDone. ReadTheDocs will now build version '{version}'.")
    if not dry_run:
        print("Ensure the new version is set to Active and Public in the RTD dashboard.")


if __name__ == "__main__":
    main()
