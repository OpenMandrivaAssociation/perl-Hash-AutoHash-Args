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
%{perl_vendorlib}/*





