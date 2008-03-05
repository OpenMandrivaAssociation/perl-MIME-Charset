%define module  MIME-Charset
%define name    perl-%{module}
%define version 1.000
%define up_version  0.044
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Charset Informations for MIME
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/MIME/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
MIME::Charset provides informations about character sets used for MIME messages
on Internet.

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc COPYING README
%{perl_vendorlib}/MIME
%{_mandir}/*/*


