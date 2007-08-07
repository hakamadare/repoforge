# $Id$
# Authority: dag
# Upstream: Michael G Schwern <mschwern$cpan,org>

### From RH9 onwards perl(Test::Simple) is provided by the perl package (sigh)
# ExclusiveDist: el2 rh7

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Simple

Summary: Simplified testing framework
Name: perl-Test-Simple
Version: 0.70
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Simple/

Source: http://www.cpan.org/modules/by-module/Test/Test-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a simplified Perl testing framework for creating tests to be
run either standalone or under Test::Harness.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Builder.pm
%{perl_vendorlib}/Test/Builder/
%{perl_vendorlib}/Test/More.pm
%{perl_vendorlib}/Test/Simple.pm
%{perl_vendorlib}/Test/Tutorial.pod

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.62-1
- Initial package. (using DAR)
