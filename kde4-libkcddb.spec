%define		_state		stable
%define		orgname		libkcddb
%define		qtver		4.8.1

Summary:	CDDB accessing library
Summary(pl.UTF-8):	Biblioteka dostępu do baz CDDB
Name:		kde4-%{orgname}
Version:	4.9.0
Release:	0.1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d3d957c8e44de759cbc0939b0c8e9369
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cdparanoia-III-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libmusicbrainz3-devel >= 1:3.0.0
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xine-lib-devel >= 1:1.0
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	zlib-devel
Requires:	kde4-kdelibs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for accessing CDDB (cd track information databases) services.

%description -l pl.UTF-8
Biblioteka dostępu do serwisów CDDB (baz danych z informacjami o
utworach).

%package devel
Summary:	Header files for libkcddb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libkcddb
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
Header files for libkcddb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libkcddb.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcddb.so.4.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcddb.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/libkcddb
%attr(755,root,root) %{_libdir}/libkcddb.so
