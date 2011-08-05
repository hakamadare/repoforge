# $Id$
# Authority: shuff
# Upstream: Vicent Marti <vicent$github,com>

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?ruby_sitearchdir: %define ruby_sitearchdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/redcarpet-%{version}

%global rubyabi 1.8

Summary: A fast and safe Markdown to (X)HTML parser
Name: rubygem-redcarpet

Version: 1.17.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/redcarpet/

Source: http://rubygems.org/downloads/redcarpet-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Provides: rubygem(redcarpet) = %{version}

%description
Redcarpet is a Ruby wrapper for Upskirt. It is mostly based on Ryan Tomayko's
RDiscount wrapper, and inspired by Rick Astley wearing a kilt.

%prep
%setup -q -c -T

%build
%{__mkdir_p} .%{gemdir}
gem install -V \
	--local \
	--install-dir $(pwd)/%{gemdir} \
	--force --rdoc \
	%{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{gemdir}
%{__cp} -a .%{gemdir}/* %{buildroot}%{gemdir}/


%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mv} %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
find %{buildroot}/%{_bindir} -type f | xargs -n 1 sed -i  -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
%{__rm}dir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/{ext,lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/README.markdown
%doc %{geminstdir}/redcarpet.gemspec
%doc %{gemdir}/doc/redcarpet-%{version}
%{_bindir}/*
%{gemdir}/cache/redcarpet-%{version}.gem
%{gemdir}/specifications/redcarpet-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/ext
%{geminstdir}/lib
%{geminstdir}/test

%changelog
* Fri Aug 05 2011 Steve Huff <shuff@vecna.org> - 1.17.2-1
- Initial package.
