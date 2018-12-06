# Run tests in check section
%bcond_without check

%global goipath         github.com/satori/go.uuid
Version:                1.2.0

%global common_description %{expand:
This package provides pure Go implementation of Universally Unique Identifier 
(UUID). Supported both creation and parsing of UUIDs.

With 100% test coverage and benchmarks out of box.

Supported versions:
 - Version 1, based on timestamp and MAC address (RFC 4122)
 - Version 2, based on timestamp, MAC address and POSIX UID/GID (DCE 1.1)
 - Version 3, based on MD5 hashing (RFC 4122)
 - Version 4, based on random numbers (RFC 4122)
 - Version 5, based on SHA-1 hashing (RFC 4122)}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        UUID package for Go 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
BuildRequires: golang(gopkg.in/check.v1)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- First package for Fedora

