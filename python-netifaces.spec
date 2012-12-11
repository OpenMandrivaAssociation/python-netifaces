%define module netifaces

Name:          python-%module
Version:       0.6
Release:       1
Provides:      %{module} = %{version}
Requires:      python
BuildRequires: gcc
BuildRequires: python-devel
BuildRequires: python-setuptools
Group:         Development/Python
License:       MIT
URL:           http://alastairs-place.net/netifaces/
Summary:       Portable network interface information
Source:        %{module}-%{version}.tar.gz

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
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT --install-purelib=%{python_sitearch}

%files
%doc README
%{python_sitearch}/*


%changelog
* Fri Nov 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6-1
+ Revision: 731515
- fix for new packaging policy and version bump

* Thu Jun 09 2011 Antoine Ginies <aginies@mandriva.com> 0.5-1
+ Revision: 683340
- fix provides
- import python-netifaces

