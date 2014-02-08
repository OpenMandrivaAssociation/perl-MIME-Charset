%define upstream_name    MIME-Charset
%define upstream_version 1.009.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Charset Informations for MIME
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
MIME::Charset provides informations about character sets used for MIME messages
on Internet.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-3mdv2012.0
+ Revision: 765481
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-2
+ Revision: 763975
- rebuilt for perl-5.14.x

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.1-1
+ Revision: 684773
- update to new version 1.009.1

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.2-1
+ Revision: 682135
- update to new version 1.008.2

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-2
+ Revision: 667228
- mass rebuild

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.1-1
+ Revision: 638919
- update to new version 1.008.1

* Tue Dec 29 2009 Pascal Terjan <pterjan@mandriva.org> 1.8.0-2mdv2011.0
+ Revision: 483279
- Refuse to install Encode::{EUCJPASCII,JIS2K,HanExtra} from cpan instead of blocking on the question

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.8.0-1mdv2010.1
+ Revision: 461325
- update to 1.008

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.7.1-2mdv2010.0
+ Revision: 392921
- bumping mkrel
- update to 1.007.1
- using %%perl_convert_version
- fixed license field

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.007.1-1mdv2010.0
+ Revision: 387010
- update to new version 1.007.1

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.007-1mdv2010.0
+ Revision: 377833
- update to new version 1.007

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.006.2-2mdv2009.0
+ Revision: 265415
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.006.2-1mdv2009.0
+ Revision: 195555
- update to new version 1.006.2

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.006.1-1mdv2009.0
+ Revision: 193860
- update to new version 1.006.1
- update to new version 1.000

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04.4-1mdv2007.0
+ Revision: 94828
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04.3-1mdv2007.1
+ Revision: 86556
- new version

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04.2-1mdv2007.1
+ Revision: 84300
- Import perl-MIME-Charset

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04.2-1mdv2007.1
-  first mdv release

