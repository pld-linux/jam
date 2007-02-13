Summary:	Jam - make replacement
Summary(pl.UTF-8):	Jam - zastępca make
Name:		jam
Version:	2.5
Release:	5
Epoch:		1
License:	distributable (see README)
Group:		Development/Building
# Source0-md5:	d340f3c73d16a1206d0e8c88a66428e7
Source0:	ftp://ftp.perforce.com/pub/jam/%{name}-%{version}.tar
URL:		http://www.perforce.com/jam/jam.html
BuildRequires:	bison
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
# CFLAGS for jam bootstrap, OPTIM for build using jam
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	OPTIM="%{rpmcflags}" \
	YACC="bison -y"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin.*/jam $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELNOTES README *.html
%attr(755,root,root) %{_bindir}/*
