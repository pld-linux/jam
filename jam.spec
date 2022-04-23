Summary:	Jam - make replacement
Summary(pl.UTF-8):	Jam - zastępca make
Name:		jam
Version:	2.6.1
Release:	1
Epoch:		1
License:	distributable (see README)
Group:		Development/Building
#Source0Download: https://swarm.workshop.perforce.com/files/guest/perforce_software/jam
Source0:	https://swarm.workshop.perforce.com/downloads/guest/perforce_software/jam/%{name}-%{version}.zip
# Source0-md5:	6df59f91da8d3c8ab12de22f3b8c1258
URL:		https://www.perforce.com/documentation/jam-documentation
BuildRequires:	bison
BuildRequires:	unzip
Obsoletes:	boost-jam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jam is a make(1) replacement that makes building simple things simple
and building complicated things manageable.

%description -l pl.UTF-8
Jam to zamiennik make(1), który czyni budowanie prostych rzeczy
prostym, a budowanie skomplikowanych rzeczy wykonalnym.

%prep
%setup -q

%build
# split build into bootstrap and actual build, so that we can pass verbosity option to jam0
%{__make} jam0 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

CC="%{__cc}" \
OPTIM="%{rpmcflags}" \
YACC="bison -y" \
./jam0 -d x

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin.*/jam $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELNOTES README *.html
%attr(755,root,root) %{_bindir}/jam
