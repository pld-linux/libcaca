#
# Conditional build:
%bcond_without	dotnet		# don't build mono plugin
#
%ifnarch %{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
%undefine	with_dotnet
%endif
%ifarch i386
%undefine	with_dotnet
%endif

%{?with_dotnet:%include	/usr/lib/rpm/macros.mono}
Summary:	Graphics library that outputs text instead of pixels
Summary(pl.UTF-8):	Biblioteka graficzna wyświetlająca tekst zamiast pikseli
Name:		libcaca
Version:	0.99
%define	subver	beta17
Release:	0.%{subver}.1
License:	WTFPL
Group:		Libraries
Source0:	http://libcaca.zoy.org/files/libcaca/%{name}-%{version}.%{subver}.tar.gz
# Source0-md5:	790d6e26b7950e15909fdbeb23a7ea87
Patch0:		install.patch
URL:		http://libcaca.zoy.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	freeglut-devel >= 2.0.0
BuildRequires:	imlib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?with_dotnet:BuildRequires:	mono-csharp}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.533
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	ruby-devel
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel >= 2.0.0
# shouldn't these be in doxygen requirements?
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	tetex-makeindex
BuildRequires:	tetex-metafont
BuildRequires:	xorg-lib-libX11-devel
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
%undos */Makefile.am
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# NOTE: ncurses driver builds, but there's no color when linked against
# ABI 6. While caca defaults to ncurses this must be disabled until fixed.
%configure \
	--disable-ncurses \
	--%{!?with_dotnet:dis}%{?with_dotnet:en}able-csharp \
	--disable-java \
	--enable-cxx \
	--enable-gl \
	--enable-plugins \
	--enable-slang \
	--enable-x11


# ObjC file not used, use plain CC to link library to avoid C++/ObjC deps
%{__make} \
	OBJC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# replace symlink by groff include
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/cacademo.1
echo '.so cacafire.1' > $RPM_BUILD_ROOT%{_mandir}/man1/cacademo.1

rm -f $RPM_BUILD_ROOT%{_libdir}/caca/*.{a,la}
rm -f $RPM_BUILD_ROOT%{ruby_sitearchdir}/*.{a,la}
# man3 pages have too common base names to be included
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/*.3caca
rm -rf $RPM_BUILD_ROOT%{_docdir}/libcucul-dev

cd $RPM_BUILD_ROOT%{_libdir}
for i in libcaca*.so.*.*.*; do
	ln -sf $i $(echo $i |sed 's/caca/cucul/')
done
ln -sf libcaca.a	$RPM_BUILD_ROOT%{_libdir}/libcucul.a
ln -sf libcaca.la	$RPM_BUILD_ROOT%{_libdir}/libcucul.la
ln -sf libcaca.so	$RPM_BUILD_ROOT%{_libdir}/libcucul.so
ln -sf libcaca.so.0 	$RPM_BUILD_ROOT%{_libdir}/libcucul.so.0
ln -sf libcaca++.a	$RPM_BUILD_ROOT%{_libdir}/libcucul++.a
ln -sf libcaca++.la	$RPM_BUILD_ROOT%{_libdir}/libcucul++.la
ln -sf libcaca++.so 	$RPM_BUILD_ROOT%{_libdir}/libcucul++.so
ln -sf libcaca++.so.0 	$RPM_BUILD_ROOT%{_libdir}/libcucul++.so.0
ln -sf caca-sharp 	$RPM_BUILD_ROOT%{_libdir}/cucul-sharp
ln -sf caca++.h 	$RPM_BUILD_ROOT%{_includedir}/cucul++.h
ln -sf caca_types.h 	$RPM_BUILD_ROOT%{_includedir}/cucul_types.h
#ln -sf caca_types++.h 	$RPM_BUILD_ROOT%{_includedir}/cucul_types++.h
ln -sf caca.so 		$RPM_BUILD_ROOT%{ruby_sitearchdir}/cucul.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS NOTES README THANKS
%attr(755,root,root) %{_bindir}/cacademo
%attr(755,root,root) %{_bindir}/cacafire
%attr(755,root,root) %{_bindir}/cacaplay
%attr(755,root,root) %{_bindir}/cacaserver
%attr(755,root,root) %{_libdir}/libcaca.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaca.so.0
%attr(755,root,root) %{_libdir}/libcucul.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcucul.so.0
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
%attr(755,root,root) %{_libdir}/libcucul.so
%{_libdir}/libcaca.la
%{_libdir}/libcucul.la
%{_includedir}/caca.h
%{_includedir}/caca0.h
%{_includedir}/caca_types.h
%{_includedir}/cucul.h
%{_includedir}/cucul_types.h
%{_pkgconfigdir}/caca.pc
%{_pkgconfigdir}/cucul.pc
%{_mandir}/man1/caca-config.1*
# man3 pages have too common base names to be included

%files static
%defattr(644,root,root,755)
%{_libdir}/libcaca.a
%{_libdir}/libcucul.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcaca++.so.0
%attr(755,root,root) %{_libdir}/libcucul++.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcucul++.so.0

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca++.so
%attr(755,root,root) %{_libdir}/libcucul++.so
%{_libdir}/libcaca++.la
%{_libdir}/libcucul++.la
%{_includedir}/caca++.h
%{_includedir}/cucul++.h
%{_pkgconfigdir}/caca++.pc
%{_pkgconfigdir}/cucul++.pc

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libcaca++.a
%{_libdir}/libcucul++.a

%if %{with dotnet}
%files -n dotnet-caca-sharp
%defattr(644,root,root,755)
%{_libdir}/caca-sharp
%{_libdir}/cucul-sharp
%endif

%files -n ruby-caca
%defattr(644,root,root,755)
%{ruby_sitelibdir}/caca.rb
%attr(755,root,root) %{ruby_sitearchdir}/caca.so
%attr(755,root,root) %{ruby_sitearchdir}/cucul.so
