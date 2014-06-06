%define upstream_name    Hash-AutoHash-Args
%define upstream_version 1.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Object-oriented processing of argument lists (version 0)

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Test::Pod::Content)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Exporter)
BuildRequires: perl(Hash::AutoHash)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Hash)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch

%description
This class simplifies the handling of keyword argument lists. It replaces
the Class::AutoClass::Args manpage. See the DIFFERENCES FROM
Class::AutoClass::Args manpage for a discussion of what's new. See the
Hash::AutoHash::Args::V0 manpage for a subclass which is more compatible
with the original.

The 'new' method accepts a list, ARRAY, or HASH of keyword=>value pairs,
another Hash::AutoHash::Args object, or any object that can be coerced into
a HASH . It normalizes the keywords to ignore case and leading dashes
('-'). The following keywords are all equivalent:

  name, -name, -NAME, --NAME, Name, -Name

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 654206
- rebuild for updated spec-helper

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 510971
- update to 1.12

* Fri Jan 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.1
+ Revision: 484646
- update to 1.11

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 466974
- import perl-Hash-AutoHash-Args


* Tue Nov 17 2009 cpan2dist 1.10-1mdv
- initial mdv release, generated with cpan2dist

