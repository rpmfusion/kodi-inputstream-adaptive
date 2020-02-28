%global aname inputstream.adaptive
%global kodi_version 18.0
%global kodi_branch Leia

Name:           kodi-inputstream-adaptive
Version:        2.4.3

Release:        1%{?dist}
Summary:        Adaptive file addon for Kodi's InputStream interface

# wvdecryper contains parts of Chromium CDM under BSD
License:        GPLv2+ and BSD
URL:            https://github.com/peak3d/%{aname}/
Source0:        %{url}/archive/%{version}-%{kodi_branch}/%{aname}-%{version}-%{kodi_branch}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  expat-devel

Requires:       kodi >= %{kodi_version}
Provides:       bundled(bento4)
Provides:       bundled(libwebm)

ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{aname}-%{version}-%{kodi_branch}

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.c' -or -name '*.cc' -or -name '*.cpp' | xargs chmod a-x
chmod a-x README.md %{aname}/changelog.txt


%build
%cmake .
%make_build


%install
%make_install

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/kodi/addons/%{aname}/*.so


%files
%doc README.md %{aname}/changelog.txt
%license LICENSE.GPL
%{_libdir}/kodi/addons/%{aname}/
%{_datadir}/kodi/addons/%{aname}/


%changelog
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
