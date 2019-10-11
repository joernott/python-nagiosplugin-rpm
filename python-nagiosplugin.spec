%global srcname distribute

Name:           python-nagiosplugin
Version:        1.2.4
Release:        1%{?dist}
Summary:        Python class library for writing Nagios (Icinga) plugins

License:        ZPLv2.1
URL:            https://projects.gocept.com/projects/nagiosplugin
Source0:        https://pypi.python.org/packages/source/n/nagiosplugin/nagiosplugin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools
BuildRequires:  python3-devel python3-setuptools

%description
nagiosplugin is a Python class library which helps writing Nagios
(or Icinga) compatible plugins easily in Python. It cares for much of
the boilerplate code and default logic commonly found in Nagios
checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independent measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent "cookies" to retain state information between check runs
- Resume log file processing at the point where the last run left
- No dependencies beyond the Python standard library (except for Python 2.6).

%package -n python3-nagiosplugin
Summary:        Python class library for writing Nagios (Icinga) plugins
%description -n python3-nagiosplugin
nagiosplugin is a Python class library which helps writing Nagios
(or Icinga) compatible plugins easily in Python. It cares for much of
the boilerplate code and default logic commonly found in Nagios
checks, including:

- Nagios 3 Plugin API compliant parameters and output formatting
- Full Nagios range syntax support
- Automatic threshold checking
- Multiple independent measures
- Custom status line to communicate the main point quickly
- Long output and performance data
- Timeout handling
- Persistent "cookies" to retain state information between check runs
- Resume log file processing at the point where the last run left
- No dependencies beyond the Python standard library (except for Python 2.6).

%prep
%setup -q -n nagiosplugin-%{version}

rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' -exec sed -i 's|^#!python|#!%{__python3}|' {} +

find -name '*.py' -exec sed -i 's|^#!python|#!%{__python2}}|' {} +

%build
%{__python2} setup.py build

pushd %{py3dir}
%{__python3} setup.py build
popd


%install
rm -rf %{buildroot}

pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
# install the examples to doc rather than the the lib dir
mkdir -p %{buildroot}%{_defaultdocdir}/python3-nagiosplugin
mv %{buildroot}%{python3_sitelib}/nagiosplugin/examples %{buildroot}%{_defaultdocdir}/python3-nagiosplugin/
popd

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_defaultdocdir}/python-nagiosplugin
mv %{buildroot}%{python2_sitelib}/nagiosplugin/examples %{buildroot}%{_defaultdocdir}/python-nagiosplugin/


%files
%doc HISTORY.txt LICENSE.txt README.txt
%{python2_sitelib}/*
/usr/share/doc/python-nagiosplugin/examples/*

%files -n python3-nagiosplugin
%doc HISTORY.txt LICENSE.txt README.txt
%{python3_sitelib}/*
/usr/share/doc/python3-nagiosplugin/examples/*

%changelog
* Fri Oct 11 2019 Joern Ott <joern.ott@ott-consult.de> - 1.2.4-1
- Update to 1.2.4
- Implement requested changes from https://bugzilla.redhat.com/show_bug.cgi?id=1057454
- Removed conditionals around python3 build

* Thu Jan 23 2014 Jordan Metzmeier <jmetzmeier01@gmail.com> - 1.2-1
- Initial release
