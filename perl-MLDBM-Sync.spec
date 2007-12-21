%define name	perl-MLDBM-Sync
%define real_name    MLDBM-Sync
%define version 0.30
%define release %mkrel 5

%define perl_sitelib %(eval "`perl -V:installsitelib`"; echo $installsitelib)

Summary:	%{real_name} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source0:	%{real_name}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:	perl-devel perl-Digest-MD5 perl-MLDBM
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl-base
BuildArch:	noarch

%description
%{real_name} module for perl

%prep
%setup -q -n %{real_name}-%{version}

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


