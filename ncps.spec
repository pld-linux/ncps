Summary:	Another processes manager utility
Summary(pl):	Kolejny zarz�dca proces�w
Name:		ncps
Version:	0.55
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.math.ohio-state.edu/~pschan/ncps/%{name}-%{version}.tar.gz
# Source0-md5:	de18df8cdf5d238a68ae85f9901393bd
Patch0:		%{name}-FILLBUG.patch
URL:		http://www.math.ohio-state.edu/~pschan/ncps/
BuildRequires:	ncurses-devel
BuildRequires:	procps-devel
BuildRequires:	procps-static
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

%description -l pl
ncps jest programem do zarz�dzania procesami, pozwalaj�cym
u�ytkownikowi ogl�da� je i nimi zarz�dza�.

Mo�liwo�ci:
- mo�na �atwo wys�a� dowolne polecenie do procesu; drzewka s� zwijalne
- mo�na zabi� lub monitorowa� (od�wie�a�) grup� wybranych proces�w
- obs�uga wyra�e� regularnych w trybie wyszukiwania.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/ncps $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ncps
