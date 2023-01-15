%define modname	MIME-Charset

Summary:	Charset Informations for MIME
Name:		perl-%{modname}
Version:	1.013.1
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/MIME::Charset
Source0:	http://www.cpan.org/modules/by-module/MIME/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(CPAN)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
MIME::Charset provides informations about character sets used for MIME messages
on Internet.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor < /dev/null

%build
%make_build

%check
make test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/MIME
%{_mandir}/man3/*
%{perl_vendorlib}/POD2/JA/MIME
