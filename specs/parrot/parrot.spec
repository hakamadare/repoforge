# $Id$
# Authority: shuff
# Upstream: 

Summary: the Parrot virtual machine
Name: parrot
Version: 3.3.0
Release: 1%{?dist}
License: Artistic 2.0
Group: Development/Languages
URL: http://www.parrot.org/

Source: http://ftp.parrot.org/releases/supported/%{version}/parrot-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Buildarch: noarch
BuildRequires: binutils
BuildRequires: bison
BuildRequires: ctags
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: gmp-devel
BuildRequires: libicu-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: perl >= 5.8.4
BuildRequires: perl(Devel::Cover)
BuildRequires: perl(JSON)
BuildRequires: perl(Storable) >= 2.12
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::Simple)
BuildRequires: procps
BuildRequires: readline-devel
BuildRequires: rpm-macros-rpmforge

%description
Parrot is a virtual machine designed to efficiently compile and execute
bytecode for dynamic languages.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: perl(File::Which) >= 0.05
Requires: perl(Perl::Critic)
Requires: perl(Pod::Simple)
Provides: perl(Parrot::Pmc2c) = %{version}
Provides: perl(Parrot::Pmc2c::MethodEmitter) = %{version}
Provides: perl(Parrot::Pmc2c::PCCMETHOD_BITS) = %{version}
Provides: perl(Parrot::Pmc2c::PMCEmitter) = %{version}


%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n vim-%{name}
Summary: Vim support for %{name}.
Group: Applications/Editors
Requires: %{name} = %{version}-%{release}
Requires: vim-common

%description -n vim-%{name}
Syntax and filetype detection files to make working with Parrot and Vim easier.

%prep
%setup

# set up the Perl provides
cat << \PROV > %{name}-prov
#!/bin/sh
%{__perl_provides} $* | %{__sed} -e '/perl(A)/d' -e '/perl(B)/d' \
                            -e '/perl(DB)/d' -e '/perl(Parrot::OpLib::core)/d'
PROV

%global __perl_provides %{_builddir}/%{name}-%{version}/%{name}-prov
chmod +x %{__perl_provides}

%build

%ifarch %{ix86} x86_64
    RPM_OPT_FLAGS="$RPM_OPT_FLAGS -maccumulate-outgoing-args"
%else
# The PowerPC-architecture do not build with the '-maccumulate-outgoing-args'
# option.
    RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%endif

%{__perl} Configure.pl \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --sysconfdir=%{_sysconfdir} \
    --infodir=%{_datadir}/info \
    --mandir=%{_mandir} \
    --cc=%{__cc} \
    --optimize="$RPM_OPT_FLAGS" \
    --parrot_is_shared \
    --disable-rpath \
    --lex=%{_bindir}/flex

export LD_LIBRARY_PATH=$(pwd)/blib/lib

%{__make} %{?_smp_mflags}
%{__make} html

%install
%{__rm} -rf %{buildroot}

export LD_LIBRARY_PATH=$(pwd)/blib/lib
%{__make} install DESTDIR="%{buildroot}"

# Generate several files for syntax-highlighting and automatic indenting.
# First they are installed in BUILD-directory with make and after that
# they needed to be copied to the RPM_BUILD_ROOT.
(  cd editor; 
   make vim-install VIM_DIR=.%{_datadir}/vim/vimfiles \
                    SKELETON=%{_datadir}/vim/vimfiles;
   cp -r ./usr $RPM_BUILD_ROOT                                )

# Creating man-pages
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/man1
for var in 'parrot docs/running.pod' 'parrot_debugger src/parrot_debugger.c' \
           'pbc_disassemble src/pbc_disassemble.c' 'pbc_dump src/pbc_dump.c' \
           'pbc_merge src/pbc_merge.c' 'pbc_to_exe tools/dev/pbc_to_exe.pir' \
           'parrot_config tools/build/parrot_config_c.pl' \
           'parrot-nqp ext/nqp-rx/README'    # evtl. docs/book/pct/ch05_nqp.pod
do
    MAN_NAME=`echo $var | %{__perl} -na -e 'print $F[0]'`
    MAN_SOURCE=`echo $var | %{__perl} -na -e 'print $F[1]'`
    pod2man --section=1 --name=$MAN_NAME $MAN_SOURCE | %{__gzip} -c > $RPM_BUILD_ROOT%{_mandir}/man1/${MAN_NAME}.1.gz
done

# Drop the docs so rpm can pick them up itself.
rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}

# Force permissions on doc directories.
find docs examples -type d -exec chmod 755 {} \;
find docs examples -type f -exec chmod 644 {} \;

%define RPM_PAR_LIB_DIR $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}/

# Force permissions on shared versioned libs so they get stripped.
# The parrot-install-script don't set the permissions right
# With changed permissions the dependencies will be found
find %{RPM_PAR_LIB_DIR}dynext -type f -name '*.so' -exec chmod 755 {} \;

# Remove files that are already provided with the module: perl(File::Which)
rm -rf %{RPM_PAR_LIB_DIR}tools/lib/File

# Change the perl5 'use lib' command to find Parrot::Config in the
# subdirectory 'tools/lib' of the RPM location
%{__sed} -i -e '67 s&use lib "$Bin/../../lib"\; # build location&use lib '"'"'%{_libdir}/%{name}/%{version}/tools/lib'"'"'\; # RPM location&' ${RPM_PAR_LIB_DIR}tools/dev/mk_language_shell.pl


# Added to reduce output errors when using rpmlint

# Force permission on perl-scripts in the "tools" subdirctory
find %{RPM_PAR_LIB_DIR}tools -type f -name "*.pl" -exec chmod 755 {} \; \
    -exec %{__sed} -i -e '1 s&#! perl&#!/usr/bin/perl&' {} \;
# Set path to parrot binary and Force permission
find %{RPM_PAR_LIB_DIR}tools/dev -type f -name "pbc_to_exe.pir" \
    -exec %{__sed} -i -e '1 s&#! parrot&#!/usr/bin/parrot&' {} \; \
    -exec chmod 755 {} \;

# Remove doc-files with zero-length
find docs/html -type f -size 0 -exec rm -f {} \;
find docs -wholename 'docs/doc-prep' -type f -size 0 -exec rm -f {} \;

# Set path for installed programs in docs package
find examples -type f \( -name "*.pir" -o \
                         -wholename 'examples/shootout/random.pasm' \)  \
    -exec %{__sed} -i -e '1 s&#!.*\(parrot\)&#!/usr/bin/\1&' {} \;

find examples -type f \( -name '*.pl' -o \
                         -wholename 'examples/pir/befunge/t/basic.t' -o  \
                         -path 'examples/languages/*/harness'               \) \
    -exec %{__sed} -i -e '1 s&#! perl&#!/usr/bin/perl&' {} \;
find examples -type f -name "*.py" \
    -exec %{__sed} -i -e '1 s&#! python&#!/usr/bin/python&' {} \;
find examples -type f -name "*.rb" \
    -exec %{__sed} -i -e '1 s&#! ruby&#!/usr/bin/ruby&' {} \;

find examples -wholename 'examples/languages/abc/t/01-tests.t' \
    -exec %{__sed} -i -e '1 s&#!perl&#!/usr/bin/perl&' {} \;

find examples -wholename 'examples/languages/abc/t/harness' \
    -exec %{__perl} -pi -e 's/\r$//' {} \;

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS DONORS.pod LICENSE NEWS PBC_COMPAT PLATFORMS 
%doc README RESPONSIBLE_PARTIES TODO VERSION
%doc %{_mandir}/man1/parrot.1.gz
%{_bindir}/parrot
%{_libdir}/*.so.*
%{_libdir}/parrot/
%exclude %{_libdir}/parrot/%{version}/tools/*
%exclude %{_libdir}/parrot/%{version}/VERSION

%files devel
%defattr(-, root, root, 0755)
%doc LICENSE docs/ examples/
%doc %{_mandir}/man1/parrot_config.1.gz
%doc %{_mandir}/man1/parrot_debugger.1.gz
%doc %{_mandir}/man1/pbc_disassemble.1.gz
%doc %{_mandir}/man1/pbc_merge.1.gz
%doc %{_mandir}/man1/pbc_to_exe.1.gz
%doc %{_mandir}/man1/pbc_dump.1.gz
%doc %{_mandir}/man1/parrot-nqp.1.gz
%{_bindir}/parrot_config
%{_bindir}/parrot_debugger
%{_bindir}/parrot_nci_thunk_gen
%{_bindir}/parrot-nqp
%{_bindir}/parrot-prove
%{_bindir}/pbc_disassemble
%{_bindir}/pbc_merge
%{_bindir}/pbc_to_exe
%{_bindir}/pbc_dump
%{_bindir}/ops2c
%{_includedir}/parrot/
%{_libdir}/*.so
%{_libdir}/parrot/%{version}/tools/*
%{_libdir}/parrot/%{version}/VERSION
%{_usr}/src/parrot/
%exclude %{_libdir}/*.a

%files -n vim-%{name}
%{_datadir}/vim/vimfiles/skeleton.pir
%{_datadir}/vim/vimfiles/plugin/parrot.vim
%{_datadir}/vim/vimfiles/syntax/*
%{_datadir}/vim/vimfiles/indent/pir.vim

%changelog
* Fri May 27 2011 Steve Huff <shuff@vecna.org> - 3.3.0-1
- Initial package.
