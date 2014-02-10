%define modname	MIME-Charset
%define modver 1.011.1

Summary:	Charset Informations for MIME
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/MIME/MIME-Charset-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
MIME::Charset provides informations about character sets used for MIME messages
on Internet.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
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



