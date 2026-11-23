import shutil
from pathlib import Path

SOURCE_FILE = Path(__file__).parent / "app.py"
DEPLOY_DIR = Path(__file__).parent / "deploy"


def deploy():
    DEPLOY_DIR.mkdir(exist_ok=True)
    target = DEPLOY_DIR / SOURCE_FILE.name
    shutil.copy2(SOURCE_FILE, target)
    print(f"Deployed {SOURCE_FILE.name} to {target}")


if __name__ == "__main__":
    deploy()
