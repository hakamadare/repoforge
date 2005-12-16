# $Id$
# Authority: dries
# Upstream: Johan Lindstr&#246;m <johanl%5b%c3%84T%5dDarSerMan,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-View-GraphViz

Summary: GraphViz view class
Name: perl-Catalyst-View-GraphViz
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-View-GraphViz/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JOHANL/Catalyst-View-GraphViz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package contains a GraphViz view class for Catalyst.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Catalyst/View/GraphViz.pm
%{perl_vendorlib}/Catalyst/Helper/View/

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
