Summary:	Graphics library that outputs text instead of pixels
Summary(pl):	Biblioteka graficzna wyświetlająca tekst zamiast pikseli
Name:		libcaca
Version:	0.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://sam.zoy.org/projects/libcaca/%{name}-%{version}.tar.bz2
# Source0-md5:	be42552eace04fd0c02343b8b6c6b308
BuildRequires:	XFree86-devel
#BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q

%build
# TODO: fix configure, so it can find ncurses includes
%configure \
	--prefix=%{_prefix} \
	--enable-x11 \
	--disable-ncurses

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS NOTES README TODO
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
