%define major 0
%define libname  %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	C++ rendering engine for MathML documents
Name:		gtkmathview
Version:	0.8.0
Release:	5
License:	GPL
Group:		Networking/WWW
Url:		http://www.cs.unibo.it/helm/mml-widget/
Source0:	http://helm.cs.unibo.it/mml-widget/sources/%{name}-%{version}.tar.bz2
Source1:	gtkmathview.html.tar.bz2
Patch0: gtkmathview-0.8.0-cond-t1.patch
Patch1: gtkmathview-0.8.0-gcc43.patch
Patch2: gtkmathview-0.8.0-gcc44.patch
Patch3: gtkmathview-0.8.0-fix-link.patch
Patch4: gtkmathview-0.8.0-no-static.patch

BuildRequires:	xsltproc
BuildRequires:	t1lib-devel
BuildRequires:	popt-devel
BuildRequires:	pkgconfig(gdome2-cpp-smart)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
Requires:	fonts-ttf-latex

%description
GtkMathView is a GTK Widget for rendering MathML documents.

%package -n %{libname}
Summary:   Libraries for gtkmathview
Group: System/Libraries

%description -n %{libname}
GtkMathView is a GTK Widget for rendering MathML documents.

%package -n %{develname}
Summary:  Libraries and include files for gtkmathview
Group:    Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}gtkmathview0-devel < %{version}-%{release}

%description -n %{develname}
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
%configure2_5x \
	--disable-static

%make

##Add updated html reference manual##
mkdir DATA.TMP
cd DATA.TMP
tar xjf %{SOURCE1}
cd ../../..

%install
%makeinstall_std
mkdir -p %{buildroot}/%_docdir/%{name}
cp -r DATA.TMP/%{name}.html %{buildroot}/%_docdir/%{name}

%files
%doc AUTHORS BUGS COPYING ChangeLog HISTORY INSTALL LICENSE NEWS README TODO
%config(noreplace) %{_sysconfdir}/gtkmathview/gtkmathview.conf.xml
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

