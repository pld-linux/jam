Summary:	Jam - make replacement
Summary(pl):	Jam - zastêpca make
Name:		jam
Version:	2.5
Release:	1
Epoch:		1
License:	distributable (see README)
Group:		Development/Building
# Source0-md5:	d340f3c73d16a1206d0e8c88a66428e7
Source0:	ftp://ftp.perforce.com/pub/jam/%{name}-%{version}.tar
Patch0:		%{name}-Makefile.patch
URL:		ftp://ftp.perforce.com/pub/jam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jam is a make(1) replacement that makes building simple things simple
and building complicated things manageable.

%description -l pl
Jam to zamiennik make(1), który czyni budowanie prostych rzeczy
prostym, a budowanie skomplikowanych rzeczy wykonalnym.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install jam0 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELNOTES README
%attr(755,root,root) %{_bindir}/*
