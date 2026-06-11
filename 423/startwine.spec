# Original project: https://github.com/RusNor/StartWine-Launcher
Name:           startwine
Version:        423
Release:        1%{?dist}
Summary:        Windows application launcher for Linux

License:        GPL-3.0-or-later
URL:            https://github.com/RusNor/StartWine-Launcher
Source0:        StartWine_v%{version}
Source1:        ru.launcher.StartWine.desktop
Source2:        StartWine.png
Source3:        LICENSE
Source4:        README.md

Requires:       yad fuse curl

%description
StartWine is a Windows application launcher for GNU/Linux operating systems.
It includes many features, extensions, and fixes to improve performance,
visuals, and usability.

%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/startwine
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/ru.launcher.StartWine.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/startwine.png
install -Dm644 %{SOURCE3} %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dm644 %{SOURCE4} %{buildroot}/usr/share/doc/%{name}/README.md

%files
%{_bindir}/startwine
%{_datadir}/applications/ru.launcher.StartWine.desktop
%{_datadir}/pixmaps/startwine.png
%license %{_licensedir}/%{name}/LICENSE
%doc /usr/share/doc/%{name}/README.md

%changelog
* Sat Jun 06 2026 Wik217 <pri3rak217@gmail.com> - 422-1
- Initial RPM release for Fedora
- Packaged from upstream release StartWine_v422 by RusNor

