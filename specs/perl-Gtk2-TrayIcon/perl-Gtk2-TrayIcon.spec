# $Id: $

# Authority: dries
# Upstream:

%define real_name Gtk2-TrayIcon
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to the EggTrayIcon library
Name: perl-Gtk2-TrayIcon
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-TrayIcon/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Gtk2-TrayIcon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-ExtUtils-Depends, perl-ExtUtils-PkgConfig, perl-Glib, perl-Gtk2

%description
This module contains a perl interface to the EggTrayIcon library.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc TODO
%{_mandir}/man3/*
%{perl_vendorarch}/Gtk2/TrayIcon.pm
%{perl_vendorarch}/Gtk2/TrayIcon/*
%{perl_vendorarch}/auto/Gtk2/TrayIcon/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
