%define module netifaces

Name:          python-%module
Version:       0.8
Release:       2
Provides:      %{module} = %{version}
Requires:      python
BuildRequires: gcc
BuildRequires: python-devel
BuildRequires: python-setuptools
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

%prep
%setup -q -n %module-%{version}

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root %{buildroot} --install-purelib=%{py_platsitedir}

%files
%doc README
%{py_platsitedir}/*


%changelog
* Fri Nov 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6-1
+ Revision: 731515
- fix for new packaging policy and version bump

* Thu Jun 09 2011 Antoine Ginies <aginies@mandriva.com> 0.5-1
+ Revision: 683340
- fix provides
- import python-netifaces


