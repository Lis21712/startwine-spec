# Original project: https://github.com/RusNor/StartWine-Launcher
%global debug_package %{nil}

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
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  libepoxy-devel
BuildRequires:  LibRaw-devel
BuildRequires:  openssl-devel

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
ln -sf data/img img
rm -f Cargo.lock

%build
# Отключаем встроенную сборку gettext - используем системную
export GETTEXT_SYSTEM=1
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

# Указываем Rust использовать системную библиотеку
export RUSTFLAGS=$(pkg-config --libs libintl | sed 's/ / -C link-arg=/g' | sed 's/^-C link-arg=//')

# Собираем через cargo
cargo build --release

# Проверяем бинарник
ls -la target/release/
if [ ! -f target/release/sw_start ]; then
    echo "ERROR: sw_start not found!"
    find target/release -type f -executable 2>/dev/null || true
    exit 1
fi

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/startwine
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications

install -Dm755 target/release/sw_start %{buildroot}%{_bindir}/startwine

# Копируем остальные файлы
if [ -d data ]; then
    cp -r data/* %{buildroot}%{_datadir}/startwine/ 2>/dev/null || true
fi

if [ -f data/img/gui_icons/sw_icon.png ]; then
    install -Dm644 data/img/gui_icons/sw_icon.png %{buildroot}%{_datadir}/pixmaps/startwine.png
fi

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/ru.launcher.StartWine.desktop

# Делаем скрипты исполняемыми
find %{buildroot}%{_datadir}/startwine -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

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
