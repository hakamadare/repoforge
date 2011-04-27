# $Id$
# Authority: shuff
# Upstream: keroyonn <keroyon$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Async

Summary: Non-blocking interface to web service APIs
Name: perl-WebService-Async
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Async/

Source: http://search.cpan.org/CPAN/authors/id/K/KE/KEROYON/WebService-Async-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.8
BuildRequires: perl(AnyEvent)
BuildRequires: perl(AnyEvent::HTTP)
BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(Clone)
BuildRequires: perl(Data::UUID)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Hash::MultiKey)
BuildRequires: perl(JSON)
BuildRequires: perl(Log::Dispatch::Config)
BuildRequires: perl(Log::Dispatch::Configurator::YAML)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::WithCache)
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Smart::Args)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.8
Requires: perl(AnyEvent)
Requires: perl(AnyEvent::HTTP)
Requires: perl(Carp)
Requires: perl(Class::MOP)
Requires: perl(Clone)
Requires: perl(Data::UUID)
Requires: perl(Encode)
Requires: perl(Hash::MultiKey)
Requires: perl(JSON)
Requires: perl(Log::Dispatch::Config)
Requires: perl(Log::Dispatch::Configurator::YAML)
Requires: perl(Moose)
Requires: perl(Moose::Role)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(MooseX::WithCache)
Requires: perl(Regexp::Common)
Requires: perl(Scalar::Util)
Requires: perl(Smart::Args)
Requires: perl(URI::Escape)
Requires: perl(XML::Simple)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
WebService::Async is a non-blocking interface to web service APIs.  This is
similar to WebService::Simple but this is a non-blocking one.

* Easy to use asynchronous request.
* Caching with memcached.
* Retrying automatically on error.
* Logging with Log::Dispatch::Config (starting connection, storing cache, cache hit, etc...)
* Flexibly customizable.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

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
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WebService/Async.pm
%{perl_vendorlib}/WebService/Async/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Apr 21 2011 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
