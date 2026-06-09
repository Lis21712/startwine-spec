# startwine-spec

RPM SPEC file for [StartWine-Launcher](https://github.com/RusNor/StartWine-Launcher) — a Windows application launcher for Linux.

## ⚠️ Important Note

**This package is NOT compliant with Fedora Packaging Guidelines.**  
It packages a pre-built binary script rather than building from source code. The upstream project includes Rust components that require compilation.

Therefore, this package is intended only for my personal Copr repository and will not be submitted to official Fedora repositories.

## Usage

### Install from Copr

```bash
sudo dnf copr enable wik217/startwine
sudo dnf install startwine
Or build manually
bash
rpmbuild -bs startwine.spec
Version History
Version	Release Date	Notes
422	2026-06-08	Initial package
Links
Copr Repository

Bugzilla

Upstream

License
GPL-3.0-or-later
EOF

text

### 2. Убедитесь, что SPEC на месте

```bash
ls -la startwine.spec
