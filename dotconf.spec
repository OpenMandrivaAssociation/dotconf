%define	major 1
%define	libname_orig libdotconf
%define	libname %mklibname dotconf %{major}
%define	libnamedevel %mklibname dotconf -d
%define	libnamestaticdevel %mklibname dotconf -d -s

Name: dotconf
Summary: A ConfigurationFile Parser Library
Version: 1.3
Release: 1
License: LGPL
#v2.1
Group: System/Libraries
URL: https://github.com/williamh/dotconf
Source0: dotconf-%version.tar.xz
BuildRequires: recode

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
recode l1..u8 AUTHORS doc/dotconf-features.txt

#fix build
autoreconf -i

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr(-,root,root)
%doc AUTHORS README doc/dotconf*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libnamestaticdevel}
%defattr(-,root,root)
%{_libdir}/*.a

%files -n %{name}-examples
%defattr(-,root,root)
%doc examples/*
%doc %_docdir/%name



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-7mdv2011.0
+ Revision: 663846
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-6mdv2011.0
+ Revision: 604812
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-5mdv2010.1
+ Revision: 522483
- rebuilt for 2010.1

* Thu Jul 30 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0.13-4mdv2010.0
+ Revision: 404650
- Fix build

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.13-4mdv2009.0
+ Revision: 244518
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Mar 13 2008 Frederic Crozat <fcrozat@mandriva.com> 1.0.13-2mdv2008.1
+ Revision: 187511
- Patch0: fix aclocal warning

* Tue Dec 18 2007 Guillaume Bedot <littletux@mandriva.org> 1.0.13-1mdv2008.1
+ Revision: 132128
- import dotconf


* Tue Dec 18 2007 Guillaume Bedot <littletux@mandriva.org> 1.0.13-1mdv2008.1
- First package of dotconf for MandrivaLinux.
