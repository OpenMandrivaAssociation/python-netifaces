%define module netifaces

Name:          python-%module
Version:       0.5
Release:       %mkrel 1
Provides:      %{module}
Requires:      python
BuildRequires: gcc
BuildRequires: python-devel
BuildRequires: python-setuptools
Group:         Development/Python
License:       MIT
URL:           http://alastairs-place.net/netifaces/
Summary:       Portable network interface information
Source:        %{module}-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{python_sitearch}/*

