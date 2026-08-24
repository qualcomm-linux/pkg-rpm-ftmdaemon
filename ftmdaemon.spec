%global debug_package %{nil}

Name:           ftmdaemon
Version:        1.0.0
Release:        2%{?dist}
Summary:        Qualcomm WLAN Factory Test Mode daemon

License:        Qualcomm-Technologies-Inc.-Proprietary
Source0:        %{name}-prebuilt-%{version}.tar.gz

ExclusiveArch:  aarch64

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so(\\..*)?$
%global __requires_exclude ^libdiag\\.so\\.1\\(\\)\\(64bit\\)$

%description
ftmdaemon is packaged from a prebuilt payload tarball for Qualcomm Linux platforms.

%prep
%autosetup -n %{name}-prebuilt-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a . %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Mon Aug 24 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-2
- Rebuild prebuilt payload from source package with private libdiag.so

* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
