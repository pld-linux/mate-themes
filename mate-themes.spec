#
# Conditional build:
%bcond_without	a11y	# all accessibility themes (only core a11y themes otherwise)

%define	gtk3_mver	3.16
Summary:	MATE Desktop themes
Summary(pl.UTF-8):	Motywy dla środowiska MATE Desktop
Name:		mate-themes
Version:	1.10.4
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.10/%{name}-gtk%{gtk3_mver}-%{version}.tar.xz
# Source0-md5:	3053f544823d6d0d529aaf005bf4aabe
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gdk-pixbuf2-devel >= 2.0.0
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	intltool >= 0.35.0
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
- TraditionalOkTest: gtk2, gtk3, marco

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
- TraditionalOkTest: gtk2, gtk3, marco

%package accessibility
Summary:	Accessibility themes for MATE environment
Summary(pl.UTF-8):	Motywy uprzystępniające dla środowiska MATE
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	mate-icon-theme >= 1.5

%description accessibility
Accessibility themes for MATE environment:

- ContrastHigh: gtk2, gtk3, marco
- ContrastHighInverse: gtk2, gtk3, marco

%description accessibility -l pl.UTF-8
Motywy dla środowiska MATE o zwiększonej dostępności dla
niepełnosprawnych:

- ContrastHigh: gtk2, gtk3, marco
- ContrastHighInverse: gtk2, gtk3, marco

%prep
%setup -q -n %{name}-gtk%{gtk3_mver}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{__enable_disable a11y all-themes} \
	--enable-icon-mapping \
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/themes/BlackMATE
%{_datadir}/themes/BlueMenta
%{_datadir}/themes/Blue-Submarine
%{_datadir}/themes/GreenLaguna
%{_datadir}/themes/Green-Submarine
%{_datadir}/themes/Menta
%{_datadir}/themes/Shiny
%{_datadir}/themes/TraditionalGreen
%{_datadir}/themes/TraditionalOk
%{_datadir}/themes/TraditionalOkTest
%{_iconsdir}/mate/cursors

%files accessibility
%defattr(644,root,root,755)
%{_datadir}/themes/ContrastHigh
%{_datadir}/themes/ContrastHighInverse
%{_iconsdir}/ContrastHigh
