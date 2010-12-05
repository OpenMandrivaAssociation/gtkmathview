%define name       gtkmathview
%define version    0.8.0
%define release    4

%define major 0
%define libname  %mklibname %name %major
%define develname %mklibname -d %name

Summary:    C++ rendering engine for MathML documents
Name:       %name
Version:    %version
Release:    %mkrel %release
License:    GPL
Group:      Networking/WWW
Url:            http://www.cs.unibo.it/helm/mml-widget/
Source:     http://helm.cs.unibo.it/mml-widget/sources/%{name}-%{version}.tar.bz2
Source1:         gtkmathview.html.tar.bz2
Patch0: gtkmathview-0.8.0-cond-t1.patch
Patch1: gtkmathview-0.8.0-gcc43.patch
Patch2: gtkmathview-0.8.0-gcc44.patch
Patch3: gtkmathview-0.8.0-fix-link.patch
Patch4: gtkmathview-0.8.0-no-static.patch
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
BuildRequires:    t1lib-devel >= 1.3
BuildRequires:    gmetadom-devel >= 0.1.8
BuildRequires:    libxml2-devel >= 2.2.0
BuildRequires:    gtk+2-devel
BuildRequires:    popt-devel
BuildRequires:    libxslt-proc
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
Obsoletes: %{_lib}gtkmathview0-devel < %version-%release

%description -n %develname
GtkMathView is a GTK Widget for rendering MathML documents.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1
# AM_BINRELOC missing, just ignore
echo 'AC_DEFUN([AM_BINRELOC], [])' > acinclude.m4

%build
autoreconf -fi
%configure2_5x --disable-static
%make

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

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

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
%_libdir/lib*.so.%{major}
%_libdir/lib*.so.%{major}.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_includedir}/*
%_libdir/pkgconfig/*
