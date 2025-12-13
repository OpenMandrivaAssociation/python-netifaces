%global debug_package %{nil}
%define module netifaces

Name:          python-%module
Version:       0.11.0
Release:       3
Provides:      %{module} = %{version}
BuildSystem:   python
BuildRequires: pkgconfig(python3)
BuildRequires: python%{pyver}dist(setuptools)
Group:         Development/Python
License:       MIT
URL:           https://alastairs-place.net/netifaces/
Summary:       Portable network interface information
Source0:       https://files.pythonhosted.org/packages/source/n/netifaces/netifaces-%{version}.tar.gz
# Dropped after 6.0 2025-12-13
Obsoletes:     python2-%module < %{EVRD}

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

%files
%doc README.rst
%{py_platsitedir}/*
