%define	major	0
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	A ConfigurationFile Parser Library
Name:		dotconf
Version:	1.3
Release:	9
License:	LGPLv2.1
Group:		System/Libraries
Url:		https://github.com/williamh/dotconf
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	recode

%description
Dotconf is a configuration file parser library.

%package -n %{libname}
Summary:	The shared libraries needed for running programs using dotconf
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}dotconf1 < 1.3-2

%description -n	%{libname}
Dotconf is a configuration file parser library.
This package contains only the shared libraries needed for running programs 
dynamically linked against dotconf.

%package -n %{devname}
Summary:	The libraries and headers needed for dotconf development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}dotconf-static-devel < 1.3-2

%description -n %{devname}
Dotconf is a configuration file parser library.
This package contains documentation, headers and shared library symlinks 
needed for dotconf development.

%package -n %{name}-examples
Summary:	The examples for the dotconf library
Group:		Development/C
Provides:	%{libname}-examples = %{version}-%{release}

%description -n	%{name}-examples
Dotconf is a configuration file parser library.
This package contains examples, installed in the same place as the 
documentation.

%prep
%setup -q
recode l1..u8 AUTHORS doc/dotconf-features.txt

#fix build
autoreconf -i

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall

%files -n %{libname}
%{_libdir}/libdotconf.so.%{major}*

%files -n %{devname}
%doc AUTHORS README doc/dotconf*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{name}-examples
%doc examples/*
%doc %_docdir/%name

