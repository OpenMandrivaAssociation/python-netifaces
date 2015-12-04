%define module netifaces

Name:          python-%module
Version:       0.10.4
Release:       1
Provides:      %{module} = %{version}
Requires:      python
BuildRequires: gcc
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: python2-devel
BuildRequires: python2-setuptools
Group:         Development/Python
License:       MIT
URL:           http://alastairs-place.net/netifaces/
Summary:       Portable network interface information

Source:        http://alastairs-place.net/projects/netifaces/netifaces-%{version}.tar.gz

%description
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux and
Solaris. On Windows, it is currently not able to retrieve IPv6 addresses,
owing to shortcomings of the Windows API.

It should work on other UNIX-like systems provided they implement either 
getifaddrs() or support the SIOCGIFxxx socket options, although the data
provided by the socket options is normally less complete.

%package -n python2-%module
Summary:	Portable network interface information
Group:		Development/Python

%description -n python2-%module
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux and
Solaris. On Windows, it is currently not able to retrieve IPv6 addresses,
owing to shortcomings of the Windows API.

It should work on other UNIX-like systems provided they implement either
getifaddrs() or support the SIOCGIFxxx socket options, although the data
provided by the socket options is normally less complete.

%prep
%setup -q -n %module-%{version}
cp -a . %py2dir

%build
pushd %py2dir
CFLAGS="-fno-lto" python2 setup.py build
popd

CFLAGS="-fno-lto" python setup.py build

%install
pushd %py2dir
python2 setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}
popd

python setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

%files
%doc README.rst
%{py_platsitedir}/*

%files -n python2-%module
%doc README.rst
%{py2_platsitedir}/*

%changelog
* Fri Nov 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6-1
+ Revision: 731515
- fix for new packaging policy and version bump

* Thu Jun 09 2011 Antoine Ginies <aginies@mandriva.com> 0.5-1
+ Revision: 683340
- fix provides
- import python-netifaces


