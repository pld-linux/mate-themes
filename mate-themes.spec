%define	gtk3_mver	3.22
Summary:	MATE Desktop themes
Summary(pl.UTF-8):	Motywy dla środowiska MATE Desktop
Name:		mate-themes
Version:	3.22.26
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	https://pub.mate-desktop.org/releases/themes/%{gtk3_mver}/%{name}-%{version}.tar.xz
# Source0-md5:	4c8b589f2a9acacaf5e946430649ccbd
Patch0:		noarch-build.patch
URL:		https://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gdk-pixbuf2-devel >= 2.0.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Requires:	gtk2-engines
Requires:	gtk2-theme-engine-murrine >= 0.98
Requires:	mate-icon-theme >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE Desktop themes:

- BlackMATE: cinnamon, gtk2, gtk3, marco, unity
- BlueMenta: cinnamon, gtk2, gtk3, marco, unity, xfwm4
- Blue-Submarine: cinnamon, gtk2, gtk3, marco
- GreenLaguna: gtk2, gtk3, marco, unity
- Green-Submarine: cinnamon, gtk2, gtk3, marco
- Menta: cinnamon, gtk2, gtk3, marco, unity, xfwm4
- Shiny: marco
- TraditionalGreen: gtk2, gtk3, marco
- TraditionalOk: gtk2, gtk3, marco, openbox, xfwm4

%description -l pl.UTF-8
Motywy dla środowiska MATE Desktop:

- BlackMATE: cinnamon, gtk2, gtk3, marco, unity
- BlueMenta: cinnamon, gtk2, gtk3, marco, unity, xfwm4
- Blue-Submarine: cinnamon, gtk2, gtk3, marco
- GreenLaguna: gtk2, gtk3, marco, unity
- Green-Submarine: cinnamon, gtk2, gtk3, marco
- Menta: cinnamon, gtk2, gtk3, marco, unity, xfwm4
- Shiny: marco
- TraditionalGreen: gtk2, gtk3, marco
- TraditionalOk: gtk2, gtk3, marco, openbox, xfwm4

%package accessibility
Summary:	Accessibility themes for MATE environment
Summary(pl.UTF-8):	Motywy uprzystępniające dla środowiska MATE
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	mate-icon-theme >= 1.5

%description accessibility
Accessibility themes for MATE environment:

- HighContrastInverse: gtk2, gtk3, marco

%description accessibility -l pl.UTF-8
Motywy dla środowiska MATE o zwiększonej dostępności dla
niepełnosprawnych:

- HighContrastInverse: gtk2, gtk3, marco

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

for dir in $RPM_BUILD_ROOT%{_iconsdir}/*/; do
	gtk-update-icon-cache -ft $dir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/themes/BlackMATE
%{_datadir}/themes/BlackMATE-border
%{_datadir}/themes/BlueMenta
%{_datadir}/themes/BlueMenta-border
%{_datadir}/themes/Blue-Submarine
%{_datadir}/themes/Blue-Submarine-border
%{_datadir}/themes/GreenLaguna
%{_datadir}/themes/GreenLaguna-border
%{_datadir}/themes/Green-Submarine
%{_datadir}/themes/Green-Submarine-border
%{_datadir}/themes/Menta
%{_datadir}/themes/Menta-border
%{_datadir}/themes/Shiny
%{_datadir}/themes/TraditionalGreen
%{_datadir}/themes/TraditionalOk
%{_datadir}/themes/YaruGreen
%{_datadir}/themes/YaruOk
%{_iconsdir}/mate/cursors
%dir %{_iconsdir}/mate-black
%{_iconsdir}/mate-black/index.theme
%{_iconsdir}/mate-black/cursors

%files accessibility
%defattr(644,root,root,755)
%{_datadir}/themes/ContrastHigh
%{_datadir}/themes/HighContrastInverse
# note: top dirs (HighContrast/metacity-1) shared with metacity-themes-HighContrast 3.x
%{_datadir}/themes/HighContrast
%{_iconsdir}/ContrastHigh
