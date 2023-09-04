Summary:	CLEW - OpenCL Extension Wrangler library
Summary(pl.UTF-8):	CLEW - biblioteka wczytująca rozszerzenia OpenCL
Name:		clew
Version:	0.10
Release:	1
# clew.h is MIT, clew.c Boost v1.0
License:	MIT, Boost v1.0
Group:		Libraries
#Source0Download: https://github.com/martijnberger/clew/releases
Source0:	https://github.com/martijnberger/clew/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a2d3938159653e6e52f050b3dd235ca6
URL:		https://github.com/martijnberger/clew
BuildRequires:	libtool
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenCL Extension Wrangler Library (CLEW) is a cross-platform
open-source C/C++ extension loading library. CLEW provides efficient
run-time mechanisms for determining which OpenCL extensions are
supported on the target platform. OpenCL core and extension
functionality is exposed in a single header file.

%description -l pl.UTF-8
CLEW (OpenCL Extension Wrangler Library) to wieloplatformowa
biblioteka C/C++ o otwartych źródłach wczytująca rozszerzenia OpenCL.
Zapewnia wydajne mechanizmy pozwalające na określenie w czasie
działania programu, które rozszerzenia OpenCL są obsługiwane na
platformie docelowej. Podstawa oraz rozszerzenia OpenCL są
udostępnione poprzez pojedynczy plik nagłówkowy.

%package devel
Summary:	Header files for CLEW library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CLEW
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CLEW library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CLEW.

%package static
Summary:	Static CLEW library
Summary(pl.UTF-8):	Statyczna biblioteka CLEW
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CLEW library.

%description static -l pl.UTF-8
Statyczna biblioteka CLEW.

%prep
%setup -q

%build
libtool --mode=compile %{__cc} -c %{rpmcflags} %{rpmcppflags} -Iinclude -o src/clew.lo src/clew.c
libtool --mode=link %{__cc} %{rpmldflags} %{rpmcflags} -o libclew.la src/clew.lo -rpath %{_libdir} -version-info 1:0:0 -ldl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

libtool --mode=install install libclew.la $RPM_BUILD_ROOT%{_libdir}
cp -p include/clew.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclew.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclew.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclew.so
%{_libdir}/libclew.la
%{_includedir}/clew.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libclew.a
