%global kodi_addon inputstream.adaptive
%global kodi_version 21
%global kodi_codename Omega

# Internal bento4 version (forked and maintained by Kodi developers, and
# required by this addon, see depends/common/bento4/bento4.txt)
%global internal_bento4_version 1.6.0-641
%global internal_bento4_tag %{internal_bento4_version}-3-Omega

Name:           kodi-inputstream-adaptive
Version:        21.5.11
Release:        1%{?dist}
Summary:        Adaptive file addon for Kodi's InputStream interface

# - wvdecrypter contains parts of Chromium CDM under
#   BSD-2-Clause-Views/BSD-3-Clause
# - src/md5.* are RSA-MD
License:        GPL-2.0-or-later AND BSD-2-Clause-Views AND BSD-3-Clause AND RSA-MD
URL:            https://github.com/xbmc/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}-%{kodi_codename}.tar.gz
Source1:        https://github.com/xbmc/Bento4/archive/%{internal_bento4_tag}/Bento4-%{internal_bento4_tag}.tar.gz
Source2:        %{name}.metainfo.xml
Patch0:         add-missing_include.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(RapidJSON)
Requires:       kodi%{?_isa} >= %{kodi_version}
Provides:       bundled(bento4) = %{internal_bento4_version}
Provides:       bundled(libwebm)
Provides:       bundled(md5-thilo)

ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename} -p1


%build
%cmake -DENABLE_INTERNAL_BENTO4=1 -DBENTO4_URL=%{SOURCE1}
%cmake_build


%install
%cmake_install

# Install AppData file
install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%check
%ctest
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%files
%doc README.md
%license LICENSE.md LICENSES/
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Fri Apr 18 2025 Michael Cronenworth <mike@cchtml.com> - 21.5.11-1
- Update to 21.5.11

* Sat Mar 29 2025 Leigh Scott <leigh123linux@gmail.com> - 21.5.9-1
- Update to 21.5.9

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Michael Cronenworth <mike@cchtml.com> - 21.5.6-1
- Update to 21.5.6

* Sat Sep 28 2024 Michael Cronenworth <mike@cchtml.com> - 21.5.4-1
- Update to 21.5.4

* Mon Aug 12 2024 Michael Cronenworth <mike@cchtml.com> - 21.5.2-1
- Update to 21.5.2

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Michael Cronenworth <mike@cchtml.com> - 21.4.5-1
- Update to 21.4.5

* Wed Apr 03 2024 Michael Cronenworth <mike@cchtml.com> - 21.4.4-1
- Update to 21.4.4

* Mon Mar 11 2024 Michael Cronenworth <mike@cchtml.com> - 21.4.3-1
- Update to 21.4.3

* Sun Mar 10 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.18-1
- Update to 20.3.18

* Sat Feb 17 2024 Leigh Scott <leigh123linux@gmail.com> - 20.3.17-1
- Update to 20.3.17

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 11 2023 Michael Cronenworth <mike@cchtml.com> - 20.3.14-1
- Update to 20.3.14

* Mon Sep 25 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.13-1
- Update to 20.3.13

* Tue Aug 01 2023 Michael Cronenworth <mike@cchtml.com> - 20.3.11-1
- Update to 20.3.11

* Sat Jul 08 2023 Michael Cronenworth <mike@cchtml.com> - 20.3.9-1
- Update to 20.3.9

* Sun Apr 09 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.6-1
- Update to 20.3.6

* Mon Mar 27 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.5-1
- Update to 20.3.5

* Sun Feb 12 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.3-1
- Update to 20.3.3

* Sun Jan 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.2-2
- Fix build with GCC 13

* Sun Jan 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.2-1
- Update to 20.3.2
- Add AppStream metadata
- Switch to SPDX license identifiers

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 19.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Jul 07 2022 Michael Cronenworth <mike@cchtml.com> - 19.0.7-1
- Update to 19.0.7

* Mon Jun 13 2022 Michael Cronenworth <mike@cchtml.com> - 19.0.5-1
- Update to 19.0.5

* Wed Mar 09 2022 Michael Cronenworth <mike@cchtml.com> - 19.0.3-1
- Update to 19.0.3

* Wed Feb 09 2022 Michael Cronenworth <mike@cchtml.com> - 19.0.2-1
- Update to 19.0.2

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 19.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Michael Cronenworth <mike@cchtml.com> - 19.0.0-1
- Update to 19.0.0

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.17-1
- Update to 2.6.17
- Add tests

* Wed Jun 09 2021 Michael Cronenworth <mike@cchtml.com> - 2.6.16-1
- Update to 2.6.16

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.6-2
- Rebuild for Kodi 19 RC1

* Mon Nov 30 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.6-1
- Update to 2.6.6

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.4-1
- Update to 2.6.4

* Wed Aug 19 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Michael Cronenworth <mike@cchtml.com> - 2.4.4-1
- Update to 2.4.4

* Thu Feb 27 2020 Michael Cronenworth <mike@cchtml.com> - 2.4.3-1
- Update to 2.4.3

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Mon Sep 02 2019 Michael Cronenworth <mike@cchtml.com> - 2.3.22-1
- Update to 2.3.22

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Håkon Botnmark Jahre <haakobja@gmail.com> - 2.3.17-1
- Update to 2.3.17

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.25-2
- Enable arm build

* Thu Aug 30 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.2.25-1
- Update to 2.2.25
- Enable aarch64 build
- Fix permissions

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.16-0.2.20180420gitaedfa50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Dominic Robinson <github@dcrdev.com> - 2.2.16-0.1.20180420gitaedfa50
- Bump to 2.2.16 'release'

* Mon Apr 30 2018 Dominic Robinson <github@dcrdev.com> - 2.0.20-0.1.20180329gitc51b9a9
- Bump to 2.0.20 'release'

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.0.6-0.2.20161215gitcd26d5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Dominic Robinson <github@dcrdev.com> - 1.0.6-0.1.20161215gitcd26d5d
- Initial RPM Release
