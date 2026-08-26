%global debug_package %{nil}

Name:           ftmdaemon
Version:        1.0.0
Release:        3%{?dist}
Summary:        Qualcomm WLAN Factory Test Mode daemon

License:        Qualcomm-Technologies-Inc.-Proprietary
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260825/prebuilt_resolute/wlanftm_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
ftmdaemon is packaged from a Qualcomm Linux release tarball.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/wlanftm/arm64/. %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files

%changelog
* Wed Aug 26 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-3
- Switch to official Qualcomm Linux wlanftm release tarball

* Mon Aug 24 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-2
- Rebuild prebuilt payload from source package with private libdiag.so

* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
