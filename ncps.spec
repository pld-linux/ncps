Summary:	Another processes manager utility
Summary(pl):	Kolejny menad¿er procesów
Name:		ncps
Version:	0.493
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.columbia.edu/~pc171/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://www.columbia.edu/~pc171/ncps.html
BuildRequires:	ncurses-devel
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
ncps jest menad¿erem procesów pozwalaj±cym u¿ykownikowi ogl±daæ i
zarz±dzaæ procesami.

Mo¿liwo¶ci:
- mo¿na ³atwo wys³aæ dowolne polecenie do procesu; drzewka s± zwijalne
- mo¿na zabiæ lub monitorowaæ (od¶wie¿aæ) grupê wybranych procesów
- obs³uga wyra¿eñ regularnych w trybie wyszukiwania.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	REDHAT=0 \
	CC="%{__cc}" \
	OPT="-I/usr/include/ncurses %{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ncps $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ncps
