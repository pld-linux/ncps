Summary:	another processes manager utility
Name:		ncps
Version:	0.493
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.columbia.edu/~pc171/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://www.columbia.edu/~pc171/ncps.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncps is a processes manager which allows user to see and manage
processes.

Festures:
 - you can issue arbitrary command to a process. Trees are now
   collapsible.
 - you can kill a group of selected processes, and you can monitor
   (refresh) a group of selected processes.
 - regexp support in search mode.

%prep
%setup -q
%patch0 -p1

%build
%{__make} REDHAT=0 OPT="-I/usr/include/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

install ncps $RPM_BUILD_ROOT/%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ncps
