# $Id$
# Authority: shuff
# Upstream: 

%define real_name InspIRCd

Summary: Modular IRC server
Name: inspircd
Version: 2.0.5
Release: 1%{?dist}
License: GPL
Group: Applications/Daemons
URL: http://inspircd.github.com/

Source: https://github.com/downloads/inspircd/inspircd/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: geoip-devel
BuildRequires: gnutls-devel
BuildRequires: make
BuildRequires: mysql-devel
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: postgresql-devel
BuildRequires: sqlite-devel
BuildRequires: tre-devel
BuildRequires: rpm-macros-rpmforge

Requires: perl(LWP::Simple)

%description
InspIRCd is a modular Internet Relay Chat (IRC) server written in C++ for
Linux, BSD, Windows and Mac OS X systems which was created from scratch to be
stable, modern and lightweight.

As InspIRCd is one of the few IRC servers written from scratch, it avoids a
number of design flaws and performance issues that plague other more
established projects, such as UnrealIRCd, while providing the same level of
feature parity.

%prep
%setup -n %{name}

%build
%configure \
    --disable-dependency-tracking \
    --config-dir="%{_sysconfdir}/inspircd" \
    --module-dir="%{_datadir}/inspircd/modules" \
    --enable-epoll \
    --enable-gnutls \
    --enable-modules="m_geoip,m_ldapauth,m_ldapoper,m_mysql,m_pgsql,m_regex_pcre,m_regex_posix,m_regex_tre,m_sqlite3,m_ssl_gnutls,m_ssl_openssl"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -m755 -d %{buildroot}%{_initrddir}
%{__install} -m755 inspircd %{buildroot}%{_initrddir}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc docs/COPYING docs/README docs/*.example docs/aliases docs/rfc extras/
%{_bindir}/*
%{_datadir}/inspircd/*
%{_initrddir}/inspircd
%config(noreplace) %{_sysconfdir}/inspircd/*
%exclude %{_usr}/inspircd
%exclude %{_usr}/.gdbargs

%changelog
* Tue May 29 2012 Steve Huff <shuff@vecna.org> - 2.0.5-1
- Initial package.
