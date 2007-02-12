#
%define		srcname thunar-archive-plugin
#
Summary:	Archive plugin for the Thunar file manager
Summary(pl.UTF-8):   Wtyczka archiwum dla zarządcy plików Thunar
Name:		Thunar-archive-plugin
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{srcname}-%{version}.tar.bz2
# Source0-md5:	4c389e6328af9322937af76382f0baec
URL:		http://foo-projects.org/~benny/projects/thunar-archive-plugin/
BuildRequires:	Thunar-devel >= 0.8.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.4.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	Thunar >= 0.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows to create and extract archive files using the file
context menus in the Thunar file manager. It provides a generic
scripting interface for archive managers.

%description -l pl.UTF-8
Ta wtyczka umożliwia tworzenie i rozpakowywanie archiwów używając menu
podręcznego pliku w zarządcy plików Thunar. Dostarcza ogólny interfejs
dla zarządców archiwów.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/thunarx-1/*.la

%find_lang %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{srcname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS scripts/template.tap
%attr(755,root,root) %{_libdir}/thunarx-1/*
%dir %{_libdir}/thunar-archive-plugin
%attr(755,root,root) %{_libdir}/thunar-archive-plugin/*.tap
%{_iconsdir}/hicolor/*/*/*
