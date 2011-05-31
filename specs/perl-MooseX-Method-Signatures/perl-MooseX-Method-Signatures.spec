# $Id$
# Authority: shuff
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Method-Signatures

Summary: Method declarations with type constraints and no source filter
Name: perl-MooseX-Method-Signatures
Version: 0.36
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Method-Signatures/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/MooseX-Method-Signatures-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(B::Hooks::EndOfScope) >= 0.07
BuildRequires: perl(Carp)
BuildRequires: perl(Context::Preserve)
BuildRequires: perl(Devel::Declare) >= 0.005011
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose) >= 0.89
BuildRequires: perl(Moose::Meta::Class)
BuildRequires: perl(Moose::Meta::Method)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::LazyRequire) >= 0.06
BuildRequires: perl(MooseX::Meta::TypeConstraint::ForceCoercion)
BuildRequires: perl(MooseX::Types) >= 0.19
BuildRequires: perl(MooseX::Types::Moose) >= 0.19
BuildRequires: perl(MooseX::Types::Structured) >= 0.20
BuildRequires: perl(MooseX::Types::Util)
BuildRequires: perl(Parse::Method::Signatures) >= 1.003011
BuildRequires: perl(Parse::Method::Signatures::TypeConstraint)
BuildRequires: perl(Parse::Method::Signatures::Types)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Moose)
BuildRequires: perl(Test::More) >= 0.89
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Text::Balanced)
BuildRequires: perl(aliased)
BuildRequires: perl(attributes)
BuildRequires: perl(metaclass)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(B::Hooks::EndOfScope) >= 0.07
Requires: perl(Carp)
Requires: perl(Context::Preserve)
Requires: perl(Devel::Declare) >= 0.005011
Requires: perl(Moose) >= 0.89
Requires: perl(Moose::Meta::Class)
Requires: perl(Moose::Meta::Method)
Requires: perl(Moose::Util)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(MooseX::LazyRequire) >= 0.06
Requires: perl(MooseX::Meta::TypeConstraint::ForceCoercion)
Requires: perl(MooseX::Types) >= 0.19
Requires: perl(MooseX::Types::Moose) >= 0.19
Requires: perl(MooseX::Types::Structured) >= 0.20
Requires: perl(MooseX::Types::Util)
Requires: perl(Parse::Method::Signatures) >= 1.003011
Requires: perl(Parse::Method::Signatures::TypeConstraint)
Requires: perl(Parse::Method::Signatures::Types)
Requires: perl(Scalar::Util)
Requires: perl(Sub::Name)
Requires: perl(Task::Weaken)
Requires: perl(Text::Balanced)
Requires: perl(aliased)
Requires: perl(namespace::autoclean)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Provides a proper method keyword, like "sub" but specifically for making
methods and validating their arguments against Moose type constraints.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/MooseX/Method/Signatures.pm
%{perl_vendorlib}/MooseX/Method/Signatures/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue May 31 2011 Steve Huff <shuff@vecna.org> - 0.36-1
- Initial package.
