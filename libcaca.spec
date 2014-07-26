#
# Conditional build:
%bcond_without	dotnet		# C#/Mono binding
%bcond_without	java		# Java binding
#
%ifnarch %{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
%undefine	with_dotnet
%endif
%ifarch i386
%undefine	with_dotnet
%endif

%define		rel	3
%define	subver	beta19
%{?with_dotnet:%include	/usr/lib/rpm/macros.mono}
Summary:	Graphics library that outputs text instead of pixels
Summary(pl.UTF-8):	Biblioteka graficzna wyświetlająca tekst zamiast pikseli
Name:		libcaca
Version:	0.99
Release:	0.%{subver}.%{rel}
License:	WTFPL v2
Group:		Libraries
Source0:	http://caca.zoy.org/raw-attachment/wiki/libcaca/%{name}-%{version}.%{subver}.tar.gz
# Source0-md5:	a3d4441cdef488099f4a92f4c6c1da00
Patch0:		%{name}-monodir.patch
URL:		http://caca.zoy.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	freeglut-devel >= 2.0.0
# not used
#BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	imlib2-devel
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%{?with_dotnet:BuildRequires:	mono-csharp}
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpmbuild(macros) >= 1.533
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	ruby-devel
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel >= 2.0.0
#BuildRequires:	texlive-fonts-jknappen
#BuildRequires:	texlive-format-pdflatex
#BuildRequires:	texlive-latex-ams
#BuildRequires:	texlive-makeindex
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
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
%{?ruby_ver_requires_eq}

%description -n ruby-caca
Ruby bindings for libcaca.

%description -n ruby-caca -l pl.UTF-8
Wiązania języka Ruby do libcaca.

%prep
%setup -q -n %{name}-%{version}.%{subver}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# NOTE: ncurses driver builds, but there's no color when linked against
# ABI 6. While caca defaults to ncurses this must be disabled until fixed.
# NOTE: as of libcaca 0.99beta19 / doxygen 1.8.7 pdflatex fails - use
# KPSEWHICH hack to disable PDF documentation.
%configure \
	KPSEWHICH=/nonexisting \
	--enable-csharp%{!?with_dotnet:=no} \
	--enable-cxx \
	--enable-gl \
	--enable-java%{!?with_java:=no} \
	--disable-ncurses \
	--enable-plugins \
	--enable-slang \
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
%{__rm} $RPM_BUILD_ROOT%{ruby_sitearchdir}/*.la
%if %{with java}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcaca-java.la
%endif
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
%doc AUTHORS COPYING ChangeLog NEWS NOTES README THANKS
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
%doc doc/html/*
%attr(755,root,root) %{_bindir}/caca-config
%attr(755,root,root) %{_libdir}/libcaca.so
%{_libdir}/libcaca.la
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
%{_libdir}/libcaca++.la
%{_includedir}/caca++.h
%{_pkgconfigdir}/caca++.pc

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libcaca++.a

%if %{with dotnet}
%files -n dotnet-caca-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/caca-sharp-0.0
%{_prefix}/lib/mono/gac/caca-sharp
%{_javadir}/libjava.jar
%endif

%if %{with dotnet}
%files -n java-caca
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca-java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaca-java.so.0
%attr(755,root,root) %{_libdir}/libcaca-java.so
%endif

%files -n python-caca
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/caca
%{py_sitescriptdir}/caca/*.py[co]

%files -n ruby-caca
%defattr(644,root,root,755)
%{ruby_sitelibdir}/caca.rb
%attr(755,root,root) %{ruby_sitearchdir}/caca.so
