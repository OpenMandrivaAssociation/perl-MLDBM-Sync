%define upstream_name    MLDBM-Sync
%define upstream_version 0.30

%define perl_sitelib %(eval "`perl -V:installsitelib`"; echo $installsitelib)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{upstream_name} module for perl
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upsteam_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl-Digest-MD5 perl-MLDBM
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc MANIFEST README
%{_mandir}/*/*
%{perl_vendorlib}/MLDBM
