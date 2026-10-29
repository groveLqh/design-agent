from pathlib import Path

import click
import pytest

from design_agent.codex_local import create


@pytest.mark.parametrize("size", ["0x10", "8193x20", "1;shx2", "../foo"])
def test_invalid_size(tmp_path: Path, size: str) -> None:
    with pytest.raises(click.ClickException, match="side|Size"):
        create(tmp_path, "card", None, size)


def test_thread_traversal(tmp_path: Path) -> None:
    with pytest.raises(click.ClickException, match="thread"):
        create(tmp_path, "card", "../escape", "100x100")


def test_rejects_api_login(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("design_agent.codex_local.shutil.which", lambda name: name)
    monkeypatch.setattr("design_agent.codex_local.run", lambda args: "Logged in using an API key")
    with pytest.raises(click.ClickException, match="ChatGPT login required"):
        create(tmp_path, "card", None, "100x100")
