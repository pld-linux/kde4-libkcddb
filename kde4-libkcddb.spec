%define		_state		stable
%define		orgname		libkcddb
%define		qtver		4.8.1

Summary:	CDDB accessing library
Summary(pl.UTF-8):	Biblioteka dostępu do baz CDDB
Name:		kde4-%{orgname}
Version:	4.9.1
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ebdef6e8697921fa66b405807c074bf4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kde4-kdemultimedia-libkcddb < 4.8.99-1
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
Requires:	%{name} >= %{version}-%{release}
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
%attr(755,root,root) %{_libdir}/kde4/kcm_cddb.so
%{_datadir}/apps/kconf_update/kcmcddb-emailsettings.upd
%{_datadir}/config.kcfg/libkcddb.kcfg
%{_datadir}/kde4/services/libkcddb.desktop
%{_docdir}/kde/HTML/en/kcontrol/cddbretrieval

%files devel
%defattr(644,root,root,755)
%{_includedir}/libkcddb
%attr(755,root,root) %{_libdir}/libkcddb.so
%dir %{_libdir}/cmake/libkcddb
%{_libdir}/cmake/libkcddb/LibkcddbConfig.cmake
%{_libdir}/cmake/libkcddb/LibkcddbTargets-pld.cmake
%{_libdir}/cmake/libkcddb/LibkcddbTargets.cmake
