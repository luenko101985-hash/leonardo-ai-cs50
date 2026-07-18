import shutil
import subprocess
from pathlib import Path

import pytest


APP_ROOT = Path(__file__).resolve().parents[1]


def _git_root_or_skip():
    if shutil.which("git") is None:
        pytest.skip("Git executable is not available")

    result = subprocess.run(
        ["git", "-C", str(APP_ROOT), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        pytest.skip("Tests are not running inside a Git worktree")
    return Path(result.stdout.strip()).resolve()


def test_working_database_is_ignored_and_not_tracked():
    git_root = _git_root_or_skip()
    database_path = APP_ROOT / "leonardo.db"
    relative_database_path = database_path.relative_to(git_root)

    assert not database_path.exists() or database_path.is_file()

    ignored = subprocess.run(
        [
            "git",
            "-C",
            str(git_root),
            "check-ignore",
            "--no-index",
            "--quiet",
            "--",
            str(relative_database_path),
        ],
        check=False,
    )
    assert ignored.returncode == 0, "leonardo.db must be covered by .gitignore"

    tracked = subprocess.run(
        [
            "git",
            "-C",
            str(git_root),
            "ls-files",
            "--error-unmatch",
            "--",
            str(relative_database_path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert tracked.returncode != 0, "leonardo.db must not be tracked in the Git index"


def test_expected_backup_directory_is_outside_git_root():
    git_root = _git_root_or_skip()
    expected_backup_directory = git_root.parent / "leonardo-db-backups"

    assert git_root not in expected_backup_directory.resolve().parents
