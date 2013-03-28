#
# Conditional build:
%bcond_without	a11y	# disable accessibility themes

Summary:	MATE Desktop themes
Name:		mate-themes
Version:	1.5.2
Release:	0.7
License:	GPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	81402f9bfaf482224502d8965b79da52
URL:		http://mate-desktop.org/
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk2-engines
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk2-engines
Requires:	gtk2-theme-engine-murrine
Requires:	mate-icon-theme >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE Desktop themes:

- AlaDelta: gtk2, metacity
- Aldabra: gtk2, gtk3, metacity
- Atlanta: metacity
- BlackMATE: cinnamon, gnome-shell, gtk2, gtk3, metacity
- Fog: metacity
- GreenLaguna: gtk2, gtk3, metacity
- Menta: cinnamon, gnome-shell, gtk2, gtk3, metacity, unity, xfwm4
- Menta-Black: metacity
- Quid: ? (x-gnome-metatheme)
- Shiny: gtk2, metacity
- Simply: gtk2
- TraditionalGreen: gtk2, gtk3, metacity
- TraditionalOk: gtk2, gtk3, metacity, openbox, xfwm4

%package accessibility
Summary:	Accessibility themes for MATE environment
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	mate-icon-theme >= 1.5

%description accessibility
Accessibility themes for MATE environment:

- ContrastHigh: gtk2, gtk3, metacity
- ContrastHighInverse: gtk2
- ContrastHighLargePrint: gtk2
- ContrastHighLargePrintInverse: gtk2
- ContrastLow: gtk2
- ContrastLowLargePrint: gtk2
- PrintLarge: gtk2
- Reverse: gtk2, metacity

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-silent-rules \
	%{__enable_disable a11y all-themes} \
	--enable-icon-mapping \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

for dir in $RPM_BUILD_ROOT%{_iconsdir}/*/; do
	gtk-update-icon-cache -ft $dir
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
for icon_theme in \
  Fog PrintLarge Quid Reverse Shiny Simply TraditionalOk \
  ContrastHighLargePrint ContrastHighLargePrintInverse \
  ContrastLow ContrastHigh ContrastHighInverse Aldabra ;
do
	/bin/touch --no-create %{_datadir}/icons/${icon_theme}
done

%postun
if [ $1 -eq 0 ]; then
	for icon_theme in \
	Fog PrintLarge Quid Reverse Shiny Simply TraditionalOk \
	ContrastHighLargePrint ContrastHighLargePrintInverse \
	ContrastLow ContrastHigh ContrastHighInverse Aldabra; do
		/bin/touch --no-create %{_datadir}/icons/${icon_theme}
		%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/${icon_theme}
	done
fi

%posttrans
for icon_theme in \
	Fog PrintLarge Quid Reverse Shiny Simply TraditionalOk \
	ContrastHighLargePrint ContrastHighLargePrintInverse \
	ContrastLow ContrastHigh ContrastHighInverse Aldabra; do
	%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/${icon_theme}
done
exit 0

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_datadir}/themes/AlaDelta
%{_datadir}/themes/Aldabra
%{_datadir}/themes/Atantla
%{_datadir}/themes/BlackMATE
%{_datadir}/themes/Fog
%{_datadir}/themes/GreenLaguna
%{_datadir}/themes/Menta
%{_datadir}/themes/Menta-Black
%{_datadir}/themes/Quid
%{_datadir}/themes/Shiny
%{_datadir}/themes/Simply
%{_datadir}/themes/TraditionalGreen
%{_datadir}/themes/TraditionalOk
%{_iconsdir}/Fog
%{_iconsdir}/Quid
%{_iconsdir}/mate/cursors

%files accessibility
%defattr(644,root,root,755)
%{_datadir}/themes/ContrastHigh
%{_datadir}/themes/ContrastHighInverse
%{_datadir}/themes/ContrastHighLargePrint
%{_datadir}/themes/ContrastHighLargePrintInverse
%{_datadir}/themes/ContrastLow
%{_datadir}/themes/ContrastLowLargePrint
%{_datadir}/themes/PrintLarge
%{_datadir}/themes/Reverse
%{_iconsdir}/ContrastHigh
%{_iconsdir}/ContrastHigh-SVG
%{_iconsdir}/ContrastHighInverse
%{_iconsdir}/ContrastHighLargePrint
%{_iconsdir}/ContrastHighLargePrintInverse
%{_iconsdir}/MateLargePrint
