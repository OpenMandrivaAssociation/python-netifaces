%define module netifaces

Name:          python-%module
Version:       0.10.9
Release:       1
Provides:      %{module} = %{version}
Requires:      python
BuildRequires: pkgconfig(python3)
BuildRequires: python-setuptools
BuildRequires: pkgconfig(python2)
BuildRequires: python2-setuptools
Group:         Development/Python
License:       MIT
URL:           http://alastairs-place.net/netifaces/
Summary:       Portable network interface information
Source0:       https://files.pythonhosted.org/packages/0d/18/fd6e9c71a35b67a73160ec80a49da63d1eed2d2055054cc2995714949132/netifaces-%{version}.tar.gz

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
# -fno-lto is a workaround for setuptools brokenness -- it
# passes -flto to the compiler but not to the linker, even if
# it's mentioned in both CFLAGS and LDFLAGS.
# Not too bad though since this module is only one source file
# anyway. LTO doesn't make a difference here by definition.
pushd %py2dir
CFLAGS="%{optflags} -fno-lto" LDFLAGS="%{ldflags}" python2 setup.py build
popd

CFLAGS="%{optflags} -fno-lto" LDFLAGS="%{ldflags}" python setup.py build

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
