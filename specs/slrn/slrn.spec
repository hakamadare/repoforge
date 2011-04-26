# $Id$
# Authority: shuff
# Upstream: John E. Davis <davis$mit,edu>

Summary: A threaded Internet news reader
Name: slrn
Version: 0.9.9p1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://slrn.sourceforge.net/

Source0: http://download.sourceforge.net/slrn/slrn-%{version}.tar.gz
Source1: slrnpull-expire
Source2: slrnpull.log
Source4: README.rpm-slrnpull
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: canlock-devel 
BuildRequires: inews
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: slang-devel
BuildRequires: /usr/sbin/sendmail
Requires: canlock
Requires: slang >= 2.0.0

%description
SLRN is a threaded Internet news reader. SLRN is highly customizable
and allows users to design complex filters for sorting or killing news
articles. SLRN works well over slow network lines. A helper utility
for reading news offline is provided in the slrn-pull package.

%package pull
Summary: Offline news reading support for the SLRN news reader.
Group: Applications/Internet
Requires: slrn = %{version}

%description pull
The slrn-pull package provides the slrnpull utility, which allows you
to set up a small news spool for offline news reading using the SLRN
news reader. You also need to have the slrn package installed to use
the slrnpull utility.

%prep
%setup -q

%build
if pkg-config openssl ; then
	CPPFLAGS=`pkg-config --cflags openssl`; export CPPFLAGS
	LDFLAGS=`pkg-config --libs-only-L openssl`; export LDFLAGS
fi
export CFLAGS="$RPM_OPT_FLAGS"
slrn_cv_domain=no %configure \
    --with-ssl \
    --with-slrnpull \
    --with-ssl-includes=%{_includedir} \
    --with-ssl-library=%{_libdir} \
    --enable-setgid-code \
    --with-canlocklib=%{_libdir} \
    --with-canlockinc=%{_includedir} \
    --with-slrnpull=/var/spool/slrnpull \
    --with-slanglib=%{_libdir} \
    --with-slanginc=%{_includedir}/slang
%{__make}

%install
rm -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot}
%{__mkdir_p} %{buildroot}/etc
%{__install} -m644 doc/slrn.rc %{buildroot}/etc/slrn.rc
%{__mkdir_p} %{buildroot}/usr/share/slrn/contrib
%{__install} -m644 contrib/README* %{buildroot}/usr/share/slrn/contrib
%{__install} -m755 contrib/cleanscore contrib/slrnrc-conv %{buildroot}/usr/share/slrn/contrib

# slrnpull stuff
%{__mkdir_p} %{buildroot}/etc/{cron.daily,logrotate.d}
%{__install} -d %{buildroot}/var/spool/slrnpull/out.going
%{__install} doc/slrnpull/slrnpull.conf %{buildroot}/var/spool/slrnpull
%{__install} $RPM_SOURCE_DIR/slrnpull-expire %{buildroot}/etc/cron.daily
%{__install} $RPM_SOURCE_DIR/slrnpull.log %{buildroot}/etc/logrotate.d/slrnpull
cp $RPM_SOURCE_DIR/README.rpm-slrnpull doc/slrnpull/README.rpm

# makes %doc simpler
%{__mv} doc/slrnpull slrnpull-docs

%find_lang %{name}

# remove unpackaged files from the buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/slrn

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING COPYRIGHT changes.txt README
%doc doc/*
%doc %{_mandir}/man?/slrn.1*
%attr(755,root,root) %{_bindir}/slrn
%{_datadir}/slrn
%config(noreplace) %{_sysconfdir}/slrn.rc

%files pull
%defattr(-,root,root)
%doc slrnpull-docs/*
%doc %{_mandir}/man?/slrnpull.1*
%attr(755,root,root) %{_sysconfdir}/cron.daily/slrnpull-expire
%attr(644,root,root) %{_sysconfdir}/logrotate.d/slrnpull
%attr(2750,root,news) %{_bindir}/slrnpull
%attr(775,news,news) %dir %{_localstatedir}/spool/slrnpull
%attr(3777,news,news) %dir %{_localstatedir}/spool/slrnpull/out.going
%attr(644,news,news) %config(noreplace) %{_localstatedir}/spool/slrnpull/slrnpull.conf

%changelog
* Tue Apr 26 2011 Steve Huff <shuff@vecna.org> - 0.9.9-1
- Ported to Repoforge.

* Mon Aug 18 2008 Ralph Angenendt <ralph@centos.org> - 0.9.9-1
- bump to version 0.9.9
- explicitly require canlock
- require slang > 2 (utf-8)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8.1pl1-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8.1pl1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.9.8.1pl1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 26 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1pl1-1
- update to the latest slrn-0.9.8.1pl1 with slang2 support

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 0.9.8.1-7
- rebuilt against new openssl (again)

* Wed Nov  9 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-6
- rebuild to fix broken dependencies to libssl and libcrypto

* Wed Jul 27 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-5
- apply official bugfix patches (#164363)
  - fixes slrnpull problem with group containing no headers
  - fixes last character removal editor problem

* Mon Mar  7 2005 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-4
- fix type confusions reported by gcc4
- add RPM_OPT_FLAGS to CFLAGS
- rebuilt with gcc4

* Mon Dec 27 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-3
- package contrib subdir because of slrn-conv script (#73451)
- slrnpull.conf is now %config(noreplace), original config
  won't be overwritten (#56001)
- include slrnpull man page

* Fri Nov 26 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-2
- include translations to srln package (#140870)
- remove upstreamed patches

* Mon Oct 11 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.1-1
- update to 0.9.8.1

* Wed Oct 06 2004 Jindrich Novy <jnovy@redhat.com> 0.9.8.0-1
- update to 0.9.8.0
- execute runuser instead of su in slrnpull-expire #134597

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 0.9.7.4-8
- rebuild

* Fri Jan 03 2003 Florian La Roche <Florian.LaRoche@redhat.de> 0.9.7.4-7
- make /etc/slrn.rc mode 0644

* Fri Dec 13 2002 Nalin Dahyabhai <nalin@redhat.com>
- use openssl pkg-config data, if available

* Wed Dec 11 2002 Nalin Dahyabhai <nalin@redhat.com> 0.9.7.4-6
- configure with --with-ssl-includes=%%{_includedir} and
  --with-ssl-library=%%{_libdir}, for multilib systems

* Wed Dec 11 2002 Tim Powers <timp@redhat.com>
- remove unpackaged files from the buildroot

* Tue Jul  9 2002 Bill Nottingham <notting@redhat.com> 0.9.7.4-5
- fix it to build and work with utf-8 slang

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 14 2002 Bill Nottingham <notting@redhat.com> 0.9.7.4-3
- rebuild against new slang

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.4

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec  4 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.3, reorganize specfile some
- note that slrn.rc moves from /usr/lib/slrn to /etc

* Wed Aug 29 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.2

* Mon Jul 23 2001 Bill Nottingham <notting@redhat.com>
- add openssl buildprereq (#49699)

* Sat Jul 21 2001 Tim Powers <timp@redhat.com>
- remove the applnk file. It's cluttering our menus

* Wed Jul 18 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.1

* Mon Apr 16 2001 Bill Nottingham <notting@redhat.com>
- update to 0.9.7.0a, tweak URLs

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Nov 28 2000 Bill Nottingham <notting@redhat.com>
- update to 0.9.6.4
- enable SSL
- plug some possible buffer overflows (#12750)
- install sample macros in /usr/lib/slrn

* Thu Aug 16 2000 Bill Nottingham <notting@redhat.com>
- tweak summary/description

* Fri Aug  4 2000 Bill Nottingham <notting@redhat.com>
- add translation to desktop entry

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Bill Nottingham <notting@redhat.com>
- make slrnpull root.news, not news.news (#12428)

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- fix startup (#11658)
- fix manpage (#11973)

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix descriptions
- man pages are compressed

* Thu Jan  6 2000 Bill Nottingham <notting@redhat.com>
- fix typo in slrn.rc file

* Thu Dec 30 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.6.2

* Mon Dec 20 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.6.0

* Wed Jul 21 1999 Bill Nottingham <notting@redhat.com>
- fix perms on slrnpull logrotate

* Fri Jul 16 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.7

* Mon May 17 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.6

* Thu May  6 1999 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.5

* Fri Apr 23 1999 Bill Nottingham <notting@redhat.com>
- make slrnpull setgid news

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- make slrnpull/log missingok

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Feb 24 1999 Bill Nottingham <notting@redhat.com>
- return of wmconfig

* Mon Nov  9 1998 Bill Nottingham <notting@redhat.com>
- add bugfix patch from jed

* Fri Nov  6 1998 Bill Nottingham <notting@redhat.com>
- update to 0.9.5.4

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- built for Raw Hide
- added bugfix patch

* Tue Sep 8 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.3-2]
- Fixed a couple of stupid things I did.
- Took out -fno-strength-reduce. AFAIK, gcc on RH5.1 doesn't have this bug. I
  use egcs which shouldn't have this bug. And if you have this bug, *and* are
  recompiling on your own machin, you should have -fno-strength-reduce in your
  RPM_OPT_FLAGS anyway.

* Tue Sep 8 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.3-1]
- Updated to 0.9.5.3

* Mon Jun 1 1998 Manoj Kasichainula <manojk+rpm@io.com>
- added translations from RH 5.1 (still none for slrn-pull package)

* Mon May 4 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.2-1]
- updated to 0.9.5.2

* Wed Apr 22 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.5.1-1]
- updated to 0.9.5.1

* Mon Apr 12 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.4.6-3]
- updated to require slang 1.2.1

* Sun Apr 12 1998 Manoj Kasichainula <manojk+rpm@io.com>
[0.9.4.6-2]
- updated to require slang 1.2.0

* Wed Feb 11 1998 Manoj Kasichainula <manojk+rpm@io.com>
(my unreleased 0.9.4.6-1)
- updated to 0.9.4.6

* Tue Feb 3 1998 Manoj Kasichainula <manojk+rpm@io.com>
- docs are now forced to 644 to prevent including /bin/sh as a requirement
- added macros in the doc directory
- should now be buildable by non-root

* Thu Jan 29 1998 Bill Nottingham <wen1@cec.wustl.edu>
- updated to 0.9.4.5
- added wmconfig entry

* Sat Sep 13 1997 Manoj Kasichainula <manojk+rpm@io.com> (0.9.4.3-2)
- Fixes from JED
- default mode for slrnpull posts set to 0640, so slrnpull can read it as
  non-root
- lots of pre-setup for slrnpull
  - directories set up
  - automatic daily expiration
  - moved slrnpull directory to /var/spool/slrnpull, to match (most) docs
  - more 
- minor spec file changes

* Sat Jul 12 1997 Manoj Kasichainula <manojk+rpm@io.com> (0.9.4.3-1)
- Initial release for 0.9.4.3
