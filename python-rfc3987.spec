Name:		python-rfc3987
Version:	1.3.8
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/rfc3987/rfc3987-%{version}.tar.gz
Summary:	Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
URL:		https://pypi.org/project/rfc3987/
License:	GNU GPLv3+
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)

%prep
%autosetup -p1 -n rfc3987-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/rfc3987.py
%{py_sitedir}/rfc3987-*.*-info
