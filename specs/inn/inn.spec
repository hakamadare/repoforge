# $Id$
# Authority: shuff
# Upstream: Russ Allbery <inn-workers$lists,isc,org>

%define newsdir %{_sharedstatedir}/news

Summary: InterNetNews
Name: inn
Version: 2.5.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.eyrie.org/~eagle/software/inn/

Source: ftp://ftp.isc.org/isc/inn/inn-%{version}.tar.gz
Patch0: inn-2.5.2_py_libdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: cyrus-sasl-devel
BuildRequires: db4-devel >= 4.4
BuildRequires: gcc
BuildRequires: krb5-devel
BuildRequires: make
BuildRequires: gnupg2
BuildRequires: openssl-devel
BuildRequires: perl >= 5.8.0
BuildRequires: perl(MIME::Parser)
BuildRequires: python
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge
Requires: inn-utils = %{version}-%{release}
Requires: vixie-cron
Requires(pre): shadow-utils

%description
INN (InterNetNews), originally written by Rich Salz, is an extremely flexible
and configurable Usenet / Netnews news server. For a complete description of
the protocols behind Usenet and Netnews, see RFC 3977 (NNTP), RFC 4642
(TLS/NNTP), RFC 4643 (NNTP authentication), RFC 4644 (streaming NNTP feeds),
RFC 5536 (USEFOR), RFC 5537 (USEPRO) and RFC 6048 (NNTP LIST additions) or
their replacements.

In brief, Netnews is a set of protocols for exchanging messages between a
decentralized network of news servers. News articles are organized into
newsgroups, which are themselves organized into hierarchies. Each individual
news server stores locally all articles it has received for a given newsgroup,
making access to stored articles extremely fast. Netnews does not require any
central server; instead, each news server passes along articles it receives to
all of the news servers it peers with, those servers pass the articles along to
their peers, and so on, resulting in "flood fill" propagation of news articles. 

%package utils
Summary: Utilities and tools for use with %{name}.
Group: Applications/System

%description utils
This package contains utilities and tools for use with %{name}.  Some packages
may require components of %{inn}, but don't need the full %{inn} package.

%prep
%setup
%patch0 -p1

%build
%configure \
    --disable-dependency-tracking \
    --enable-ipv6 \
    --enable-largefiles \
    --with-berkeleydb \
    --with-kerberos \
    --with-openssl \
    --with-perl \
    --with-python \
    --with-sasl \
    --with-zlib \
    --with-news-master="root" \
    --with-tmp-dir="%{newsdir}/tmp"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} cert DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%pre
/usr/bin/getent group news >/dev/null || /usr/sbin/groupadd -r news
/usr/bin/getent passwd news >/dev/null || \
    /usr/sbin/useradd -r -g news -d "%{newsdir}" -s /sbin/nologin \
    -c "InterNetNews User" news
exit 0

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files utils
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Tue Sep 20 2011 Steve Huff <shuff@vecna.org> - 2.5.2-1
- Initial package.
