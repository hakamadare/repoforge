# $Id$
# Authority: shuff
# Upstream: Tom Preston-Werner <tom$github,com>

# requires python-pygments
%{?el6:# Tag: rfx}

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?ruby_sitearchdir: %define ruby_sitearchdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/jekyll-%{version}

%global rubyabi 1.8

Summary: Blog-aware, static site generator
Name: rubygem-jekyll
Version: 0.11.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/jekyll/

Source: http://rubygems.org/downloads/jekyll-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: ruby(rubygems)
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(rdiscount) >= 1.6.5
BuildRequires: rubygem(redcarpet) >= 1.9.0
BuildRequires: rubygem(RedCloth) >= 4.2.1
Requires: python-pygments
Requires: ruby(rubygems)
Requires: ruby(abi) = %{rubyabi}
Requires: rubygem(albino) >= 1.3.2
Requires: rubygem(classifier) >= 1.3.1
Requires: rubygem(directory_watcher) >= 1.1.1
Requires: rubygem(kramdown) >= 0.13.2
Requires: rubygem(liquid) >= 1.9.0
Requires: rubygem(maruku) >= 0.5.9
Provides: rubygem(jekyll) = %{version}

%description
Jekyll is a simple, blog-aware, static site generator. It takes a template
directory (representing the raw form of a website), runs it through Textile or
Markdown and Liquid converters, and spits out a complete, static website
suitable for serving with Apache or your favorite web server.

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
find %{buildroot}%{geminstdir}/{lib,test} -type f | xargs -n 1 sed -i  -e '/^#!\/usr\/bin\/env ruby/d'
find %{buildroot}%{geminstdir}/{doc,lib,test} -type f | xargs chmod 0644

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/cucumber.yml
%doc %{geminstdir}/g.pl
%doc %{geminstdir}/Gemfile
%doc %{geminstdir}/History.txt
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README*
%doc %{geminstdir}/jekyll.gemspec
%doc %{gemdir}/doc/jekyll-%{version}
%doc %{geminstdir}/doc
%{_bindir}/*
%{gemdir}/cache/jekyll-%{version}.gem
%{gemdir}/specifications/jekyll-%{version}.gemspec
%dir %{geminstdir}
%{geminstdir}/Rakefile
%{geminstdir}/bin
%{geminstdir}/features
%{geminstdir}/lib
%{geminstdir}/output
%{geminstdir}/test

%changelog
* Fri Aug 05 2011 Steve Huff <shuff@vecna.org> - 0.11.0-1
- Initial package.
