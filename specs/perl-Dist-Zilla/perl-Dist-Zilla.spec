# $Id$
# Authority: shuff
# Upstream: Ricardo SIGNES <rjbs$cpan,org>
# ExcludeDist: el3 el4
# Rationale: ExtUtils::MakeMaker version

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Dist-Zilla

Summary: distribution builder; installer not included!
Name: perl-Dist-Zilla
Version: 4.200006
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://dzil.org/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Dist-Zilla-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.5
BuildRequires: perl(App::Cmd::Setup) >= 0.309
BuildRequires: perl(App::Cmd::Tester) >= 0.306
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires: perl(CPAN::Meta::Prereqs) >= 2.101390
BuildRequires: perl(CPAN::Meta::Validator) >= 2.101550
BuildRequires: perl(CPAN::Uploader) >= 0.101550
BuildRequires: perl(Carp)
BuildRequires: perl(Config::INI::Reader)
BuildRequires: perl(Config::MVP::Assembler)
BuildRequires: perl(Config::MVP::Assembler::WithBundles)
BuildRequires: perl(Config::MVP::Reader) >= 2.101540
BuildRequires: perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires: perl(Config::MVP::Reader::Finder)
BuildRequires: perl(Config::MVP::Reader::INI) >= 2
BuildRequires: perl(Config::MVP::Section) >= 2.200001
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Data::Section) >= 0.004
BuildRequires: perl(DateTime) >= 0.44
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(ExtUtils::Manifest) >= 1.54
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::ShareDir::Install) >= 0.03
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::pushd)
BuildRequires: perl(Hash::Merge::Simple)
BuildRequires: perl(JSON) >= 2
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Log::Dispatchouli) >= 1.102220
BuildRequires: perl(Moose) >= 0.92
BuildRequires: perl(Moose::Autobox) >= 0.10
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::LazyRequire)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(MooseX::SetOnce)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(MooseX::Types::Perl)
BuildRequires: perl(PPI)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Perl::PrereqScanner) >= 0.100830
BuildRequires: perl(Perl::Version)
BuildRequires: perl(Pod::Eventual) >= 0.091480
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Software::License) >= 0.101370
BuildRequires: perl(Software::LicenseUtils)
BuildRequires: perl(String::Formatter) >= 0.100680
BuildRequires: perl(String::RewritePrefix) >= 0.005
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Exporter::Util)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Term::UI)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More) >= 0.96
BuildRequires: perl(Text::Template)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(Version::Requirements) >= 0.100630
BuildRequires: perl(YAML::Tiny)
BuildRequires: perl(autobox) >= 2.53
BuildRequires: perl(autodie)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(parent)
BuildRequires: perl(version)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.5
Requires: perl(App::Cmd::Setup) >= 0.309
Requires: perl(App::Cmd::Tester) >= 0.306
Requires: perl(Archive::Tar)
Requires: perl(CPAN::Meta::Converter) >= 2.101550
Requires: perl(CPAN::Meta::Prereqs) >= 2.101390
Requires: perl(CPAN::Meta::Validator) >= 2.101550
Requires: perl(CPAN::Uploader) >= 0.101550
Requires: perl(Carp)
Requires: perl(Config::INI::Reader)
Requires: perl(Config::MVP::Assembler)
Requires: perl(Config::MVP::Assembler::WithBundles)
Requires: perl(Config::MVP::Reader) >= 2.101540
Requires: perl(Config::MVP::Reader::Findable::ByExtension)
Requires: perl(Config::MVP::Reader::Finder)
Requires: perl(Config::MVP::Reader::INI) >= 2
Requires: perl(Config::MVP::Section) >= 2.200001
Requires: perl(Data::Dumper)
Requires: perl(Data::Section) >= 0.004
Requires: perl(DateTime) >= 0.44
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(ExtUtils::Manifest) >= 1.54
Requires: perl(File::Copy::Recursive)
Requires: perl(File::Find::Rule)
Requires: perl(File::HomeDir)
Requires: perl(File::Path)
Requires: perl(File::ShareDir)
Requires: perl(File::ShareDir::Install) >= 0.03
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(File::pushd)
Requires: perl(Hash::Merge::Simple)
Requires: perl(JSON) >= 2
Requires: perl(List::MoreUtils)
Requires: perl(List::Util)
Requires: perl(Log::Dispatchouli) >= 1.102220
Requires: perl(Moose) >= 0.92
Requires: perl(Moose::Autobox) >= 0.10
Requires: perl(Moose::Role)
Requires: perl(Moose::Util::TypeConstraints)
Requires: perl(MooseX::LazyRequire)
Requires: perl(MooseX::Role::Parameterized)
Requires: perl(MooseX::SetOnce)
Requires: perl(MooseX::Types)
Requires: perl(MooseX::Types::Moose)
Requires: perl(MooseX::Types::Path::Class)
Requires: perl(MooseX::Types::Perl)
Requires: perl(PPI)
Requires: perl(Params::Util)
Requires: perl(Path::Class)
Requires: perl(Perl::PrereqScanner) >= 0.100830
Requires: perl(Perl::Version)
Requires: perl(Pod::Eventual) >= 0.091480
Requires: perl(Scalar::Util)
Requires: perl(Software::License) >= 0.101370
Requires: perl(Software::LicenseUtils)
Requires: perl(String::Formatter) >= 0.100680
Requires: perl(String::RewritePrefix) >= 0.005
Requires: perl(Sub::Exporter)
Requires: perl(Sub::Exporter::Util)
Requires: perl(Term::ReadKey)
Requires: perl(Term::ReadLine)
Requires: perl(Term::ReadLine::Gnu)
Requires: perl(Term::UI)
Requires: perl(Test::Deep)
Requires: perl(Text::Template)
Requires: perl(Try::Tiny)
Requires: perl(Version::Requirements) >= 0.100630
Requires: perl(YAML::Tiny)
Requires: perl(autobox) >= 2.53
Requires: perl(autodie)
Requires: perl(namespace::autoclean)
Requires: perl(parent)
Requires: perl(version)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Dist::Zilla builds distributions of code to be uploaded to the CPAN. In this
respect, it is like ExtUtils::MakeMaker, Module::Build, or Module::Install.
Unlike those tools, however, it is not also a system for installing code that
has been downloaded from the CPAN. Since it's only run by authors, and is meant
to be run on a repository checkout rather than on published, released code, it
can do much more than those tools, and is free to make much more ludicrous
demands in terms of prerequisites.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes LICENSE META.json README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Dist/Zilla.pm
%{perl_vendorlib}/Dist/Zilla/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Apr 29 2011 Steve Huff <shuff@vecna.org> - 4.200006-1
- Initial package.
