%global aname inputstream.adaptive
%global commit cd26d5d7896e402be180e252b155c932b163b181
%global commit_date 20161215
%global kodi_version 17.0
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           kodi-inputstream-adaptive
Version:        1.0.6

Release:        0.1.%{commit_date}git%{short_commit}%{?dist}
Summary:        Adaptive file addon for Kodi's InputStream interface

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/peak3d/inputstream.adaptive/
Source0:        https://github.com/peak3d/%{aname}/archive/%{short_commit}/%{aname}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel
BuildRequires:  expat-devel

Requires:       kodi >= %{kodi_version}
Provides:       bundled(bento4)

ExclusiveArch:  i686 x86_64

%description
%{summary}.

%prep
%setup -q -n %{aname}-%{commit}

# Fix spurious-executable-perm on debug package
find . -name '*.h' -or -name '*.cpp' | xargs chmod a-x

%build
%cmake .
%make_build

%install
%make_install

# Fix permissions at installation
find $RPM_BUILD_ROOT%{_datadir}/kodi/addons/ -type f -exec chmod 0644 {} \;

%files
%doc %{_datadir}/kodi/addons/%{aname}/changelog.txt
%{_libdir}/kodi/addons/%{aname}/
%{_datadir}/kodi/addons/%{aname}/

%changelog
* Tue Sep 12 2017 Dominic Robinson <github@dcrdev.com> - 1.0.6-0.1.20161215gitcd26d5d
- Initial RPM Release
