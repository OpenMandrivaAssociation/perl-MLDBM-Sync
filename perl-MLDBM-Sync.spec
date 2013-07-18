%define upstream_name    MLDBM-Sync
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} module for perl
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHAMAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(MLDBM)
BuildArch:	noarch

%description
%{upstream_name} module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc MANIFEST README
%{_mandir}/*/*
%{perl_vendorlib}/MLDBM


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.0
+ Revision: 407686
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.30-8mdv2009.0
+ Revision: 257849
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.30-7mdv2009.0
+ Revision: 245881
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.30-5mdv2008.1
+ Revision: 136288
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.30-5mdv2008.0
+ Revision: 67500
- kill file require on perl-base


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.30-5mdv2007.0
+ Revision: 108472
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-MLDBM-Sync

