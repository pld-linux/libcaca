Summary:	Graphics library that outputs text instead of pixels
Summary(pl.UTF-8):	Biblioteka graficzna wyświetlająca tekst zamiast pikseli
Name:		libcaca
Version:	0.99
%define	bver	beta11
Release:	0.%{bver}.1
License:	WTFPL
Group:		Libraries
Source0:	http://libcaca.zoy.org/files/%{name}-%{version}.%{bver}.tar.gz
# Source0-md5:	94f3ae45b9d7fed43a6511452e880937
URL:		http://libcaca.zoy.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	freeglut-devel >= 2.0.0
BuildRequires:	imlib2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Biblioteka libcaca to biblioteka graficzna wyświetlająca tekst
zamiast pikseli, dzięki czemu może działać na starszych kartach
graficznych oraz terminalach tekstowych. Pod tym względem jest
podobna do słynnej biblioteki AAlib.

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
Requires:	%{name} = %{version}-%{release}

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

%prep
%setup -q -n %{name}-%{version}.%{bver}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gl \
	--disable-ncurses \
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
# man3 pages have too common base names to be included
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/*.3caca
rm -rf $RPM_BUILD_ROOT%{_docdir}/libcucul-dev

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS NOTES README THANKS TODO
%attr(755,root,root) %{_bindir}/cacademo
%attr(755,root,root) %{_bindir}/cacafire
%attr(755,root,root) %{_bindir}/cacaplay
%attr(755,root,root) %{_bindir}/cacaserver
%attr(755,root,root) %{_libdir}/libcaca.so.*.*.*
%attr(755,root,root) %{_libdir}/libcucul.so.*.*.*
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
%attr(755,root,root) %{_bindir}/img2irc
%{_mandir}/man1/cacaview.1*
%{_mandir}/man1/img2irc.1*

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
%{_includedir}/cucul.h
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
%attr(755,root,root) %{_libdir}/libcucul++.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcaca++.so
%attr(755,root,root) %{_libdir}/libcucul++.so
%{_libdir}/libcaca++.la
%{_libdir}/libcucul++.la
%{_includedir}/caca++.h
%{_includedir}/cucul++.h

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libcaca++.a
%{_libdir}/libcucul++.a
