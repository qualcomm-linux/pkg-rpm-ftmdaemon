%global debug_package %{nil}

Name:           ftmdaemon
Version:        1.0.0
Release:        1%{?dist}
Summary:        Factory Test Mode daemon for Qualcomm WLAN devices

License:        Qualcomm.nologin.binaries.license
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/wlan-service.qclinux.0.0/260825/prebuilt_resolute/wlanftm_%{version}_arm64.tar.gz

ExclusiveArch:  aarch64

%description
ftmdaemon provides the device-side daemon for Qualcomm WLAN Factory Test
Mode (FTM). It handles factory test requests used to exercise WLAN
hardware and firmware during manufacturing and diagnostics.

%prep
%autosetup -c -n %{name}-%{version}

%build
# Prebuilt payload package: nothing to compile.

%install
mkdir -p %{buildroot}
cp -a data/wlanftm/arm64/. %{buildroot}/
find %{buildroot} \( -type f -o -type l \) -printf '/%%P\n' | sort > %{name}.files

%files -f %{name}.files
%license data/wlanftm/arm64/usr/share/doc/wlanftm/copyright
%license data/LICENSE.qcom-2
%license data/NOTICE

%changelog
* Fri Aug 21 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - 1.0.0-1
- Initial prebuilt RPM packaging
