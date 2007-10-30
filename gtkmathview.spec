%define name       gtkmathview
%define version    0.8.0
%define release    1

%define major 0
%define libname  %mklibname %name %major
%define develname %mklibname -d %name

Summary:    GtkMathView is a C++ rendering engine for MathML documents
Name:       %name
Version:    %version
Release:    %mkrel %release
License:    GPL
Group:      Networking/WWW
Url:            http://www.cs.unibo.it/helm/mml-widget/
Source:     http://helm.cs.unibo.it/mml-widget/sources/%{name}-%{version}.tar.bz2
Source1:         gtkmathview.html.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
#BuildRequires:   t1lib-devel >= 1.3
BuildRequires:    gmetadom-devel >= 0.1.8 autoconf2.5
BuildRequires:    libxml2-devel >= 2.2.0
BuildRequires:    libcairo-static-devel
BuildRequires:    freetype2-static-devel
BuildRequires:    X11-static-devel
BuildRequires:    gtk+2-devel
BuildRequires:    popt-devel
BuildRequires:    libxslt-proc
BuildRequires:    t1lib-static-devel
Requires:     gtk2 >= 2.4.0 t1lib >= 1.3 %libname = %version
Requires:         libxml2 >= 2.5.0
Requires:         %{_lib}gmetadom_gdome_cpp_smart0 >= 0.1.8
Requires:         fonts-ttf-latex

%description
GtkMathView is a GTK Widget for rendering MathML documents.

%package -n %libname
Summary:   Libraries for gtkmathview
Group: System/Libraries

%description -n %libname
GtkMathView is a GTK Widget for rendering MathML documents.

%package -n %develname
Summary:  Libraries and include files for gtkmathview
Group:    Development/C++
Requires: %libname = %version glib-devel >= 1.2.10 libxml2-devel >= 2.4.26
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %{libname}-devel

%description -n %develname
GtkMathView is a GTK Widget for rendering MathML documents.

%prep
%setup -q

%build
#configure2_5x --with-t1lib=no  --with-libxml2
%configure2_5x --with-libxml2

%make -j1

##Add updated html reference manual##
mkdir DATA.TMP
cd DATA.TMP
tar xjf %{SOURCE1}
cd ../../..

%install
rm -rf %buildroot
%makeinstall_std
mkdir -p %buildroot/%_docdir/%name
cp -r DATA.TMP/%name.html %buildroot/%_docdir/%name

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc AUTHORS BUGS COPYING ChangeLog HISTORY INSTALL LICENSE NEWS README TODO
%config(noreplace) %_sysconfdir/gtkmathview/gtkmathview.conf.xml
%_bindir/*
%_datadir/%name
%_mandir/man1/*

%files -n %libname
%defattr(-, root, root)
%_libdir/lib*.so.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_includedir}/*
%_libdir/pkgconfig/*
