Summary:	Graphics library that outputs text instead of pixels
Summary(pl):	Biblioteka graficzna wy¶wietlaj±ca tekst zamiast pikseli
Name:		libcaca
Version:	0.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://sam.zoy.org/projects/libcaca/%{name}-%{version}.tar.bz2
# Source0-md5:	0540e5c24aa6747c67805958185afe3b
Patch0:		%{name}-shared.patch
URL:		http://sam.zoy.org/projects/libcaca/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	imlib2-devel
BuildRequires:	libtool
BuildRequires:	slang-devel
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

%description -l pl
Biblioteka libcaca to biblioteka graficzna wy¶wietlaj±ca tekst zamiast
pikseli, dziêki czemu mo¿e dzia³aæ na starszych kartach graficznych
oraz terminalach tekstowych. Pod tym wzglêdem jest podobna do s³ynnej
biblioteki AAlib.

Ró¿nice w stosunku do AAlib s± nastêpuj±ce:
- 16 dostêpnych kolorów dla znaków (256 par kolorów)
- dithering kolorowych obrazów
- proste kszta³ty duszków (sprites)

Ale libcaca ma tak¿e nastêpuj±ce ograniczenia:
- brak obs³ugi jasno¶ci, kontrakstu, korekcji gamma
- ma³o wydajne algorytmy wyboru znaków
- brak obs³ugi klawiatury w trybie surowym

%package devel
Summary:	Header files for libcaca library
Summary(pl):	Pliki nag³ówkowe biblioteki libcaca
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	slang-devel

%description devel
Header files for libcaca library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libcaca.

%package static
Summary:	Static libcaca library
Summary(pl):	Statyczna biblioteka libcaca
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcaca library.

%description static -l pl
Statyczna biblioteka libcaca.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-x11 \
	--disable-ncurses \
	--enable-slang

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# replace symlink by groff include
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/cacafire.1
echo '.so cacademo.1' > $RPM_BUILD_ROOT%{_mandir}/man1/cacafire.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS NOTES README TODO
%attr(755,root,root) %{_bindir}/caca-spritedit
%attr(755,root,root) %{_bindir}/cacademo
%attr(755,root,root) %{_bindir}/cacafire
%attr(755,root,root) %{_bindir}/cacaview
%attr(755,root,root) %{_libdir}/libcaca.so.*.*.*
%{_datadir}/%{name}
%{_mandir}/man1/caca-spritedit.1*
%{_mandir}/man1/cacademo.1*
%{_mandir}/man1/cacafire.1*
%{_mandir}/man1/cacaview.1*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/caca-config
%attr(755,root,root) %{_libdir}/libcaca.so
%{_libdir}/libcaca.la
%{_includedir}/*.h
# man3 pages have too common base names to be included

%files static
%defattr(644,root,root,755)
%{_libdir}/libcaca.a
