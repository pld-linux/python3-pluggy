#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pluggy
Summary:	Plugin and hook calling mechanisms for Python
Summary(pl.UTF-8):	Mechanizmy wtyczek dla Pythona
Name:		python-%{module}
Version:	0.3.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/1b/a9/6f5f80b75a8d84d21a8a13486fe26a2da9f043f93b464b2e3928be256dc4/pluggy-%{version}.tar.gz
# Source0-md5:	ecdd791e309f60668b66fec97c2ee7db
URL:		https://pypi.python.org/pypi/pluggy
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-pytest
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin manager as used by pytest but stripped of pytest specific
details.

%description -l pl.UTF-8
Zarządca wtyczek tak jak używany przez pytest, ale pozbawiony detali
specyficznych dla pytest.

%package -n python3-%{module}
Summary:	Plugin and hook calling mechanisms for Python
Summary(pl.UTF-8):	Mechanizmy wtyczek dla Pythona
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Plugin manager as used by pytest but stripped of pytest specific
details.

%description -n python3-%{module} -l pl.UTF-8
Zarządca wtyczek tak jak używany przez pytest, ale pozbawiony detali
specyficznych dla pytest.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*.pyc
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
