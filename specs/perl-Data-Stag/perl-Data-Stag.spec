# $Id$
# Authority: dries
# Upstream: Chris Mungall <cjm$fruitfly,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Stag

Summary: Structured Tags datastructures
Name: perl-Data-Stag
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Stag/

Source: http://search.cpan.org/CPAN/authors/id/C/CM/CMUNGALL/Data-Stag-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is for manipulating data as hierarchical tag/value pairs
(Structured TAGs or Simple Tree AGgreggates). These datastructures can
be represented as nested arrays, which have the advantage of being
native to perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/stag-*.pl
%{perl_vendorlib}/Data/Stag.pm
%{perl_vendorlib}/Data/Stag/

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
