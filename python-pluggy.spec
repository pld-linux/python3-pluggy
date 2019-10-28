#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pluggy
Summary:	Plugin and hook calling mechanisms for Python
Summary(pl.UTF-8):	Mechanizmy wtyczek dla Pythona
Name:		python-%{module}
Version:	0.8.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pluggy/
Source0:	https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-%{version}.tar.gz
# Source0-md5:	12ddd25322d909a286c4018d18fddc79
URL:		https://pypi.org/project/pluggy/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.7.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.7.0
%endif
%endif
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
Plugin manager as used by pytest but stripped of pytest specific
details.

%description -n python3-%{module} -l pl.UTF-8
Zarządca wtyczek tak jak używany przez pytest, ale pozbawiony detali
specyficznych dla pytest.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest testing
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest testing
%endif
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
%doc LICENSE README.rst
%{py_sitescriptdir}/pluggy
%{py_sitescriptdir}/pluggy-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pluggy
%{py3_sitescriptdir}/pluggy-%{version}-py*.egg-info
%endif
