# Original project: https://github.com/RusNor/StartWine-Launcher
Name:           startwine
Version:        422
Release:        1%{?dist}
Summary:        Windows application launcher for Linux

License:        GPL-3.0-or-later
URL:            https://github.com/RusNor/StartWine-Launcher
Source0:        StartWine_v%{version}.tar.gz
Source1:        ru.launcher.StartWine.desktop

ExclusiveArch:  x86_64

BuildRequires:  cargo
BuildRequires:  rustup
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gdk4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3-devel

Requires:       python3
Requires:       gtk4
Requires:       fuse
Requires:       curl
Requires:       yad

%description
StartWine is a Windows application launcher for GNU/Linux operating systems.
It includes many features, extensions, and fixes to improve performance,
visuals, and usability.

%prep
%autosetup -n StartWine-Launcher-StartWine_v%{version}

%build
./build release

%install
# Rust-бинарник
install -Dm755 target/release/sw_start %{buildroot}%{_bindir}/startwine

# Python-скрипты
mkdir -p %{buildroot}%{_datadir}/startwine/scripts
cp -r data/scripts/* %{buildroot}%{_datadir}/startwine/scripts/

# Иконка
install -Dm644 data/img/gui_icons/sw_icon.png %{buildroot}%{_datadir}/pixmaps/startwine.png

# .desktop файл
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/ru.launcher.StartWine.desktop

%files
%{_bindir}/startwine
%{_datadir}/startwine/
%{_datadir}/pixmaps/startwine.png
%{_datadir}/applications/ru.launcher.StartWine.desktop
%license LICENSE
%doc README.md

%changelog
* Sun Jun 07 2026 Wik217 <pri3rak217@gmail.com> - 422-1
- Initial RPM release for Fedora
- Built from source code (x86_64 only)
