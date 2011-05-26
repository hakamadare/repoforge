# $Id$
# Authority: shuff
# Upstream: Jens Rehsack <rehsack$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Sys

Summary: System tables interface via DBI
Name: perl-DBD-Sys
Version: 0.102
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Sys/

Source: http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/DBD-Sys-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DBI) >= 1.612
BuildRequires: perl(Filesys::DfPortable) >= 0.85
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Module::Pluggable) >= 3.0
BuildRequires: perl(Net::Interface) >= 1.0012
BuildRequires: perl(Net::Ifconfig::Wrapper) >= 0.11
BuildRequires: perl(NetAddr::IP) >= 4.028
BuildRequires: perl(Params::Util) >= 1.00
BuildRequires: perl(Scalar::Util) >= 1.00
BuildRequires: perl(Socket6)
BuildRequires: perl(SQL::Statement) >= 1.28
BuildRequires: perl(Sys::Filesystem) >= 1.30
BuildRequires: perl(Sys::Filesystem::Mountpoint) >= 1.02
BuildRequires: perl(Sys::Utmp) >= 1.6
BuildRequires: perl(Test::More)
BuildRequires: perl(Unix::Lsof) >= 0.0.5
BuildRequires: rpm-macros-rpmforge

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
DBD::Sys is a so called database driver for DBI designed to request information
from system tables using SQL. It's based on SQL::Statement as SQL engine and
allows to be extended by DBD::Sys::Plugins.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Build.PL \
    --installdirs="vendor" \
    --PREFIX="%{buildroot}%{_prefix}"

%install
%{__rm} -rf %{buildroot}
./Build pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE META.yml README Todo
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Bundle/DBD/Sys.pm
%{perl_vendorlib}/DBD/Sys.pm
%{perl_vendorlib}/DBD/Sys/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed May 25 2011 Steve Huff <shuff@vecna.org> - 0.102-1
- Initial package.
