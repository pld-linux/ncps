%define name ncps
%define version 0.41
%define release 1mdk

Summary: another processes manager utility
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Copyright: GPL
Group: Applications/System
BuildRoot: /tmp/%{name}-buildroot
Prefix: %{_prefix}

%description
 ncps is a processes manager which allows user to see and manage
 processes.

%prep
%setup -q 
%build
make
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{prefix}/bin
install -s -m 755 ncps $RPM_BUILD_ROOT/%{prefix}/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README
/%{prefix}/bin/ncps

%changelog
* Tue Sep  7 1999 Daouda LO <daouda@mandrakesoft.com>

-0.41
- First spec file for Mandrake distribution.


# end of file
