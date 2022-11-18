%define modname	MIME-Charset
%define modver 1.012.2

Summary:	Charset Informations for MIME
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/MIME::Charset
Source0:	http://www.cpan.org/modules/by-module/MIME/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(CPAN)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
MIME::Charset provides informations about character sets used for MIME messages
on Internet.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/MIME
%{_mandir}/man3/*
%{perl_vendorlib}/POD2/JA/MIME
