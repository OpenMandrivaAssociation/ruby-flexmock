%define upstream_name flexmock
%define name  ruby-%{upstream_name}

%define version 0.8.6
%define release %mkrel 1

Summary: Simple mock object for unit testing
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Ruby
URL: http://flexmock.rubyforge.org/
Source0: http://rubyforge.org/frs/download.php/55056/%{upstream_name}-%{version}.tgz
BuildRequires: ruby-RubyGems ruby-rake ruby-rcov
Requires: ruby
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
FlexMock is a simple mock object for unit testing. The interface is simple,
but still provides a good bit of flexibility.

%prep
%setup -q -n %upstream_name-%version

%build

%check
rake test

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
mkdir -p %buildroot%ruby_sitelibdir
cp -a lib/flexmock* %buildroot%ruby_sitelibdir
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
%{ruby_sitelibdir}/flexmock*
%doc README test
