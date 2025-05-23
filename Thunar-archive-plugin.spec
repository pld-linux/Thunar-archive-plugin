#
%define		srcname thunar-archive-plugin
#
Summary:	Archive plugin for the Thunar file manager
Summary(pl.UTF-8):	Wtyczka archiwum dla zarządcy plików Thunar
Name:		Thunar-archive-plugin
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/thunar-plugins/thunar-archive-plugin/0.6/%{srcname}-%{version}.tar.xz
# Source0-md5:	52f266214e7dfa952c83f8e3523f6956
URL:		https://foo-projects.org/~benny/projects/thunar-archive-plugin/
BuildRequires:	Thunar-devel >= 1.8.0
BuildRequires:	exo-devel >= 0.10.0
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxfce4util-devel >= 4.18.0
BuildRequires:	meson >= 0.61.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.18.0
Requires:	Thunar >= 1.8.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hy_AM,hye,hye_RU,ie,uz@Latn}

%find_lang %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{srcname}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS THANKS scripts/template.tap
%attr(755,root,root) %{_libdir}/thunarx-3/thunar-archive-plugin.so
%dir %{_libexecdir}/thunar-archive-plugin
%attr(755,root,root) %{_libexecdir}/thunar-archive-plugin/*.tap
%{_iconsdir}/hicolor/*/*/*
