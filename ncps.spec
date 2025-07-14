Summary:	Another processes manager utility
Summary(pl.UTF-8):	Kolejny zarządca procesów
Name:		ncps
Version:	0.55
Release:	17
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.math.ohio-state.edu/~pschan/ncps/%{name}-%{version}.tar.gz
# Source0-md5:	de18df8cdf5d238a68ae85f9901393bd
Patch0:		%{name}-FILLBUG.patch
Patch1:		%{name}-procps.patch
Patch2:		%{name}-fixes.patch
Patch3:		%{name}-PAGE_SIZE.patch
URL:		http://www.math.ohio-state.edu/~pschan/ncps/
BuildRequires:	ncurses-devel
BuildRequires:	procps-devel >= 1:3.3.3-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncps is a processes manager which allows user to see and manage
processes.

Features:
 - you can issue arbitrary command to a process. Trees are now
   collapsible.
 - you can kill a group of selected processes, and you can monitor
   (refresh) a group of selected processes.
 - regexp support in search mode.

%description -l pl.UTF-8
ncps jest programem do zarządzania procesami, pozwalającym
użytkownikowi oglądać je i nimi zarządzać.

Możliwości:
- można łatwo wysłać dowolne polecenie do procesu; drzewka są zwijalne
- można zabić lub monitorować (odświeżać) grupę wybranych procesów
- obsługa wyrażeń regularnych w trybie wyszukiwania.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p0

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
export LIBS="-ltinfo"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CONTRIBUTORS ChangeLog
%attr(755,root,root) %{_bindir}/ncps
%{_mandir}/man1/ncps.1*
