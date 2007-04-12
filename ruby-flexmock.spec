%define rname flexmock
%define name  ruby-%{rname}

%define version 0.1.7
%define release %mkrel 2

Summary: Simple mock object for unit testing
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Other
URL: http://onestepback.org/software/flexmock/
Source0: %{rname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: ruby-RubyGems ruby-rake
Requires: ruby

%{expand:%%define ruby_libdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{expand:%%define ruby_archdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

%description
FlexMock is a simple mock object for unit testing. The interface is simple,
but still provides a good bit of flexibility.

%prep
rm -rf %rname-%version
gem install %{SOURCE0} --install-dir `pwd`
mv gems/%rname-%version .
rmdir gems
%setup -T -D -n %rname-%version

%check
rake test

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
mkdir -p %buildroot%ruby_libdir
cp -a lib/flexmock.rb %buildroot%ruby_libdir
for f in `find test %buildroot -name \*.rb`
do
	if head -n1 "$f" | grep '^#!' >/dev/null;
	then
		sed -i 's|/usr/local/bin|/usr/bin|' "$f"
		chmod 0755 "$f"
	else
		chmod 0644 "$f"
	fi
done

%files
%defattr(-,root,root)
%{ruby_libdir}/flexmock.rb
%doc CHANGELOG README test

