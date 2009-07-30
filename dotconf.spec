%define name dotconf
%define	major 1
%define version 1.0.13
%define release %mkrel 4
%define	libname_orig libdotconf
%define	libname %mklibname dotconf %{major}
%define	libnamedevel %mklibname dotconf -d
%define	libnamestaticdevel %mklibname dotconf -d -s

Name: %{name}
Summary: A ConfigurationFile Parser Library
Version: %{version}
Release: %{release}
License: LGPL
#v2.1
Group: System/Libraries
URL: http://www.azzit.de/dotconf/
# (fc) 1.0.13-2mdv fix aclocal warning
Patch0:	dotconf-1.0.13-aclocal-warning.patch
Source: http://www.azzit.de/dotconf/download/v1.0/%{name}-%{version}.tar.gz
BuildRequires: recode
%if %mdkversion < 200800
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%endif

%description
Dotconf is a configuration file parser library.

%package -n %{libname}
Summary: The shared libraries needed for running programs using dotconf
Group: System/Libraries
Provides: %{libname_orig} = %{version}-%{release}
Provides: %{name} = %{version}-%{release}

%description -n	%{libname}
Dotconf is a configuration file parser library.
This package contains only the shared libraries needed for running programs 
dynamically linked against dotconf.

%package -n %{libnamedevel}
Summary: The libraries and headers needed for dotconf development
License: LGPL
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}

%description -n %{libnamedevel}
Dotconf is a configuration file parser library.
This package contains documentation, headers and shared library symlinks 
needed for dotconf development.

%package -n %{libnamestaticdevel}
Summary: Static libraries for dotconf development
License: LGPL
Group: Development/C
Requires: %{libnamedevel} = %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %{libnamestaticdevel}
Dotconf is a configuration file parser library.
This package contains only the static libraries for dotconf devlopment.

%package -n %{name}-examples
Summary: The examples for the dotconf library
Group: Development/C
Obsoletes:	%{libname}-examples < %{version}-%{release}
Provides:	%{libname}-examples = %{version}-%{release}

%description -n	 %{name}-examples
Dotconf is a configuration file parser library.
This package contains examples, installed in the same place as the 
documentation.

%prep
%setup -q
%patch0 -p1 -b .aclocal-warning
recode l1..u8 AUTHORS doc/dotconf-features.txt

#fix build
autoreconf -i

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README doc/dotconf*
%{_bindir}/%{name}-config
%{_includedir}/*.h
%{_datadir}/aclocal/%{name}.m4
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libnamestaticdevel}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.la

%files -n %{name}-examples
%defattr(-,root,root)
%doc examples/*

