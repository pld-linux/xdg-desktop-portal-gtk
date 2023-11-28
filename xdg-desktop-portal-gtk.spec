Summary:	Gtk implementation of xdg-desktop-portal
Name:		xdg-desktop-portal-gtk
Version:	1.15.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://github.com/flatpak/xdg-desktop-portal-gtk/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9c7836b1fe09bc914ea4c06b9c58231f
URL:		https://github.com/flatpak/xdg-desktop-portal-gtk
BuildRequires:	fontconfig-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.21.5
BuildRequires:	meson >= 0.61.2
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xdg-desktop-portal-devel >= 1.14.0
BuildRequires:	xz
Requires:	glib2 >= 1:2.44
Requires:	gtk+3 >= 3.21.5
Requires:	xdg-desktop-portal >= 1.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A backend implementation for xdg-desktop-portal that is using GTK and
various pieces of GNOME infrastructure, such as org.gnome.desktop.*
GSettings schemas and the org.gnome.SessionManager and
org.gnome.Screensaver D-Bus interfaces.

%prep
%setup -q

%build
%meson build \
	-Dsystemd-user-unit-dir=%{systemduserunitdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang xdg-desktop-portal-gtk

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post xdg-desktop-portal-gtk.service

%preun
%systemd_user_preun xdg-desktop-portal-gtk.service

%files -f xdg-desktop-portal-gtk.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal-gtk
%{systemduserunitdir}/xdg-desktop-portal-gtk.service
%{_desktopdir}/xdg-desktop-portal-gtk.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
%{_datadir}/xdg-desktop-portal/portals/gtk.portal
