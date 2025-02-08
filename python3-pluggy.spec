#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define 	module	pluggy
Summary:	Plugin and hook calling mechanisms for Python
Summary(pl.UTF-8):	Mechanizmy wtyczek dla Pythona
Name:		python3-%{module}
Version:	1.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pluggy/
Source0:	https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-%{version}.tar.gz
# Source0-md5:	ac0870be78ba0ee227a5c3955efeba59
URL:		https://pypi.org/project/pluggy/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
%if "%{py3_ver}" < "3.8"
BuildRequires:	python3-importlib_metadata >= 0.12
%endif
BuildRequires:	python3-pytest >= 3.7.0
BuildRequires:	python3-pytest-benchmark
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-pygments
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin manager as used by pytest but stripped of pytest specific
details.

%description -l pl.UTF-8
Zarządca wtyczek tak jak używany przez pytest, ale pozbawiony detali
specyficznych dla pytest.

%package apidocs
Summary:	API documentation for Python pluggy module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pluggy
Group:		Documentation

%description apidocs
API documentation for Python pluggy module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pluggy.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest testing
%endif

%if %{with doc}
PYTHONPATH="$PWD/src" \
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/pluggy
%{py3_sitescriptdir}/pluggy-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
