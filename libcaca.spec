#
# Conditional build:
%bcond_without	dotnet		# C#/Mono binding
%bcond_without	java		# Java binding
%bcond_without	ruby		# Ruby binding
%bcond_without	python		# Python binding
%bcond_without	ncurses		# ncurses driver
%bcond_without	slang		# slang driver

%ifnarch %{ix86} %{x8664} alpha %{arm} hppa ia64 mips ppc s390 s390x sparc sparcv9
%undefine	with_dotnet
%endif
%ifarch i386
%undefine	with_dotnet
%endif

%define		rel	1
%define	subver	beta20
Summary:	Graphics library that outputs text instead of pixels
Summary(pl.UTF-8):	Biblioteka graficzna wyświetlająca tekst zamiast pikseli
Name:		libcaca
Version:	0.99
Release:	0.%{subver}.%{rel}
License:	WTFPL v2
Group:		Libraries
#Source0Download: https://github.com/cacalabs/libcaca/releases
Source0:	https://github.com/cacalabs/libcaca/releases/download/v%{version}.%{subver}/%{name}-%{version}.%{subver}.tar.bz2
# Source0-md5:	019c036ef038e7b5727b46f07fda739b
Patch0:		%{name}-monodir.patch
Patch1:		ruby-vendordir.patch
Patch2:		%{name}-sh.patch
Patch3:		%{name}-plugins.patch
Patch4:		%{name}-javah.patch
URL:		http://caca.zoy.org/wiki/libcaca
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	freeglut-devel >= 2.0.0
# not used
#BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	imlib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%{?with_ncurses:BuildRequires:	ncurses-devel >= 5}
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.533
BuildRequires:	sed >= 4.0
%{?with_slang:BuildRequires:	slang-devel >= 2.0.0}
#BuildRequires:	texlive-fonts-jknappen
#BuildRequires:	texlive-format-pdflatex
#BuildRequires:	texlive-latex-ams
#BuildRequires:	texlive-makeindex
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
%if %{with dotnet}
BuildRequires:	mono-csharp
%endif
%if %{with java}
BuildRequires:	jdk >= 1.8
BuildRequires:	rpm-javaprov
# org_zoy_caca_Attribute.c:14:18: fatal error: caca.h: No such file or directory
BuildRequires:	libcaca-devel
%endif
%if %{with python}
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
%endif
%if %{with ruby}
BuildRequires:	rpm-rubyprov
BuildRequires:	ruby-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
The libcaca library is a graphics library that outputs text instead of
pixels, so that it can work on older video cards or text terminals. It
is not unlike the famous AAlib library.

The differences with AAlib are the following:
- 16 available colours for character output (256 colour pairs)
- dithering of colour images
- basic sprite primitives

But libcaca also has the following limitations:
- no support for brightness, contrast, gamma
- unefficient character-choosing algorithms
- no raw keyboard support

%description -l pl.UTF-8
Biblioteka libcaca to biblioteka graficzna wyświetlająca tekst zamiast
pikseli, dzięki czemu może działać na starszych kartach graficznych
oraz terminalach tekstowych. Pod tym względem jest podobna do słynnej
biblioteki AAlib.

Różnice w stosunku do AAlib są następujące:
- 16 dostępnych kolorów dla znaków (256 par kolorów)
- dithering kolorowych obrazów
- proste kształty duszków (sprites)

Ale libcaca ma także następujące ograniczenia:
- brak obsługi jasności, kontrastu, korekcji gamma
- mało wydajne algorytmy wyboru znaków
- brak obsługi klawiatury w trybie surowym

%package plugin-GL
Summary:	GL plugin for libcaca library
Summary(pl.UTF-8):	Wtyczka GL dla biblioteki libcaca
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freeglut >= 2.0.0

%description plugin-GL
GL plugin for libcaca library.

%description plugin-GL -l pl.UTF-8
Wtyczka GL dla biblioteki libcaca.

%package plugin-X11
Summary:	X11 plugin for libcaca library
Summary(pl.UTF-8):	Wtyczka X11 dla biblioteki libcaca
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-X11
X11 plugin for libcaca library.

%description plugin-X11 -l pl.UTF-8
Wtyczka X11 dla biblioteki libcaca.

%package img
Summary:	libcaca-based image viewer and converter
Summary(pl.UTF-8):	Przeglądarka i konwerter obrazków oparte na libcaca
Group:		Applications/Graphics

%description img
libcaca-based image viewer and converter. They use imlib2 to load
images.

%description img -l pl.UTF-8
Przeglądarka i konwerter obrazków oparte na libcaca. Do wczytywania
obrazków używają biblioteki imlib2.

%package devel
Summary:	Header files for libcaca library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcaca
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	slang-devel >= 2.0.0

%description devel
Header files for libcaca library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcaca.

%package static
Summary:	Static libcaca library
Summary(pl.UTF-8):	Statyczna biblioteka libcaca
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcaca library.

%description static -l pl.UTF-8
Statyczna biblioteka libcaca.

%package c++
Summary:	C++ bindings for libcaca
Summary(pl.UTF-8):	Wiązania C++ do libcaca
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ bindings for libcaca.

%description c++ -l pl.UTF-8
Wiązania C++ do libcaca.

%package c++-devel
Summary:	C++ bindings for libcaca - header files
Summary(pl.UTF-8):	Wiązania C++ do libcaca - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
C++ bindings for libcaca - header files.

%description c++-devel -l pl.UTF-8
Wiązania C++ do libcaca - pliki nagłówkowe.

%package c++-static
Summary:	C++ bindings for libcaca - static libraries
Summary(pl.UTF-8):	Wiązania C++ do libcaca - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
C++ bindings for libcaca - static libraries.

%description c++-static -l pl.UTF-8
Wiązania C++ do libcaca - biblioteki statyczne.

%package apidocs
Summary:	API documentation for libcaca library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libcaca
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libcaca library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libcaca.

%package -n dotnet-caca-sharp
Summary:	C# bindings for libcaca
Summary(pl.UTF-8):	Wiązania C# do libcaca
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mono

%description -n dotnet-caca-sharp
C# bindings for libcaca.

%description -n dotnet-caca-sharp -l pl.UTF-8
Wiązania C# do libcaca.

%package -n java-caca
Summary:	Java bindings for libcaca
Summary(pl.UTF-8):	Wiązania Javy do libcaca
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jre

%description -n java-caca
Java bindings for libcaca.

%description -n java-caca -l pl.UTF-8
Wiązania Javy do libcaca.

%package -n python-caca
Summary:	Python bindings for libcaca
Summary(pl.UTF-8):	Wiązania Pythona do libcaca
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
# ctypes
Requires:	python-modules

%description -n python-caca
Python bindings for libcaca.

%description -n python-caca -l pl.UTF-8
Wiązania Pythona do libcaca.

%package -n ruby-caca
Summary:	Ruby bindings for libcaca
Summary(pl.UTF-8):	Wiązania języka Ruby do libcaca
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description -n ruby-caca
Ruby bindings for libcaca.

%description -n ruby-caca -l pl.UTF-8
Wiązania języka Ruby do libcaca.

%prep
%setup -q -n %{name}-%{version}.%{subver}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# NOTE: as of libcaca 0.99beta19 / doxygen 1.8.7 pdflatex fails - use
# KPSEWHICH hack to disable PDF documentation.
%configure \
	%{?with_dotnet:CSC=/usr/bin/dmcs} \
	KPSEWHICH=/nonexisting \
	--disable-cocoa \
	--enable-csharp%{!?with_dotnet:=no} \
	--enable-cxx \
	--enable-gl \
	--enable-java%{!?with_java:=no} \
	--enable-ncurses%{!?with_ncurses:=no} \
	--enable-plugins \
	--enable-slang%{!?with_slang:=no} \
	--enable-x11

# --disable-silent-rules doesn't work due to AM_DEFAULT_VERBOSITY=0; use V=1 instead
# ObjC file not used, use plain CC to link library to avoid C++/ObjC deps
%{__make} %{?with_java:-j1} \
	CLASSPATH=$(pwd)/java \
	OBJC="%{__cc}" \
	V=1 \
	jnidir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	jnidir=%{_libdir}

# replace symlink by groff include
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/cacademo.1
echo '.so cacafire.1' > $RPM_BUILD_ROOT%{_mandir}/man1/cacademo.1

# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caca/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{ruby_vendorarchdir}/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcaca*.la
# man3 pages have too common base names to be included
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/*.3caca
# packaged as %doc in -devel
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libcaca-dev

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	-n java-caca -p /sbin/ldconfig
%postun	-n java-caca -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS NOTES README THANKS
%attr(755,root,root) %{_bindir}/cacaclock
%attr(755,root,root) %{_bindir}/cacademo
%attr(755,root,root) %{_bindir}/cacafire
%attr(755,root,root) %{_bindir}/cacaplay
%attr(755,root,root) %{_bindir}/cacaserver
%attr(755,root,root) %{_libdir}/libcaca.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaca.so.0
%dir %{_libdir}/caca
%{_datadir}/%{name}
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacaplay.1*
%{_mandir}/man1/cacaserver.1*

%files plugin-GL
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caca/libgl_plugin.so*

%files plugin-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caca/libx11_plugin.so*

%files img
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cacaview
%attr(755,root,root) %{_bindir}/img2txt
%{_mandir}/man1/cacaview.1*
%{_mandir}/man1/img2txt.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caca-config
%attr(755,root,root) %{_libdir}/libcaca.so
%{_includedir}/caca.h
%{_includedir}/caca0.h
%{_includedir}/caca_conio.h
%{_includedir}/caca_types.h
%{_pkgconfigdir}/caca.pc
%{_mandir}/man1/caca-config.1*
# man3 pages have too common base names to be included

%files static
%defattr(644,root,root,755)
%{_libdir}/libcaca.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaca++.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca++.so
%{_includedir}/caca++.h
%{_pkgconfigdir}/caca++.pc

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libcaca++.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*

%if %{with dotnet}
%files -n dotnet-caca-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/caca-sharp-0.0
%{_prefix}/lib/mono/gac/caca-sharp
%endif

%if %{with java}
%files -n java-caca
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca-java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaca-java.so.0
%attr(755,root,root) %{_libdir}/libcaca-java.so
%{_javadir}/libjava.jar
%endif

%files -n python-caca
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/caca
%{py_sitescriptdir}/caca/*.py[co]

%files -n ruby-caca
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/caca.rb
%attr(755,root,root) %{ruby_vendorarchdir}/caca.so
