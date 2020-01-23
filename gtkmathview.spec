%define major 0
%define libname  %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	C++ rendering engine for MathML documents
Name:		gtkmathview
Version:	0.8.0
Release:	8
License:	GPLv3+
Group:		Networking/WWW
Url:		http://www.cs.unibo.it/helm/mml-widget/
Source0:	http://helm.cs.unibo.it/mml-widget/sources/%{name}-%{version}.tar.bz2
Source1:	gtkmathview.html.tar.bz2
Patch0: gtkmathview-0.8.0-cond-t1.patch
Patch1: gtkmathview-0.8.0-gcc43.patch
Patch2: gtkmathview-0.8.0-gcc44.patch
Patch3: gtkmathview-0.8.0-fix-link.patch
Patch4: gtkmathview-0.8.0-no-static.patch
Patch5: gtkmathview-0.8.0-gcc47.patch
Patch6: gtkmathview-0.8.0-gcc7.patch

BuildRequires:	xsltproc
BuildRequires:	t1lib-devel
BuildRequires:	popt-devel
#BuildRequires:	pkgconfig(gdome2-cpp-smart)
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
Provides: %{name}-devel = %{EVRD}

%description -n %{develname}
GtkMathView is a GTK Widget for rendering MathML documents.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1

# AM_BINRELOC missing, just ignore
echo 'AC_DEFUN([AM_BINRELOC], [])' > acinclude.m4

%build
autoreconf -fi
%configure \
	--disable-static

make

##Add updated html reference manual##
mkdir DATA.TMP
cd DATA.TMP
tar xjf %{SOURCE1}
cd ../../..

%install
%make_install
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



%changelog
* Tue Mar 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.8.0-5
+ Revision: 787563
- bump release
- cleaned up spec

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-4mdv2011.0
+ Revision: 610994
- rebuild

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 0.8.0-3mdv2010.1
+ Revision: 507035
- add pld linux patch to disable static build
- add gentoo patches to have it built
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.8.0-2mdv2008.1
+ Revision: 109226
- rebuild for new lzma

* Tue Oct 30 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 103829
- New release

* Fri Jun 22 2007 Funda Wang <fwang@mandriva.org> 0.7.8-1mdv2008.0
+ Revision: 42633
- New version
  Build against t1lib again

  + JÃ©rÃ´me Soyer <saispo@mandriva.org>
    - Import gtkmathview



* Mon Sep 04 2006 Jerome Soyer <saispo@mandriva.org> 0.7.7-2mdv2007.0
- Fix changelog

* Sun Sep 03 2006 Jerome Soyer <saispo@mandriva.org> 0.7.7-1mdv2007.0
- New release 0.7.7

* Fri Jul 21 2006 Charles A Edwards <eslrahc@mandriva.org> 0.7.5-6mdv2007.0
- rebuild

* Mon Jan 16 2006 Götz Waschk <waschk@mandriva.org> 0.7.5-5mdk
- fix buildrequires

* Sun Jan 15 2006 Götz Waschk <waschk@mandriva.org> 0.7.5-4mdk
- update build deps

* Mon Jan  2 2006 Götz Waschk <waschk@mandriva.org> 0.7.5-3mdk
- fix buildrequires

* Sat Nov 26 2005 Marcel Pol <mpol@mandriva.org> 0.7.5-2mdk
- mkrel
- small cleanups

* Thu Oct 06 2005 Marcel Pol <mpol@mandriva.org> 0.7.5-1mdk
- 0.7.5

* Wed Sep 28 2005 Marcel Pol <mpol@mandriva.org> 0.7.4-2mdk
- require fonts-ttf-latex

* Mon Sep 12 2005 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdk
- fix buildrequires
- New release 0.7.4

* Mon Aug 15 2005 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdk
- fix file list
- fix buildrequires
- 0.7.3

* Mon May  9 2005 Götz Waschk <waschk@mandriva.org> 0.4.3-4mdk
- multiarch

* Tue Jan 10 2005 Charles A Edwards <eslrahc@bellsouth.net> 0.4.3-3mdk
- rebuild without t1lib (build fails if latest is used)

* Fri Jun 11 2004 Götz Waschk <waschk@linux-mandrake.com> 0.4.3-2mdk
- spec cleanup
- fix deps
- patch for new g++

* Tue Jul 29 2003 Charles A Edwards <eslrahc@bellsouth.net> 0.4.3-1mdk
- 0.4.3
- drop gcc Patch...merged upstream
- build --with libxml2
- Requires/BuildRequires
- rm Info Post/Postrun (info dropped in 0.4.2)

* Tue Jul  8 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4.2-2mdk
- fix directory ownership

* Tue Jun 10 2003 Charles A Edwards <eslrahc@bellsouth.net> 0.4.2-1mdk
- release 0.4.2
- rm info, no longer created 
- add gtkmathview.pc
- BuildRequires/Requires gmetadom-devel>= 0.1.8

* Mon Jun  9 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4.1-2mdk
- move the config script to the devel package

* Sun May  4 2003 Götz Waschk <waschk@linux-mandrake.com> 0.4.1-1mdk
- from Charles A Edwards <eslrahc@bellsouth.net>:
  - initial Mdk release 
