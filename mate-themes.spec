Summary:	MATE Desktop themes
Name:		mate-themes
Version:	1.5.0
Release:	0.4
License:	GPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	dd187acc5ccefc60b7b0309ee14a4912
URL:		http://mate-desktop.org/
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	mate-icon-theme-devel
BuildRequires:	pkgconfig(gtk-engines-2)
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk2-engines
Requires:	gtk2-theme-engine-murrine
Requires:	mate-icon-theme >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE Desktop themes.

%package accessibility
Summary:	Accessibility themes for MATE environment
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	mate-icon-theme >= %{version}

%description accessibility
Accessibility themes for MATE environment.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-all-themes \
	--enable-icon-mapping \

%{__make} \
	V=1

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
%{_datadir}/themes/Fog
%{_datadir}/themes/Quid
%{_datadir}/themes/Shiny
%{_datadir}/themes/Simply
%{_datadir}/themes/TraditionalOk
%{_datadir}/themes/TraditionalOkClassic
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
%{_datadir}/themes/Reverse
%{_iconsdir}/ContrastHigh
%{_iconsdir}/ContrastHigh-SVG
%{_iconsdir}/ContrastHighInverse
%{_iconsdir}/ContrastHighLargePrint
%{_iconsdir}/ContrastHighLargePrintInverse
%{_iconsdir}/MateLargePrint
%{_datadir}/themes/PrintLarge
