# $Id$
# Authority: shuff
# Upstream: http://rakudo.org

%define rakudo_year 2011
%define rakudo_month 4

%define parrot_version 3.3.0

%define parrot_dynext %{_libdir}/parrot/%{parrot_version}/dynext
%define parrot_lang_perl6 %{_libdir}/parrot/%{parrot_version}/languages/perl6

Summary: Perl 6 distribution
Name: rakudo-star
Version: %{rakudo_year}.%{rakudo_month}
Release: 1%{?dist}
License: Artistic 2.0
Group: Development/Languages
URL: http://rakukdo.org/

Source: http://github.com/downloads/rakudo/star/rakudo-star-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Buildarch: noarch
BuildRequires: 
BuildRequires: rpm-macros-rpmforge
Requires:

%description

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;AudioVideo;
EOF

%build
%{__libtoolize} --force --copy
%{__aclocal} #--force
%{__autoheader}
%{__automake} --add-missing -a --foreign
%{__autoconf}
autoreconf --force --install --symlink
%configure \
    --disable-dependency-tracking \
    --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post
/sbin/ldconfig 2>/dev/null
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Son Jun 20 2006 Dag Wieers <dag@wieers.com> - 
- Initial package. (using DAR)
